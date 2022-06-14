# https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001
# reference: https://ithelp.ithome.com.tw/articles/10276375

# from types import NoneType
import requests, json

#import numpy as np
#import pandas as pd
#import matplotlib.pyplot as plt
# from bs4 import BeautifulSoup

'''
可以 request 到的數據:

elementName: PoP12h
description: 12小時降雨機率 v

elementName: T
description: 平均溫度 v

elementName: RH
description: 平均相對濕度 v

elementName: MinCI
description: 最小舒適度指數 v

elementName: WS
description: 最大風速 v

elementName: MaxAT
description: 最高體感溫度 v

elementName: Wx
description: 天氣現象 v

elementName: MaxCI
description: 最大舒適度指數 v

elementName: MinT
description: 最低溫度 V

elementName: UVI
description: 紫外線指數 V

elementName: WeatherDescription
description: 天氣預報綜合描述

elementName: MinAT
description: 最低體感溫度 V

elementName: MaxT
description: 最高溫度 V

elementName: WD
description: 風向

elementName: Td
description: 平均露點溫度
'''

city_url = {
    "宜蘭縣": "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-003",
    "桃園市": "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-007",
    "新竹縣": "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-011",
    "苗栗縣": "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-015",
    "彰化縣": "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-019",
    "南投縣": "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-023",
    "雲林縣": "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-027",
    "嘉義縣": "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-031",
    "屏東縣": "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-035",
    "臺東縣": "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-039",
    "花蓮縣": "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-043",
    "澎湖縣": "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-047",
    "基隆市": "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-051",
    "新竹市": "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-055",
    "嘉義市": "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-059",
    "臺北市": "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-063",
    "高雄市": "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-067",
    "新北市": "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-071",
    "臺中市": "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-075",
    "臺南市": "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-079",
    "連江縣": "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-083",
    "金門縣": "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-087",
    "各縣市": "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-091"
}   

def print_data(data, prefix=""):
    if type(data) == list:
        print()
        for i in range(len(data)):
            print("%s%d:" %(prefix, i), end='')
            print_data(data[i], prefix+"  ")
    elif type(data) == dict:
        print()
        for i in data:
            print("%s%s:" %(prefix, i), end='')
            print_data(data[i], prefix+"  ")
    else:
        print(" %s" %(data))

# 獲得天氣預報(縣市或鄉鎮)，若成功獲取，則回傳值為dict，否則為NoneType
def get_weather_data(city:str, town:str=""):
    # 若沒有輸入城市，則回傳NoneType
    if city == "":
        return None

    locationName = "未設定"
    if town == "":  # 鄉鎮市區為空字串，查該城市天氣
        url = city_url["各縣市"]
        locationName = city
    else:           # 查該鄉鎮市區天氣
        url = city_url[city]
        locationName = town

    params = {
        "Authorization": "CWB-ED69F510-91B5-451B-A152-9068A4E5062A",
        "format": "JSON",
        "locationName": locationName,
        # 下面為我覺得可能只會用到的資料，要只抓這些的話把下面uncomment
        #"elementName": ["MinCI", "MaxAT", "MaxCI", "MinT", "UVI", "MinAT", "MaxT", "WS", "PoP12h", "T", "RH", "Wx"],
        "sort": "time",
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = json.loads(response.text)

        if len(data["records"]["locations"]) == 0:
            print('Error: 縣/市不存在')
            return None
        if len(data["records"]["locations"][0]["location"]) == 0:
            print('Error: 鄉鎮市/區不存在')
            return None
        
        weather_data = data["records"]["locations"][0]["location"][0]["weatherElement"]
        
        if __name__ == "__main__":
            print_data(weather_data)

        return weather_data
    else:
        return None

if __name__ == "__main__":
    # get_data()
    # city = input("輸入城市名 （台需改為臺）：")
    # town = input("輸入鄉鎮市區名：")
    ret = get_weather_data('臺北市', '大安森林公園')
    print(type(ret))
