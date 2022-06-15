import Control
import requests
from PIL import Image, ImageDraw, ImageFont

class line():
    def __init__(self):
        self.Srcimg  = Image.open('./chinesenewyear.png')
        self.Drawimg = ImageDraw.Draw(self.Srcimg)
        self.width , self.height = self.Srcimg.size
        self.controller = Control.Controller()

    def sendMessage(self):
        Line_tokens_list = self.controller.getLineList()
        """
        使用controller.getMessage()取得訊息，並發送通知給Line tokens list的每個使用者
        輸入：無
        回傳：無
        """
        if Line_tokens_list:
            for token in Line_tokens_list:
                url = "https://notify-api.line.me/api/notify"
                headers = {
                            "Authorization": "Bearer " + token,
                            #"Content-Type" : "application/x-www-form-urlencoded"
                }
                msg = self.controller.getMessage()
                '''
                print(msg)
                print(type(msg))
                #第一行字
                Myfont  = ImageFont.truetype('NotoSansTC-Black.otf', 30)
                (x, y) = (self.width/2/2, self.height/2)
                color  = 'rgb(253, 191, 98)'
                Mytext = '今日' + msg[0].split("。")[0] + '\n' + msg[2] #今日多雲短暫陣雨或雷雨  
                #controller傳過來的為 "多雲短暫陣雨或雷雨。降雨機率 30%。溫度攝氏24至28度。舒適至悶熱。西南風 風速2級(每秒2公尺)。相對濕度92%。"
                #變成"今日多雲短暫陣雨或雷雨"
                Myfont  = ImageFont.truetype('NotoSansTC-Black.otf', 100)
                self.Drawimg.text((x, y), Mytext, fill=color,anchor="ms", font=Myfont,align = 'center')
                Myfont  = ImageFont.truetype('NotoSansTC-Black.otf', 30)
                                
                #第二行字
                (x, y) = (self.width/2-210, self.height/2+200) # Text position
                color  = 'rgb(253, 191, 98)' # Text color
                Mytext = '天氣分析鬼才機器人 貼心提醒'
                self.Drawimg.text((x, y), Mytext, fill=color, font=Myfont,align = 'center')
                #文字訊息為msg[1]
                payload = {'message':  msg[1]}
                self.Srcimg.save('WeatherCard.png')
                picURI = "./WeatherCard.png"
                '''
                #payload = {'message':  msg}
                #picURI={}
                #第一行字
                Myfont  = ImageFont.truetype('NotoSansTC-Black.otf', 30)
                (x, y) = (self.width/2, self.height/2)
                color  = 'rgb(253, 191, 98)'
                Mytext = msg.split("\n")[6]
                Myfont  = ImageFont.truetype('NotoSansTC-Black.otf', 150)
                self.Drawimg.text((x, y), Mytext, fill=color,anchor="ms", font=Myfont,align = 'center')
                
                Myfont  = ImageFont.truetype('NotoSansTC-Black.otf', 40)
                (x, y) = (self.width/2-300, self.height/2+200) # Text position
                color  = 'rgb(253, 191, 98)' # Text color
                Mytext = '天氣分析鬼才機器人 貼心提醒'
                self.Drawimg.text((x, y), Mytext, fill=color, font=Myfont,align = 'center')
                #文字訊息為msg[1]
                payload = {'message':  msg}
                self.Srcimg.save('WeatherCard.png')
                picURI = "./WeatherCard.png"
                
                
                
                self.Srcimg.save('WeatherCard.png')
                picURI = "./WeatherCard.png"
                
                
                if picURI:
                    files = {'imageFile': open(picURI, 'rb')}
                    r = requests.post(url, headers=headers, params=payload, files=files)
                else:
                    r = requests.post(url, headers = headers, params = payload)
                return r.status_code


if __name__ == '__main__':
    line = line()
    line.sendMessage()
    

    