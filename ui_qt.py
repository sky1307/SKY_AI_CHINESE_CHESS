# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1189, 1024)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 932, 1024))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("data/bg.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(917, 0, 272, 1024))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("data/pure.jpg"))
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(952, 420, 151, 31))
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setMaxLength(4)
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(952, 40, 250, 320))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_3.setFont(font)
        self.label_3.setTextFormat(QtCore.Qt.PlainText)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(952, 330, 251, 81))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_4.setFont(font)
        self.label_4.setTextFormat(QtCore.Qt.PlainText)
        self.label_4.setWordWrap(False)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(982, 600, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_end = QtWidgets.QLabel(self.centralwidget)
        self.label_end.setGeometry(QtCore.QRect(952, 500, 141, 91))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(20)
        self.label_end.setFont(font)
        self.label_end.setAlignment(QtCore.Qt.AlignCenter)
        self.label_end.setObjectName("label_end")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "sky ai chinese chess"))
        self.label_3.setText(_translate("MainWindow", "Định dạng di động: xyx \'y \'\n "
"xy là tọa độ trước khi di chuyển \n"
"x là số dòng (0 bị bỏ qua) \n"
"y là số cột (bị bỏ qua khi xy bằng 0) \n"
"x\'y\' là tọa độ sau khi di chuyển \n"
"x\'là 0 và không thể bị bỏ qua \n"
"Chẳng hạn như 9484,122,10 \n"
"Vui lòng đợi máy tính di chuyển sau khi nhập \n"
"Nếu dữ liệu sai, quân cờ sẽ không di chuyển, \n"
"Vui lòng nhập lại \n"))
        self.label_4.setText(_translate("MainWindow", "--------------\n" "Lượt của bạn\n" "bước tiếp theo"))
        self.pushButton.setText(_translate("MainWindow", "di chuyen"))
        self.label_end.setText(_translate("MainWindow", "ing"))


