from Model import Model
import os
import platform
from datetime import datetime, timedelta
"""
安裝: pip install python-crontab
"""
from crontab import CronTab

class Controller():
    def __init__(self):
        """
        初始化
        """
        self.model = Model()

    def determine(self):
        """
        決定天氣資料是否符合使用者需求
        輸入：無
        回傳：bool(是否符合使用者需求) (讓getMessage call)
        """
        check = True

        # 用Temp, Hum, Rain, Uv 存取回傳的使用者各項喜好大小值
        metrics = self.model.getConfigField('metrics')
        Temp =  metrics['temp']
        Hum = metrics['hum']
        Rain = metrics['rain']
        Uv = metrics['uv']

        # 預設為True，如果使用者有設定任一項天氣指標(list不為空)且天氣不介於這項指標喜好大小值之前，則回傳False(目前想法是一項不符合即表示不建議出門，可以再討論)
        if len(Temp) == 2 and (self.model.getWeatherData('temp') <= Temp[0] or self.model.getWeatherData('temp') >= Temp[1]):
            check = False
        if len(Hum) == 2 and (self.model.getWeatherData('hum') <= Hum[0] or self.model.getWeatherData('hum') >= Hum[1]):
            check = False
        if len(Rain) == 2 and (self.model.getWeatherData('rain') <= Rain[0] or self.model.getWeatherData('rain') >= Rain[1]):
            check = False
        if len(Uv) == 2 and (self.model.getWeatherData('uv') <= Uv[0] or self.model.getWeatherData('uv') >= Uv[1]):
            check = False

        return check

    def setCron(self, command: str=''):
        """
        設定contab
        輸入：暫無 固定參照config的資訊傳送line通知
        回傳：bool(是否寫入成功)
        Comments: 使用python-crontab (?) / 當通知時間被設定時要執行，並用python-crontab更改/新增/刪除 crontab jobs / command可能就是"python3 [abs path]/line.py"
        Comments: windows跑需要管理員權限 unix-like若沒限制crontab執行權限則都可
        """
        # check python command
        py = os.system('python -V')
        py3 = os.system('python3 -V')
        if not (py and py3):
            py_command = 'python3' if not py3 else 'python'
        else:
            print('Please input your command of running python scripts.(like "python3" or "python")')
            py_command = input()        

        work_dir = os.getcwd()
        cron_file_name = 'line.py'
        task_name = "OOPLine"
        days = self.getConfigField('days')
        time = self.getConfigField('time')        
	
        if not platform.system().lower() == 'windows':
            my_cron = CronTab(user=True)
            my_cron.remove_all(comment=task_name)
            if len(days) == 0:
                return True
            my_cron.env['PATH'] = '/bin:/usr/bin:/usr/local/bin'
            job = my_cron.new(command=f'cd {work_dir} && python {work_dir}/{cron_file_name}',comment=task_name)

            job.minute.on(10*time[-2]+time[-1])
            job.hour.on(10*time[0]+time[1])
            job.dow.on(*[day%7 for day in days])
            my_cron.write(user=True)
            return True
        else:
            if len(days) == 0:
                os.system(f'schtasks /Delete /F /TN {task_name}')
                return True
            week_name = ['SUN','MON','TUE','WED','THU','FRI','SAT']
            weekday = ' '.join([week_name[i%7] for i in days])
            run_time = time[:2]+':'+time[2:]

            now = datetime.now()
            end_time = now.strftime("%H:%M")
            end_date = (now + timedelta(days=7)).strftime("%Y/%m/%d")

            # schedule the notification, runs exactly one time at each specified time and date
            os.system(f'schtasks /Create /F /Z /TN {task_name} \
		                 /TR "{py_command} {work_dir}/{cron_file_name}" \
		                 /SC WEEKLY \
		                 /D "{weekday}" \
		                 /ST {run_time} \
		                 /ED {end_date} \
		                 /ET {end_time} \
		                 /RI 0 \
            ')
            os.system(f'schtasks /Query /TN {task_name} /XML > config.xml')
            config = open('./config.xml', 'r', encoding='cp950')
            config_add = open('./config_add.xml', 'w', encoding='cp950')
            while True:
                line = config.readline()
                if line == '':
                    break
                config_add.write(line)
                if '<Arguments>' in line:
                    add_line = '\n' + line[:line.index('<')] + f'<WorkingDirectory>{work_dir}</WorkingDirectory>\n'
                    config_add.write(add_line)
            config.close()
            config_add.close()
            os.system(f'schtasks /Create /F /TN {task_name} /XML config_add.xml')
            try:
                os.remove('./config.xml')
                os.remove('./config_add.xml')
            except:
                #os.remove('./config.xml')
                #os.remove('./config_add.xml')
                pass
            finally:
                return True

    def getMessage(self):
        """
        取得要通知的訊息內容
        輸入：無
        回傳：str(要輸出的訊息字串) (call determine並根據config產生對應字串)
        """
        temp_t = self.model.getWeatherData('temp')
        hum_t = self.model.getWeatherData('hum')
        rain_t = self.model.getWeatherData('rain')
        uv_t = self.model.getWeatherData('uv')

        # temp_t = 10
        # hum_t = 20
        # rain_t = 30
        # uv_t = 40

        """
        預設是建不建議做甚麼事的msg為使用者自己設定，
        例如這是他要判斷要不要去早八的，message_post_t就可能是:[可以去上早八]
        或是判斷打球的，message_post_f就可能是:[不建議去打球]
        所以msg沒寫入任何建議/不建議等字樣(這點也可以大家討論)
        """
        if self.determine():
            msg = str(self.model.getConfigField('message_pre_t')) + "\n今天溫度為攝氏" + str(temp_t) + "度\n濕度為" + str(hum_t) + "%\n降雨機率為" + str(rain_t) + "%\n紫外線指數為" + str(uv_t) + "\n" + str(self.model.getConfigField('message_post_t'))
        else:
            msg = str(self.model.getConfigField('message_pre_f')) + "\n今天溫度為攝氏" + str(temp_t) + "度\n濕度為" + str(hum_t) + "%\n降雨機率為" + str(rain_t) + "%\n紫外線指數為" + str(uv_t) + "\n" + str(self.model.getConfigField('message_post_f'))
        return msg
    def getMessagePrev(self):
        """
        取得要通知的訊息內容
        輸入：無
        回傳：str(要輸出的訊息字串) (call determine並根據config產生對應字串)
        """
        temp_t = self.model.getWeatherData('temp')
        hum_t = self.model.getWeatherData('hum')
        rain_t = self.model.getWeatherData('rain')
        uv_t = self.model.getWeatherData('uv')

        # temp_t = 10
        # hum_t = 20
        # rain_t = 30
        # uv_t = 40

        """
        預設是建不建議做甚麼事的msg為使用者自己設定，
        例如這是他要判斷要不要去早八的，message_post_t就可能是:[可以去上早八]
        或是判斷打球的，message_post_f就可能是:[不建議去打球]
        所以msg沒寫入任何建議/不建議等字樣(這點也可以大家討論)
        """
        if self.determine():
            msg = str(self.model.getConfigField('message_pre_t')) + "\n今天溫度為攝氏" + str(temp_t) + "度\n濕度為" + str(hum_t) + "%\n降雨機率為" + str(rain_t) + "%\n紫外線指數為" + str(uv_t) + "\n" + str(self.model.getConfigField('message_post_t'))
        else:
            msg = str(self.model.getConfigField('message_pre_f')) + "\n今天溫度為攝氏" + str(temp_t) + "度\n濕度為" + str(hum_t) + "%\n降雨機率為" + str(rain_t) + "%\n紫外線指數為" + str(uv_t) + "\n" + str(self.model.getConfigField('message_post_f'))
        return msg

    def addLineList(self, line_token: str):
        """
        新增Line token
        輸入：line token(單一一個)
        回傳：bool(寫入成功與否)
        Comments: 讓GUI的新增token按鈕call的，可能可以改成回傳str讓GUI顯示是否成功等
        """
        return self.model.setLineList(line_token, "add")
        # more instructions

    def delLineList(self, line_token: str):
        """
        刪除Line token
        輸入：line token(單一一個)
        回傳：bool(刪除成功與否)
        Comments: 讓GUI的刪除token按鈕call的，可能可以改成回傳str讓GUI顯示是否成功等
        """
        return self.model.setLineList(line_token, "del")
        # more instructions

    # 以下是直接call model的method (可能不需要更動)
    def getWeatherData(self, elementName: str):
        """
        取得特定某項天氣資料
        輸入：elementName(資料項目，參考api)
        回傳：int(數值) (or None, no data)
        """
        return self.model.getWeatherData(elementName)

    def getConfigField(self, field: str):
        """
        取得特定一項config資料(除了line token lists(因為可能多個tokens所以另外處理))
        輸入：field(config參數名稱)
        回傳：Any(該參數內容) (or None, no data)
        Comments: 直接call model的method
        """
        return self.model.getConfigField(field)

    def setConfigField(self, field: str, value: any):
        """
        設定特定一項config資料(除了line token lists)
        輸入：field(config參數名稱), value(參數數值)
        回傳：bool(寫入成功與否)
        Comments: 直接call model的method
        """
        return self.model.setConfigField(field, value)

    def getLineList(self):
        """
        取得Line tokens list
        輸入：無
        回傳：list(要送的line user list)
        Comments: 直接call model的method
        """
        return self.model.getLineList()
