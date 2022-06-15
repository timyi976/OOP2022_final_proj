from Control import Controller
from PyQt5 import QtWidgets, QtCore
from ui import Ui_Form
import sys

class PopUp(QtWidgets.QMessageBox):
    """
    顯示預覽通知訊息的彈出視窗
    """
    def __init__(self):
        QtWidgets.QMessageBox.__init__(self)
        self.setWindowTitle("通知訊息預覽")
        self.setText("")
        self.setStandardButtons(QtWidgets.QMessageBox.Ok)

    def showMessage(self, msg: str, title: str):
        self.setWindowTitle(title)
        self.setText(msg)
        self.show()

class view(Ui_Form):
    def __init__(self):
        # super(view, self).__init__()

        self.app = QtWidgets.QApplication(sys.argv)
        self.form = QtWidgets.QMainWindow()
        self.popup = PopUp()
        self.setupUi(self.form)

        # line show button state (True of displaying "顯示所有")
        self.line_show_state = True

        # additional; need to move to view.py
        self.preview_pushButton.clicked.connect(self.preview_button)
        self.save_pushButton.clicked.connect(self.save_button)
        self.line_add_pushButton.clicked.connect(self.line_add_button)
        self.line_del_pushButton.clicked.connect(self.line_del_button)
        self.line_show_pushButton.clicked.connect(self.line_show_button)
        self.temp_checkBox.stateChanged.connect(self.temp_state_action)
        self.uv_checkBox.stateChanged.connect(self.uv_state_action)
        self.hum_checkBox.stateChanged.connect(self.hum_state_action)
        self.rain_checkBox.stateChanged.connect(self.rain_state_action)

    def temp_disabled(self):
        self.label_min_temp.setDisabled(True)
        self.label_max_temp.setDisabled(True)
        self.temp_min_spinBox.setDisabled(True)
        self.temp_max_spinBox.setDisabled(True)

    def temp_enabled(self):
        self.label_min_temp.setDisabled(False)
        self.label_max_temp.setDisabled(False)
        self.temp_min_spinBox.setDisabled(False)
        self.temp_max_spinBox.setDisabled(False)

    def uv_disabled(self):
        self.label_min_uv.setDisabled(True)
        self.label_max_uv.setDisabled(True)
        self.uv_min_spinBox.setDisabled(True)
        self.uv_max_spinBox.setDisabled(True)

    def uv_enabled(self):
        self.label_min_uv.setDisabled(False)
        self.label_max_uv.setDisabled(False)
        self.uv_min_spinBox.setDisabled(False)
        self.uv_max_spinBox.setDisabled(False)

    def hum_disabled(self):
        self.label_min_hum.setDisabled(True)
        self.label_max_hum.setDisabled(True)
        self.hum_min_spinBox.setDisabled(True)
        self.hum_max_spinBox.setDisabled(True)

    def hum_enabled(self):
        self.label_min_hum.setDisabled(False)
        self.label_max_hum.setDisabled(False)
        self.hum_min_spinBox.setDisabled(False)
        self.hum_max_spinBox.setDisabled(False)

    def rain_disabled(self):
        self.label_min_rain.setDisabled(True)
        self.label_max_rain.setDisabled(True)
        self.rain_min_spinBox.setDisabled(True)
        self.rain_max_spinBox.setDisabled(True)

    def rain_enabled(self):
        self.label_min_rain.setDisabled(False)
        self.label_max_rain.setDisabled(False)
        self.rain_min_spinBox.setDisabled(False)
        self.rain_max_spinBox.setDisabled(False)

    def init_form_data(self):
        # init checkbox state
        # and fill in current config
        self.city_lineEdit.setText(self.controller.getConfigField('city'))
        self.town_lineEdit.setText(self.controller.getConfigField('district'))
        self.time_timeEdit.setTime(QtCore.QTime.fromString(self.controller.getConfigField('time'), "hhmm"))

        day_lis = self.controller.getConfigField('days')
        if 1 in day_lis:
            self.mon_checkBox.setCheckState(2)
        if 2 in day_lis:
            self.tue_checkBox.setCheckState(2)
        if 3 in day_lis:
            self.wed_checkBox.setCheckState(2)
        if 4 in day_lis:
            self.thu_checkBox.setCheckState(2)
        if 5 in day_lis:
            self.fri_checkBox.setCheckState(2)
        if 6 in day_lis:
            self.sat_checkBox.setCheckState(2)
        if 7 in day_lis:
            self.sun_checkBox.setCheckState(2)

        metrics = self.controller.getConfigField('metrics')
        if len(metrics["temp"]) == 2:
            self.temp_checkBox.setCheckState(2)
            self.temp_min_spinBox.setValue(metrics["temp"][0])
            self.temp_max_spinBox.setValue(metrics["temp"][1])
            self.temp_enabled()
        else:
            self.temp_disabled()

        if len(metrics["uv"]) == 2:
            self.uv_checkBox.setCheckState(2)
            self.uv_min_spinBox.setValue(metrics["uv"][0])
            self.uv_max_spinBox.setValue(metrics["uv"][1])
            self.uv_enabled()
        else:
            self.uv_disabled()

        if len(metrics["hum"]) == 2:
            self.hum_checkBox.setCheckState(2)
            self.hum_min_spinBox.setValue(metrics["hum"][0])
            self.hum_max_spinBox.setValue(metrics["hum"][1])
            self.hum_enabled()
        else:
            self.hum_disabled()

        if len(metrics["rain"]) == 2:
            self.rain_checkBox.setCheckState(2)
            self.rain_min_spinBox.setValue(metrics["rain"][0])
            self.rain_max_spinBox.setValue(metrics["rain"][1])
            self.rain_enabled()
        else:
            self.rain_disabled()

        self.msgT_pre_textEdit.setText(self.controller.getConfigField('message_pre_t'))
        self.msgT_post_textEdit.setText(self.controller.getConfigField('message_post_t'))
        self.msgF_pre_textEdit.setText(self.controller.getConfigField('message_pre_f'))
        self.msgF_post_textEdit.setText(self.controller.getConfigField('message_post_f'))

    def start_ui(self):
        self.form.show()
        sys.exit(self.app.exec_())

    def set_controller(self, controller):
        self.controller = controller
        self.init_form_data()

    def temp_state_action(self):
        if self.temp_checkBox.isChecked():
            self.temp_enabled()
        else:
            self.temp_disabled()

    def uv_state_action(self):
        if self.uv_checkBox.isChecked():
            self.uv_enabled()
        else:
            self.uv_disabled()

    def hum_state_action(self):
        if self.hum_checkBox.isChecked():
            self.hum_enabled()
        else:
            self.hum_disabled()

    def rain_state_action(self):
        if self.rain_checkBox.isChecked():
            self.rain_enabled()
        else:
            self.rain_disabled()

    def save_button(self):
        d = dict()
        day_lis = []

        if self.check_location() == 0:
            print("location_error")
            return

        d["city"] = self.city_lineEdit.text()
        # 處理'臺' '台'
        if d["city"][0] == '台':
            d["city"][0] = '臺'
            self.city_lineEdit.setText(d["city"])
        
        d["district"] = self.town_lineEdit.text()

        if self.mon_checkBox.checkState() == 2:
            day_lis.append(1)
        if self.tue_checkBox.checkState() == 2:
            day_lis.append(2)
        if self.wed_checkBox.checkState() == 2:
            day_lis.append(3)
        if self.thu_checkBox.checkState() == 2:
            day_lis.append(4)
        if self.fri_checkBox.checkState() == 2:
            day_lis.append(5)
        if self.sat_checkBox.checkState() == 2:
            day_lis.append(6)
        if self.sun_checkBox.checkState() == 2:
            day_lis.append(7)
        d["days"] = day_lis
        # print(self.time_timeEdit.dateTime().toString("HHmm"))
        d["time"] = self.time_timeEdit.dateTime().toString("HHmm")

        if self.check_value() == 0:
            print("value_error")
            return

        d["metrics"] = {}
        if self.hum_checkBox.checkState() == 2:
            d["metrics"]["hum"] = [self.hum_min_spinBox.value(), self.hum_max_spinBox.value()]
        else:
            d["metrics"]["hum"] = []

        if self.temp_checkBox.checkState() == 2:
            d["metrics"]["temp"] = [self.temp_min_spinBox.value(), self.temp_max_spinBox.value()]
        else:
            d["metrics"]["temp"] = []

        if self.rain_checkBox.checkState() == 2:
            d["metrics"]["rain"] = [self.rain_min_spinBox.value(), self.rain_max_spinBox.value()]
        else:
            d["metrics"]["rain"] = []

        if self.uv_checkBox.checkState() == 2:
            d["metrics"]["uv"] = [self.uv_min_spinBox.value(), self.uv_max_spinBox.value()]
        else:
            d["metrics"]["uv"] = []

        d["user"] = self.controller.getLineList()

        d["message_pre_t"] = self.msgT_pre_textEdit.toPlainText()
        d["message_post_t"] = self.msgT_post_textEdit.toPlainText()
        d["message_pre_f"] = self.msgF_pre_textEdit.toPlainText()
        d["message_post_f"] = self.msgF_post_textEdit.toPlainText()


        self.controller.setConfigField('city', d["city"])
        self.controller.setConfigField('district', d["district"])
        self.controller.setConfigField('days', d["days"])
        self.controller.setConfigField('time', d["time"])
        self.controller.setConfigField('metrics', d["metrics"])
        self.controller.setConfigField('user', d["user"])
        self.controller.setConfigField('message_pre_t', d["message_pre_t"])
        self.controller.setConfigField('message_post_t', d["message_post_t"])
        self.controller.setConfigField('message_pre_f', d["message_pre_f"])
        self.controller.setConfigField('message_post_f', d["message_post_f"])

        """
        儲存設定後直接排定通知
        """
        # self.controller.setCron()

        self.popup.showMessage("設定儲存成功！","設定成功通知")

        print(d)

    def preview_button(self):
        self.save_button()
        self.popup.showMessage(self.controller.getMessagePrev(),"通知訊息預覽")

    def delay_exec(self, delay, func):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(func)
        self.timer.start(delay)

    def hide_line_message(self):
        if self.line_show_state == True:
            self.line_result_label.setText("")
        self.line_result_label.setStyleSheet("color: black")

    def hide_location_message(self):
        self.label_error_location.setText("                 ")
        self.label_error_location.setStyleSheet("color: black")

    def hide_value_message(self):
        self.label_error_value.setText("")
        self.label_error_value.setStyleSheet("color: black")

    def line_add_button(self):
        ret = self.controller.addLineList(self.line_lineEdit.text())
        self.line_show_state = True
        self.line_show_pushButton.setText("顯示所有使用者")
        if ret == 1:
            self.line_result_label.setStyleSheet("color: green")
            # self.line_result_label.setText("Successfully add new user: {}".format(self.line_lineEdit.text()))
            self.line_result_label.setText("成功新增使用者: {}".format(self.line_lineEdit.text()))
            self.delay_exec(3000, self.hide_line_message)
        elif ret == 0:
            self.line_result_label.setStyleSheet("color: red")
            # self.line_result_label.setText("Fail to add user: {}".format(self.line_lineEdit.text()))
            self.line_result_label.setText("無法新增使用者: {}".format(self.line_lineEdit.text()))
            self.delay_exec(3000, self.hide_line_message)
        elif ret == -1:
            self.line_result_label.setStyleSheet("color: red")
            self.line_result_label.setText("使用者欄位不可為空！")
            self.delay_exec(3000, self.hide_line_message)
        self.line_lineEdit.setText("")

    def line_del_button(self):
        ret = self.controller.delLineList(self.line_lineEdit.text())
        self.line_show_state = True
        self.line_show_pushButton.setText("顯示所有使用者")
        if ret == 1:
            self.line_result_label.setStyleSheet("color: green")
            # self.line_result_label.setText("Successfully delete user: {}".format(self.line_lineEdit.text()))
            self.line_result_label.setText("成功刪除使用者: {}".format(self.line_lineEdit.text()))
            self.delay_exec(3000, self.hide_line_message)
        elif ret == 0:
            self.line_result_label.setStyleSheet("color: red")
            # self.line_result_label.setText("Fail to delete user: {}".format(self.line_lineEdit.text()))
            self.line_result_label.setText("無法刪除使用者: {}".format(self.line_lineEdit.text()))
            self.delay_exec(3000, self.hide_line_message)
        elif ret == -1:
            self.line_result_label.setStyleSheet("color: red")
            self.line_result_label.setText("使用者欄位不可為空！")
            self.delay_exec(3000, self.hide_line_message)
        self.line_lineEdit.setText("")

    def line_show_button(self):
        if self.line_show_state:
            self.line_result_label.setStyleSheet("color: black")
            lst = self.controller.getLineList()
            if len(lst) != 0:
                self.line_result_label.setText(str(self.controller.getLineList()))
            else:
                self.line_result_label.setText("目前無使用者")
            self.line_show_pushButton.setText("隱藏所有使用者")
            self.line_show_state = False
        else:
            self.line_result_label.setText("")
            self.line_show_pushButton.setText("顯示所有使用者")
            self.line_show_state = True

    def check_location(self):
        d = {"宜蘭縣": ['頭城鎮', '礁溪鄉', '壯圍鄉', '員山鄉', '宜蘭市', '大同鄉', '五結鄉', '三星鄉', '羅東鎮', '冬山鄉', '南澳鄉', '蘇澳鎮'],
             '桃園市': ['大園區', '蘆竹區', '觀音區', '龜山區', '桃園區', '中壢區', '新屋區', '八德區', '平鎮區', '楊梅區', '大溪區', '龍潭區', '復興區'],
             '新竹縣': ['新豐鄉', '湖口鄉', '新埔鎮', '竹北市', '關西鎮', '芎林鄉', '竹東鎮', '寶山鄉', '尖石鄉', '橫山鄉', '北埔鄉', '峨眉鄉', '五峰鄉'],
             '苗栗縣': ['竹南鎮', '頭份市', '三灣鄉', '造橋鄉', '後龍鎮', '南庄鄉', '頭屋鄉', '獅潭鄉', '苗栗市', '西湖鄉', '通霄鎮', '公館鄉', '銅鑼鄉', '泰安鄉',
                     '苑裡鎮', '大湖鄉', '三義鄉', '卓蘭鎮'],
             '彰化縣': ['伸港鄉', '和美鎮', '線西鄉', '鹿港鎮', '彰化市', '秀水鄉', '福興鄉', '花壇鄉', '芬園鄉', '芳苑鄉', '埔鹽鄉', '大村鄉', '二林鎮', '員林市',
                     '溪湖鎮', '埔心鄉', '永靖鄉', '社頭鄉', '埤頭鄉', '田尾鄉', '大城鄉', '田中鎮', '北斗鎮', '竹塘鄉', '溪州鄉', '二水鄉'],
             '南投縣': ['仁愛鄉', '國姓鄉', '埔里鎮', '草屯鎮', '中寮鄉', '南投市', '魚池鄉', '水里鄉', '名間鄉', '信義鄉', '集集鎮', '竹山鎮', '鹿谷鄉'],
             '嘉義縣': ['大林鎮', '溪口鄉', '阿里山鄉', '梅山鄉', '新港鄉', '民雄鄉', '六腳鄉', '竹崎鄉', '東石鄉', '太保市', '番路鄉', '朴子市', '水上鄉', '中埔鄉',
                     '布袋鎮', '鹿草鄉', '義竹鄉', '大埔鄉'],
             '雲林縣': ['麥寮鄉', '二崙鄉', '崙背鄉', '西螺鎮', '莿桐鄉', '林內鄉', '臺西鄉', '土庫鎮', '虎尾鎮', '褒忠鄉', '東勢鄉', '斗南鎮', '四湖鄉', '古坑鄉',
                     '元長鄉', '大埤鄉', '口湖鄉', '北港鎮', '水林鄉', '斗六市'],
             '屏東縣': ['高樹鄉', '三地門鄉', '霧臺鄉', '里港鄉', '鹽埔鄉', '九如鄉', '長治鄉', '瑪家鄉', '屏東市', '內埔鄉', '麟洛鄉', '泰武鄉', '萬巒鄉', '竹田鄉',
                     '萬丹鄉', '來義鄉', '潮州鎮', '新園鄉', '崁頂鄉', '新埤鄉', '南州鄉', '東港鎮', '林邊鄉', '佳冬鄉', '春日鄉', '獅子鄉', '琉球鄉', '枋山鄉',
                     '牡丹鄉', '滿州鄉', '車城鄉', '恆春'],
             '臺東縣': ['長濱鄉', '海端鄉', '池上鄉', '成功鎮', '關山鎮', '東河鄉', '鹿野鄉', '延平鄉', '卑南鄉', '臺東市', '太麻里鄉', '綠島鄉', '達仁鄉', '大武鄉',
                     '蘭嶼鄉', '金峰鄉'],
             '花蓮縣': ['秀林鄉', '新城鄉', '花蓮市', '吉安鄉', '壽豐鄉', '萬榮鄉', '鳳林鎮', '豐濱鄉', '光復鄉', '卓溪鄉', '瑞穗鄉', '玉里鎮', '富里鄉'],
             '澎湖縣': ['白沙鄉', '西嶼鄉', '湖西鄉', '馬公市', '望安鄉', '七美鄉'],
             '基隆市': ['安樂區', '中山區', '中正區', '七堵區', '信義區', '仁愛區', '暖暖區'],
             '新竹市': ['北區', '香山區', '東區'],
             '嘉義市': ['東區', '西區'],
             '臺北市': ['北投區', '士林區', '內湖區', '中山區', '大同區', '松山區', '南港區', '中正區', '萬華區', '信義區', '大安區', '文山區'],
             '高雄市': ['楠梓區', '左營區', '三民區', '鼓山區', '苓雅區', '新興區', '前金區', '鹽埕區', '前鎮區', '旗津區', '小港區', '那瑪夏區', '甲仙區', '六龜區',
                     '杉林區', '內門區', '茂林區', '美濃區', '旗山區', '田寮區', '湖內區', '茄萣區', '阿蓮區', '路竹區', '永安區', '岡山區', '燕巢區', '彌陀區',
                     '橋頭區', '大樹區', '梓官區', '大社區', '仁武區', '鳥松區', '大寮區', '鳳山區', '林園區', '桃源區'],
             '新北市': ['石門區', '三芝區', '金山區', '淡水區', '萬里區', '八里區', '汐止區', '林口區', '五股區', '瑞芳區', '蘆洲區', '雙溪區', '三重區', '貢寮區',
                     '平溪區', '泰山區', '新莊區', '石碇區', '板橋區', '深坑區', '永和區', '樹林區', '中和區', '土城區', '新店區', '坪林區', '鶯歌區', '三峽區',
                     '烏來區'],
             '臺中市': ['北屯區', '西屯區', '北區', '南屯區', '西區', '東區', '中區', '南區', '和平區', '大甲區', '大安區', '外埔區', '后里區', '清水區', '東勢區',
                     '神岡區', '龍井區', '石岡區', '豐原區', '梧棲區', '新社區', '沙鹿區', '大雅區', '潭子區', '大肚區', '太平區', '烏日區', '大里區', '霧峰區'],
             '臺南市': ['安南區', '中西區', '安平區', '東區', '南區', '北區', '白河區', '後壁區', '鹽水區', '新營區', '東山區', '北門區', '柳營區', '學甲區',
                     '下營區', '六甲區', '南化區', '將軍區', '楠西區', '麻豆區', '官田區', '佳里區', '大內區', '七股區', '玉井區', '善化區', '西港區', '山上區',
                     '安定區', '新市區', '左鎮區', '新化區', '永康區', '歸仁區', '關廟區', '龍崎區', '仁德區'],
             '連江縣': ['南竿鄉', '北竿鄉', '莒光鄉', '東引鄉'],
             '金門縣': ['金城鎮', '金湖鎮', '金沙鎮', '金寧鄉', '烈嶼鄉', '烏坵鄉'],
             }
        if self.city_lineEdit.text() in d.keys() and (d[self.city_lineEdit.text()].count(self.town_lineEdit.text()) != 0 or self.town_lineEdit.text() == ""):
            return 1
        else:
            self.error_location()
            return 0

    def check_value(self):
        if self.hum_min_spinBox.value() > self.hum_max_spinBox.value():
            self.error_value()
            return 0
        if self.temp_min_spinBox.value() > self.temp_max_spinBox.value():
            self.error_value()
            return 0
        if self.rain_min_spinBox.value() > self.rain_max_spinBox.value():
            self.error_value()
            return 0
        if self.uv_min_spinBox.value() > self.uv_max_spinBox.value():
            self.error_value()
            return 0

        return 1

    def error_value(self):
        self.label_error_value.setStyleSheet("color: red")
        # self.line_result_label.setText("Fail to add user: {}".format(self.line_lineEdit.text()))
        self.label_error_value.setText("最小值不能大於最大值!")
        self.delay_exec(3000, self.hide_value_message)

    def error_location(self):
        self.label_error_location.setStyleSheet("color: red")
        self.label_error_location.setText("地區錯誤!!")
        self.delay_exec(3000, self.hide_location_message)

if __name__ == '__main__':
    controller = Controller()
    view = view()
    view.set_controller(controller)
    view.start_ui()