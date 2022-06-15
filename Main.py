from View import view
from Control import Controller
from Model import model

import os
import sys
import platform

class app():
    def __init__(self):
        self.controller = Controller()
        self.view = view()
        self.view.set_controller(self.controller)

if __name__ == '__main__':
    if platform.system().lower() == 'windows':
        """
        windows需要有pywin32模組 安裝: pip install pywin32
        """
        import win32com.shell.shell as shell
        ASADMIN = 'asadmin'
        if sys.argv[-1] != ASADMIN:
            script = os.path.abspath(sys.argv[0])
            params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
            shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)

    app = app()
    app.view.start_ui()
