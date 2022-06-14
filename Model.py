# import api
import json
import os

class Model():
    def __init__(self):
        """
        初始化config file或是api等
        """
        self.config = {"days": [1, 2, 3, 4, 5, 6, 7],
                       "time": "0730",
                       "metrics": {"temp": [], "hum": [], "rain": [], "uv": []},
                       "city": "臺北市",
                       "district": "大安區",
                       "user": [],
                       "message_pre_t": "你好！\n",
                       "message_post_t": "\n適合上早八！\n",
                       "message_pre_f": "你好！\n",
                       "message_post_f": "\n不適合上早八！\n"}

        self.config_path = './config.json'
        if os.path.exists(self.config_path):
            self.readConfig(self.config_path)
        else:
            self.writeConfig(self.config_path, self.config)
        # self.api = api.api()

    # 以下是讓model自己使用的
    def getWeatherAPIData(self, city: str, town: str):
        """
        從api取得天氣資料
        輸入：city(縣市), town(鄉鎮市區)
        回傳： dict(天氣資料) (or None, no data)
        """
        pass

    def readConfig(self, file: str):
        """
        讀取config file並存成dict
        輸入：file(檔案路徑)
        回傳：dict(各項config數值) (or None, no data)
        """
        with open(file, 'r') as config_file:
            config = json.load(config_file)

        return config

    def writeConfig(self, file: str, config: dict):
        """
        寫入config file
        輸入：file(檔案路徑), config
        回傳：bool(寫入成功與否)
        """
        with open(file, 'w') as config_file:
            json.dump(config, config_file)

    # 以下是讓controller可以呼叫使用的
    def getWeatherData(self, elementName: str):
        """
        取得特定某項天氣資料
        輸入：elementName(資料項目，參考api)
        回傳：int(數值) (or None, no data)
        """
        if elementName == 'temp':
            return 10
        elif elementName == 'hum':
            return 20
        elif elementName == 'rain':
            return 30
        elif elementName == 'uv':
            return 40
        pass

    def getConfigField(self, field: str):
        """
        取得特定一項config資料(除了line token lists(因為可能多個tokens所以另外處理))
        輸入：field(config參數名稱)
        回傳：Any(該參數內容) (or None, no data)
        """
        d = self.readConfig(self.config_path)
        return d[field]

    def setConfigField(self, field: str, value: any):
        """
        設定特定一項config資料(除了line token lists)
        輸入：field(config參數名稱), value(參數數值)
        回傳：bool(寫入成功與否)
        """
        d = self.readConfig(self.config_path)
        d[field] = value
        self.config = d
        self.writeConfig(self.config_path, self.config)

    def getLineList(self):
        """
        取得Line tokens list
        輸入：無
        回傳：list(要送的line user list)
        """
        d = self.readConfig(self.config_path)
        return d["user"]

    def setLineList(self, line_token: str, action: str):
        """
        設定Line tokens list
        輸入：line_token(單一一個), action("add" or "del")(動作，新增(add)或刪除(del))
        回傳：bool(設定成功與否)
        Comments: 要處理如果要新增的token已經存在(不要再重複寫入)或是要刪除的token不存在(不要動作並回傳錯誤)等 / 
        讓controller的addLineList跟delLineList call的
        """
        if line_token == "":
            return -1
        d = self.readConfig(self.config_path)
        if d["user"].count(line_token) == 0:
            if action == "add":
                d["user"].append(line_token)
            elif action == "del":
                return 0
        else:
            if action == "add":
                return 0
            elif action == "del":
                d["user"].remove(line_token)

        self.config = d
        self.writeConfig(self.config_path, self.config)
        return 1

model = Model()
d = model.readConfig(model.config_path)
