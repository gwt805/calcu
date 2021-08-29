# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class jisuanqi(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(358, 340)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(MainWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textEdit = QtWidgets.QTextEdit(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMouseTracking(True)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_2.addWidget(self.textEdit, 0, 0, 1, 4)
        self.pushButton_4 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_2.addWidget(self.pushButton_4, 2, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 3, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_2.addWidget(self.pushButton_6, 2, 3, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 2, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_2.addWidget(self.pushButton_5, 2, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(MainWindow)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 1, 0, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_2.addWidget(self.pushButton_7, 1, 1, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_2.addWidget(self.pushButton_8, 1, 2, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_2.addWidget(self.pushButton_9, 1, 3, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_2.addWidget(self.pushButton_10, 3, 1, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout_2.addWidget(self.pushButton_12, 3, 3, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout_2.addWidget(self.pushButton_11, 3, 2, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout_2.addWidget(self.pushButton_13, 4, 0, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout_2.addWidget(self.pushButton_14, 4, 1, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout_2.addWidget(self.pushButton_15, 4, 2, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout_2.addWidget(self.pushButton_16, 4, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

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
    def num0(self):
        self.textEdit.setText(self.textEdit.toPlainText() + '0')
    def num1(self):
        self.textEdit.setText(self.textEdit.toPlainText() + '1')
    def num2(self):
        self.textEdit.setText(self.textEdit.toPlainText() + '2')
    def num3(self):
        self.textEdit.setText(self.textEdit.toPlainText() + '3')
    def num4(self):
        self.textEdit.setText(self.textEdit.toPlainText() + '4')
    def num5(self):
        self.textEdit.setText(self.textEdit.toPlainText() + '5')
    def num6(self):
        self.textEdit.setText(self.textEdit.toPlainText() + '6')
    def num7(self):
        self.textEdit.setText(self.textEdit.toPlainText() + '7')
    def num8(self):
        self.textEdit.setText(self.textEdit.toPlainText() + '8')
    def num9(self):
        self.textEdit.setText(self.textEdit.toPlainText() + '9')
    def numcheng(self):
        self.textEdit.setText(self.textEdit.toPlainText() + '×')
    def numchu(self):
        self.textEdit.setText(self.textEdit.toPlainText() + '/')
    def numdian(self):
        self.textEdit.setText(self.textEdit.toPlainText() + '.')
    def numjia(self):
        self.textEdit.setText(self.textEdit.toPlainText() + '+')
    def numjian(self):
        self.textEdit.setText(self.textEdit.toPlainText() + '-')
    def numdengyu(self):
        try:
            self.textEdit.setText(str(eval(self.textEdit.toPlainText().replace('×','*'))))
        except:
            self.textEdit.setText('输入有误，请重新输入')
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "计算器"))
        self.pushButton_4.setText(_translate("MainWindow", "5"))
        self.pushButton_2.setText(_translate("MainWindow", "7"))
        self.pushButton_6.setText(_translate("MainWindow", "+"))
        self.pushButton_3.setText(_translate("MainWindow", "4"))
        self.pushButton_5.setText(_translate("MainWindow", "6"))
        self.pushButton.setText(_translate("MainWindow", "1"))
        self.pushButton_7.setText(_translate("MainWindow", "2"))
        self.pushButton_8.setText(_translate("MainWindow", "3"))
        self.pushButton_9.setText(_translate("MainWindow", "-"))
        self.pushButton_10.setText(_translate("MainWindow", "8"))
        self.pushButton_12.setText(_translate("MainWindow", "×"))
        self.pushButton_11.setText(_translate("MainWindow", "9"))
        self.pushButton_13.setText(_translate("MainWindow", "0"))
        self.pushButton_14.setText(_translate("MainWindow", "."))
        self.pushButton_15.setText(_translate("MainWindow", "="))
        self.pushButton_16.setText(_translate("MainWindow", "/"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = jisuanqi()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

