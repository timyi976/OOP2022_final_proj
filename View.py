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
        d["time"] = self.time_timeEdit.dateTime().toString("HHMM")

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

        self.popup.showMessage("設定儲存成功！","設定成功通知")

        print(d)

    def preview_button(self):
        self.save_button()
        self.popup.showMessage(self.controller.getMessage(),"通知訊息預覽")

    def delay_exec(self, delay, func):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(func)
        self.timer.start(delay)

    def hide_line_message(self):
        if self.line_show_state == True:
            self.line_result_label.setText("")
        self.line_result_label.setStyleSheet("color: black")

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


if __name__ == '__main__':
    controller = Controller()
    view = view()
    view.set_controller(controller)
    view.start_ui()