# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\OOP2022_final_proj\ui (1).ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(930, 568)
        self.centralwidget = QtWidgets.QWidget(Form)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_line = QtWidgets.QHBoxLayout()
        self.horizontalLayout_line.setObjectName("horizontalLayout_line")
        self.label_line = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_line.setFont(font)
        self.label_line.setObjectName("label_line")
        self.horizontalLayout_line.addWidget(self.label_line)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.line_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.line_lineEdit.setFont(font)
        self.line_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.line_lineEdit.setObjectName("line_lineEdit")
        self.horizontalLayout_11.addWidget(self.line_lineEdit)
        self.line_add_pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_add_pushButton.setFont(font)
        self.line_add_pushButton.setObjectName("line_add_pushButton")
        self.horizontalLayout_11.addWidget(self.line_add_pushButton)
        self.line_del_pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_del_pushButton.setFont(font)
        self.line_del_pushButton.setObjectName("line_del_pushButton")
        self.horizontalLayout_11.addWidget(self.line_del_pushButton)
        self.line_show_pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.line_show_pushButton.setFont(font)
        self.line_show_pushButton.setObjectName("line_show_pushButton")
        self.horizontalLayout_11.addWidget(self.line_show_pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_line.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout_line, 5, 0, 1, 1)
        self.horizontalLayout_location = QtWidgets.QHBoxLayout()
        self.horizontalLayout_location.setObjectName("horizontalLayout_location")
        self.label_city = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_city.setFont(font)
        self.label_city.setAlignment(QtCore.Qt.AlignCenter)
        self.label_city.setObjectName("label_city")
        self.horizontalLayout_location.addWidget(self.label_city)
        self.city_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.city_lineEdit.setObjectName("city_lineEdit")
        self.horizontalLayout_location.addWidget(self.city_lineEdit)
        self.label_town = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_town.setFont(font)
        self.label_town.setAlignment(QtCore.Qt.AlignCenter)
        self.label_town.setObjectName("label_town")
        self.horizontalLayout_location.addWidget(self.label_town)
        self.town_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.town_lineEdit.setObjectName("town_lineEdit")
        self.horizontalLayout_location.addWidget(self.town_lineEdit)
        self.label_error_location = QtWidgets.QLabel(self.centralwidget)
        self.label_error_location.setObjectName("label_error_location")
        self.horizontalLayout_location.addWidget(self.label_error_location)
        self.gridLayout.addLayout(self.horizontalLayout_location, 1, 0, 1, 1)
        self.horizontalLayout_day = QtWidgets.QHBoxLayout()
        self.horizontalLayout_day.setObjectName("horizontalLayout_day")
        self.label_days = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_days.setFont(font)
        self.label_days.setObjectName("label_days")
        self.horizontalLayout_day.addWidget(self.label_days)
        self.mon_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.mon_checkBox.setFont(font)
        self.mon_checkBox.setObjectName("mon_checkBox")
        self.horizontalLayout_day.addWidget(self.mon_checkBox)
        self.tue_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.tue_checkBox.setObjectName("tue_checkBox")
        self.horizontalLayout_day.addWidget(self.tue_checkBox)
        self.wed_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.wed_checkBox.setObjectName("wed_checkBox")
        self.horizontalLayout_day.addWidget(self.wed_checkBox)
        self.thu_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.thu_checkBox.setObjectName("thu_checkBox")
        self.horizontalLayout_day.addWidget(self.thu_checkBox)
        self.fri_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.fri_checkBox.setObjectName("fri_checkBox")
        self.horizontalLayout_day.addWidget(self.fri_checkBox)
        self.sat_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.sat_checkBox.setObjectName("sat_checkBox")
        self.horizontalLayout_day.addWidget(self.sat_checkBox)
        self.sun_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.sun_checkBox.setObjectName("sun_checkBox")
        self.horizontalLayout_day.addWidget(self.sun_checkBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_day.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_day, 2, 0, 1, 1)
        self.horizontalLayout_button = QtWidgets.QHBoxLayout()
        self.horizontalLayout_button.setObjectName("horizontalLayout_button")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.preview_pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.preview_pushButton.setFont(font)
        self.preview_pushButton.setObjectName("preview_pushButton")
        self.horizontalLayout_12.addWidget(self.preview_pushButton)
        self.save_pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.save_pushButton.setFont(font)
        self.save_pushButton.setObjectName("save_pushButton")
        self.horizontalLayout_12.addWidget(self.save_pushButton)
        self.horizontalLayout_button.addLayout(self.horizontalLayout_12)
        self.gridLayout.addLayout(self.horizontalLayout_button, 8, 0, 1, 1)
        self.horizontalLayout_weatherPreference = QtWidgets.QHBoxLayout()
        self.horizontalLayout_weatherPreference.setObjectName("horizontalLayout_weatherPreference")
        self.label_weather = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.label_weather.setFont(font)
        self.label_weather.setObjectName("label_weather")
        self.horizontalLayout_weatherPreference.addWidget(self.label_weather)
        self.gridLayout_left = QtWidgets.QGridLayout()
        self.gridLayout_left.setObjectName("gridLayout_left")
        self.temp_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.temp_checkBox.setFont(font)
        self.temp_checkBox.setObjectName("temp_checkBox")
        self.gridLayout_left.addWidget(self.temp_checkBox, 1, 0, 1, 1)
        self.rain_max_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.rain_max_spinBox.setObjectName("rain_max_spinBox")
        self.gridLayout_left.addWidget(self.rain_max_spinBox, 0, 4, 1, 1)
        self.label_min_rain = QtWidgets.QLabel(self.centralwidget)
        self.label_min_rain.setEnabled(True)
        self.label_min_rain.setObjectName("label_min_rain")
        self.gridLayout_left.addWidget(self.label_min_rain, 0, 1, 1, 1)
        self.label_max_rain = QtWidgets.QLabel(self.centralwidget)
        self.label_max_rain.setObjectName("label_max_rain")
        self.gridLayout_left.addWidget(self.label_max_rain, 0, 3, 1, 1)
        self.label_max_temp = QtWidgets.QLabel(self.centralwidget)
        self.label_max_temp.setObjectName("label_max_temp")
        self.gridLayout_left.addWidget(self.label_max_temp, 1, 3, 1, 1)
        self.rain_min_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.rain_min_spinBox.setObjectName("rain_min_spinBox")
        self.gridLayout_left.addWidget(self.rain_min_spinBox, 0, 2, 1, 1)
        self.temp_max_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.temp_max_spinBox.setObjectName("temp_max_spinBox")
        self.gridLayout_left.addWidget(self.temp_max_spinBox, 1, 4, 1, 1)
        self.temp_min_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.temp_min_spinBox.setObjectName("temp_min_spinBox")
        self.gridLayout_left.addWidget(self.temp_min_spinBox, 1, 2, 1, 1)
        self.rain_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.rain_checkBox.setFont(font)
        self.rain_checkBox.setObjectName("rain_checkBox")
        self.gridLayout_left.addWidget(self.rain_checkBox, 0, 0, 1, 1)
        self.label_min_temp = QtWidgets.QLabel(self.centralwidget)
        self.label_min_temp.setObjectName("label_min_temp")
        self.gridLayout_left.addWidget(self.label_min_temp, 1, 1, 1, 1)
        self.horizontalLayout_weatherPreference.addLayout(self.gridLayout_left)
        self.gridLayout_right = QtWidgets.QGridLayout()
        self.gridLayout_right.setObjectName("gridLayout_right")
        self.hum_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.hum_checkBox.setFont(font)
        self.hum_checkBox.setObjectName("hum_checkBox")
        self.gridLayout_right.addWidget(self.hum_checkBox, 1, 0, 1, 1)
        self.label_max_uv = QtWidgets.QLabel(self.centralwidget)
        self.label_max_uv.setObjectName("label_max_uv")
        self.gridLayout_right.addWidget(self.label_max_uv, 0, 3, 1, 1)
        self.label_max_hum = QtWidgets.QLabel(self.centralwidget)
        self.label_max_hum.setObjectName("label_max_hum")
        self.gridLayout_right.addWidget(self.label_max_hum, 1, 3, 1, 1)
        self.uv_min_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.uv_min_spinBox.setObjectName("uv_min_spinBox")
        self.gridLayout_right.addWidget(self.uv_min_spinBox, 0, 2, 1, 1)
        self.hum_max_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.hum_max_spinBox.setObjectName("hum_max_spinBox")
        self.gridLayout_right.addWidget(self.hum_max_spinBox, 1, 4, 1, 1)
        self.uv_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.uv_checkBox.setFont(font)
        self.uv_checkBox.setObjectName("uv_checkBox")
        self.gridLayout_right.addWidget(self.uv_checkBox, 0, 0, 1, 1)
        self.uv_max_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.uv_max_spinBox.setObjectName("uv_max_spinBox")
        self.gridLayout_right.addWidget(self.uv_max_spinBox, 0, 4, 1, 1)
        self.label_min_uv = QtWidgets.QLabel(self.centralwidget)
        self.label_min_uv.setObjectName("label_min_uv")
        self.gridLayout_right.addWidget(self.label_min_uv, 0, 1, 1, 1)
        self.label_min_hum = QtWidgets.QLabel(self.centralwidget)
        self.label_min_hum.setObjectName("label_min_hum")
        self.gridLayout_right.addWidget(self.label_min_hum, 1, 1, 1, 1)
        self.hum_min_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.hum_min_spinBox.setObjectName("hum_min_spinBox")
        self.gridLayout_right.addWidget(self.hum_min_spinBox, 1, 2, 1, 1)
        self.horizontalLayout_weatherPreference.addLayout(self.gridLayout_right)
        self.label_error_value = QtWidgets.QLabel(self.centralwidget)
        self.label_error_value.setText("")
        self.label_error_value.setObjectName("label_error_value")
        self.horizontalLayout_weatherPreference.addWidget(self.label_error_value)
        self.gridLayout.addLayout(self.horizontalLayout_weatherPreference, 4, 0, 1, 1)
        self.horizontalLayout_lineResult = QtWidgets.QHBoxLayout()
        self.horizontalLayout_lineResult.setObjectName("horizontalLayout_lineResult")
        self.line_result_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.line_result_label.setFont(font)
        self.line_result_label.setAlignment(QtCore.Qt.AlignCenter)
        self.line_result_label.setObjectName("line_result_label")
        self.horizontalLayout_lineResult.addWidget(self.line_result_label)
        self.gridLayout.addLayout(self.horizontalLayout_lineResult, 6, 0, 1, 1)
        self.horizontalLayout_time = QtWidgets.QHBoxLayout()
        self.horizontalLayout_time.setObjectName("horizontalLayout_time")
        self.label_time = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.label_time.setFont(font)
        self.label_time.setAlignment(QtCore.Qt.AlignCenter)
        self.label_time.setObjectName("label_time")
        self.horizontalLayout_time.addWidget(self.label_time)
        self.time_timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.time_timeEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.time_timeEdit.setObjectName("time_timeEdit")
        self.horizontalLayout_time.addWidget(self.time_timeEdit)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_time.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_time, 3, 0, 1, 1)
        self.horizontalLayout_msg = QtWidgets.QHBoxLayout()
        self.horizontalLayout_msg.setObjectName("horizontalLayout_msg")
        self.label_msg = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_msg.setFont(font)
        self.label_msg.setObjectName("label_msg")
        self.horizontalLayout_msg.addWidget(self.label_msg)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_msgT = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.label_msgT.setFont(font)
        self.label_msgT.setAlignment(QtCore.Qt.AlignCenter)
        self.label_msgT.setObjectName("label_msgT")
        self.gridLayout_5.addWidget(self.label_msgT, 0, 0, 1, 1)
        self.msgT_pre_textEdit = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.msgT_pre_textEdit.setFont(font)
        self.msgT_pre_textEdit.setObjectName("msgT_pre_textEdit")
        self.gridLayout_5.addWidget(self.msgT_pre_textEdit, 0, 3, 1, 1)
        self.msgT_post_textEdit = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.msgT_post_textEdit.setFont(font)
        self.msgT_post_textEdit.setObjectName("msgT_post_textEdit")
        self.gridLayout_5.addWidget(self.msgT_post_textEdit, 0, 5, 1, 1)
        self.label_msgF = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.label_msgF.setFont(font)
        self.label_msgF.setAlignment(QtCore.Qt.AlignCenter)
        self.label_msgF.setObjectName("label_msgF")
        self.gridLayout_5.addWidget(self.label_msgF, 1, 0, 1, 1)
        self.label_msgT_post = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_msgT_post.setFont(font)
        self.label_msgT_post.setObjectName("label_msgT_post")
        self.gridLayout_5.addWidget(self.label_msgT_post, 0, 4, 1, 1)
        self.label_msgF_post = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_msgF_post.setFont(font)
        self.label_msgF_post.setObjectName("label_msgF_post")
        self.gridLayout_5.addWidget(self.label_msgF_post, 1, 4, 1, 1)
        self.msgF_post_textEdit = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.msgF_post_textEdit.setFont(font)
        self.msgF_post_textEdit.setObjectName("msgF_post_textEdit")
        self.gridLayout_5.addWidget(self.msgF_post_textEdit, 1, 5, 1, 1)
        self.msgF_pre_textEdit = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.msgF_pre_textEdit.setFont(font)
        self.msgF_pre_textEdit.setObjectName("msgF_pre_textEdit")
        self.gridLayout_5.addWidget(self.msgF_pre_textEdit, 1, 3, 1, 1)
        self.label_msgT_pre = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_msgT_pre.setFont(font)
        self.label_msgT_pre.setObjectName("label_msgT_pre")
        self.gridLayout_5.addWidget(self.label_msgT_pre, 0, 1, 1, 1)
        self.label_msgF_pre = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_msgF_pre.setFont(font)
        self.label_msgF_pre.setObjectName("label_msgF_pre")
        self.gridLayout_5.addWidget(self.label_msgF_pre, 1, 1, 1, 1)
        self.horizontalLayout_msg.addLayout(self.gridLayout_5)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_msg.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout_msg, 7, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_setting = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(24)
        self.label_setting.setFont(font)
        self.label_setting.setObjectName("label_setting")
        self.horizontalLayout_7.addWidget(self.label_setting)
        self.gridLayout.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        Form.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Form)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 930, 25))
        self.menubar.setObjectName("menubar")
        Form.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Form)
        self.statusbar.setObjectName("statusbar")
        Form.setStatusBar(self.statusbar)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "天氣分析鬼才機器人 設定介面"))
        self.label_line.setText(_translate("Form", "Line分享設定："))
        self.line_add_pushButton.setText(_translate("Form", "新增"))
        self.line_del_pushButton.setText(_translate("Form", "刪除"))
        self.line_show_pushButton.setText(_translate("Form", "顯示所有"))
        self.label_city.setText(_translate("Form", "縣/市："))
        self.label_town.setText(_translate("Form", "鄉鎮市/區："))
        self.label_error_location.setText(_translate("Form", "                                           "))
        self.label_days.setText(_translate("Form", "通知發送日期："))
        self.mon_checkBox.setText(_translate("Form", "週一"))
        self.tue_checkBox.setText(_translate("Form", "週二"))
        self.wed_checkBox.setText(_translate("Form", "週三"))
        self.thu_checkBox.setText(_translate("Form", "週四"))
        self.fri_checkBox.setText(_translate("Form", "週五"))
        self.sat_checkBox.setText(_translate("Form", "週六"))
        self.sun_checkBox.setText(_translate("Form", "週日"))
        self.preview_pushButton.setText(_translate("Form", "儲存並預覽通知訊息"))
        self.save_pushButton.setText(_translate("Form", "儲存設定"))
        self.label_weather.setText(_translate("Form", "天氣偏好："))
        self.temp_checkBox.setText(_translate("Form", "氣溫(°C)"))
        self.label_min_rain.setText(_translate("Form", "最小值"))
        self.label_max_rain.setText(_translate("Form", "最大值"))
        self.label_max_temp.setText(_translate("Form", "最大值"))
        self.rain_checkBox.setText(_translate("Form", "降雨機率(%)"))
        self.label_min_temp.setText(_translate("Form", "最小值"))
        self.hum_checkBox.setText(_translate("Form", "濕度(%)"))
        self.label_max_uv.setText(_translate("Form", "最大值"))
        self.label_max_hum.setText(_translate("Form", "最大值"))
        self.uv_checkBox.setText(_translate("Form", "紫外線指數"))
        self.label_min_uv.setText(_translate("Form", "最小值"))
        self.label_min_hum.setText(_translate("Form", "最小值"))
        self.line_result_label.setText(_translate("Form", "(Current Line Output)"))
        self.label_time.setText(_translate("Form", "通知發送時間："))
        self.label_msg.setText(_translate("Form", "通知訊息內容："))
        self.label_msgT.setText(_translate("Form", "符合條件時"))
        self.label_msgF.setText(_translate("Form", "不符合條件時"))
        self.label_msgT_post.setText(_translate("Form", "後置訊息："))
        self.label_msgF_post.setText(_translate("Form", "後置訊息："))
        self.label_msgT_pre.setText(_translate("Form", "前置訊息："))
        self.label_msgF_pre.setText(_translate("Form", "前置訊息："))
        self.label_setting.setText(_translate("Form", "設定"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
