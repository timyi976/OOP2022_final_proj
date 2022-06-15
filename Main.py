from View import view
from Control import Controller
from Model import model

"""
為了定時通知功能 以下module用於提權 限windows管理員帳戶使用
需要有pywin32模組 安裝: pip install pywin32
"""
import os
import sys
import win32com.shell.shell as shell

class app():
    def __init__(self):
        self.controller = Controller()
        self.view = view()
        self.view.set_controller(self.controller)

if __name__ == '__main__':
    
    ASADMIN = 'asadmin'
    if sys.argv[-1] != ASADMIN:
        script = os.path.abspath(sys.argv[0])
        params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
        shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)

    app = app()
    app.view.start_ui()