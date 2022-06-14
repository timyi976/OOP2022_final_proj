from Control import Controller

class line():
    def __init__(self):
        """
        初始化
        """
        self.controller = Controller()

    def sendMessage(self):
        """
        使用controller.getMessage()取得訊息，並發送通知給Line tokens list的每個使用者
        輸入：無
        回傳：無
        """
        pass

if __name__ == '__main__':
    line = line()
    line.sendMessage()