# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1153, 782)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(170, 110, 221, 481))
        font = QtGui.QFont()
        font.setFamily("方正舒体")
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(92, 126, 168);\n"
"\n"
"\n"
"\n"
"border-top-left-radius:15px;\n"
"border-bottom-left-radius:15px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(MainWindow)
        self.label_2.setGeometry(QtCore.QRect(390, 110, 651, 481))
        self.label_2.setStyleSheet("border-image: url(:/img/res/img/1107810.jpg);\n"
"border-top-right-radius:15px;\n"
"border-bottom-right-radius:15px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(MainWindow)
        self.label_3.setGeometry(QtCore.QRect(390, 110, 651, 481))
        self.label_3.setStyleSheet("background-color: rgba(0, 0, 0,80);\n"
"border-top-right-radius:15px;\n"
"border-bottom-right-radius:15px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(MainWindow)
        self.label_4.setGeometry(QtCore.QRect(230, 180, 111, 61))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("")
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(MainWindow)
        self.lineEdit.setGeometry(QtCore.QRect(200, 280, 161, 51))
        self.lineEdit.setStyleSheet("border:none;\n"
"border-bottom:2px solid rgba(0,0,0,100);\n"
"background-color: rgba(0, 0, 0,0);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(MainWindow)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 350, 161, 51))
        self.lineEdit_2.setStyleSheet("border:none;\n"
"border-bottom:2px solid rgba(0,0,0,100);\n"
"background-color: rgba(0, 0, 0,0);")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.login_button = QtWidgets.QPushButton(MainWindow)
        self.login_button.setGeometry(QtCore.QRect(220, 450, 131, 41))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.login_button.setFont(font)
        self.login_button.setStyleSheet("QPushButton{    \n"
"    background-color: rgb(180,160,160);\n"
"    \n"
"    color: rgb(248,250,255);\n"
"border-radius:20px;\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"    \n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"}\n"
"QPushButton:hover{\n"
" background-color:  rgb(200,160,160)\n"
"}\n"
"")
        self.login_button.setObjectName("login_button")
        self.label_5 = QtWidgets.QLabel(MainWindow)
        self.label_5.setGeometry(QtCore.QRect(600, 200, 281, 141))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 210);")
        self.label_5.setObjectName("label_5")
        self.frame = QtWidgets.QFrame(MainWindow)
        self.frame.setGeometry(QtCore.QRect(950, 120, 79, 44))
        self.frame.setStyleSheet("QPushButton{\n"
"border:none;\n"
"}\n"
"QPushButton:hover{\n"
" padding-bottom:5px;\n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.min_button = QtWidgets.QPushButton(self.frame)
        self.min_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/res/icon/最小化.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.min_button.setIcon(icon)
        self.min_button.setObjectName("min_button")
        self.horizontalLayout.addWidget(self.min_button)
        self.max_button = QtWidgets.QPushButton(self.frame)
        self.max_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/res/icon/关闭.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.max_button.setIcon(icon1)
        self.max_button.setObjectName("max_button")
        self.horizontalLayout.addWidget(self.max_button)
        self.signin_button = QtWidgets.QPushButton(MainWindow)
        self.signin_button.setGeometry(QtCore.QRect(240, 500, 93, 28))
        self.signin_button.setStyleSheet("QPushButton{\n"
"border:none;\n"
"    color: rgb(0,0,0);\n"
"}\n"
"QPushButton:hover{\n"
"\n"
" color:  rgb(255, 255, 255)\n"
"}\n"
"")
        self.signin_button.setObjectName("signin_button")

        self.retranslateUi(MainWindow)
        self.max_button.clicked.connect(MainWindow.close) # type: ignore
        self.min_button.clicked.connect(MainWindow.showMinimized) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Form"))
        self.label_4.setText(_translate("MainWindow", "欢迎登录"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "账号："))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "密码："))
        self.login_button.setText(_translate("MainWindow", "登录"))
        self.label_5.setText(_translate("MainWindow", "“ 如果你是月亮\n"
"   能不能够陪伴\n"
"   独守着\n"
"   想念你的海岸”"))
        self.signin_button.setText(_translate("MainWindow", "注册账号"))
import resource_rc
