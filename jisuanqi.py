# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jisuanqi.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget

class Jisuanqi(QtWidgets.QTabWidget):
    def __init__(self):
        super(Jisuanqi,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
    def setupUi(self, jisuanqi):
        jisuanqi.setObjectName("jisuanqi")
        jisuanqi.resize(358, 342)
        jisuanqi.setFixedWidth(300)
        jisuanqi.setFixedHeight(300)
        # let the window center
        screen = QDesktopWidget().screenGeometry()
        jsq_size = self.geometry()
        jisuanqi.move(int((screen.width() - jsq_size.width()) / 2) , int((screen.height() - jsq_size.height()) / 2))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(jisuanqi.sizePolicy().hasHeightForWidth())
        jisuanqi.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(jisuanqi)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(jisuanqi)
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.grabKeyboard() 
        self.gridLayout_2.addWidget(self.lineEdit, 1, 0, 1, 4)
        self.pushButton_4 = QtWidgets.QPushButton(jisuanqi)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_2.addWidget(self.pushButton_4, 3, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(jisuanqi)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 4, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(jisuanqi)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_2.addWidget(self.pushButton_6, 3, 3, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(jisuanqi)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 3, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(jisuanqi)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_2.addWidget(self.pushButton_5, 3, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(jisuanqi)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 2, 0, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(jisuanqi)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_2.addWidget(self.pushButton_7, 2, 1, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(jisuanqi)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_2.addWidget(self.pushButton_8, 2, 2, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(jisuanqi)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_2.addWidget(self.pushButton_9, 2, 3, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(jisuanqi)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_2.addWidget(self.pushButton_10, 4, 1, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(jisuanqi)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout_2.addWidget(self.pushButton_12, 4, 3, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(jisuanqi)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout_2.addWidget(self.pushButton_11, 4, 2, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(jisuanqi)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout_2.addWidget(self.pushButton_13, 5, 0, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(jisuanqi)
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout_2.addWidget(self.pushButton_14, 5, 1, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(jisuanqi)
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout_2.addWidget(self.pushButton_15, 5, 2, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(jisuanqi)
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout_2.addWidget(self.pushButton_16, 5, 3, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(jisuanqi)
        self.textEdit.setEnabled(False)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_2.addWidget(self.textEdit, 0, 0, 1, 4)
        self.verticalLayout.addLayout(self.gridLayout_2)
        # mycode
        self.ji = '' # 多行文本框赋值用

        self.retranslateUi(jisuanqi)
        QtCore.QMetaObject.connectSlotsByName(jisuanqi)

        self.pushButton_13.clicked.connect(self.num0)
        self.pushButton.clicked.connect(self.num1)
        self.pushButton_7.clicked.connect(self.num2)
        self.pushButton_8.clicked.connect(self.num3)
        self.pushButton_3.clicked.connect(self.num4)
        self.pushButton_4.clicked.connect(self.num5)
        self.pushButton_5.clicked.connect(self.num6)
        self.pushButton_2.clicked.connect(self.num7)
        self.pushButton_10.clicked.connect(self.num8)
        self.pushButton_11.clicked.connect(self.num9)
        self.pushButton_14.clicked.connect(self.numdian)
        self.pushButton_6.clicked.connect(self.numjia)
        self.pushButton_9.clicked.connect(self.numjian)
        self.pushButton_12.clicked.connect(self.numcheng)
        self.pushButton_16.clicked.connect(self.numchu)
        self.pushButton_15.clicked.connect(self.numdengyu)
        self.lineEdit.returnPressed.connect(self.numdengyu)

    def num0(self):
        self.lineEdit.setText(self.lineEdit.text() + '0')
    def num1(self):
        self.lineEdit.setText(self.lineEdit.text() + '1')
    def num2(self):
        self.lineEdit.setText(self.lineEdit.text() + '2')
    def num3(self):
        self.lineEdit.setText(self.lineEdit.text() + '3')
    def num4(self):
        self.lineEdit.setText(self.lineEdit.text() + '4')
    def num5(self):
        self.lineEdit.setText(self.lineEdit.text() + '5')
    def num6(self):
        self.lineEdit.setText(self.lineEdit.text() + '6')
    def num7(self):
        self.lineEdit.setText(self.lineEdit.text() + '7')
    def num8(self):
        self.lineEdit.setText(self.lineEdit.text() + '8')
    def num9(self):
        self.lineEdit.setText(self.lineEdit.text() + '9')
    def numcheng(self):
        self.lineEdit.setText(self.lineEdit.text() + '×')
    def numchu(self):
        self.lineEdit.setText(self.lineEdit.text() + '/')
    def numdian(self):
        self.lineEdit.setText(self.lineEdit.text() + '.')
    def numjia(self):
        self.lineEdit.setText(self.lineEdit.text() + '+')
    def numjian(self):
        self.lineEdit.setText(self.lineEdit.text() + '-')
    def numdengyu(self):
        try:
            tt = self.lineEdit.text()
            num = eval(tt.replace('×','*'))
            self.lineEdit.setText(str(num))
            self.ji += tt + '=' +str(num) + '\n'
            self.textEdit.setText(self.ji)
        except:
            self.lineEdit.setText('输入有误，请重新输入')

    def retranslateUi(self, jisuanqi):
        _translate = QtCore.QCoreApplication.translate
        jisuanqi.setWindowTitle(_translate("jisuanqi", "计算器"))
        self.pushButton_4.setText(_translate("jisuanqi", "5"))
        self.pushButton_2.setText(_translate("jisuanqi", "7"))
        self.pushButton_6.setText(_translate("jisuanqi", "+"))
        self.pushButton_3.setText(_translate("jisuanqi", "4"))
        self.pushButton_5.setText(_translate("jisuanqi", "6"))
        self.pushButton.setText(_translate("jisuanqi", "1"))
        self.pushButton_7.setText(_translate("jisuanqi", "2"))
        self.pushButton_8.setText(_translate("jisuanqi", "3"))
        self.pushButton_9.setText(_translate("jisuanqi", "-"))
        self.pushButton_10.setText(_translate("jisuanqi", "8"))
        self.pushButton_12.setText(_translate("jisuanqi", "×"))
        self.pushButton_11.setText(_translate("jisuanqi", "9"))
        self.pushButton_13.setText(_translate("jisuanqi", "0"))
        self.pushButton_14.setText(_translate("jisuanqi", "."))
        self.pushButton_15.setText(_translate("jisuanqi", "="))
        self.pushButton_16.setText(_translate("jisuanqi", "/"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Mainwindow = QtWidgets.QWidget()
    ui = Jisuanqi()
    ui.setupUi(Mainwindow)
    Mainwindow.show()
    sys.exit(app.exec_())

