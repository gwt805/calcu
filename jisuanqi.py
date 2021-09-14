# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jisuanqi.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtGui import QIcon

class Jisuanqi(QtWidgets.QWidget):
    def __init__(self):
        super(Jisuanqi,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
    def setupUi(self, jisuanqi):
        jisuanqi.setObjectName("jisuanqi")
        jisuanqi.resize(358, 372)
        # fix window size
        jisuanqi.setFixedWidth(300)
        jisuanqi.setFixedHeight(300)
        jisuanqi.setWindowIcon(QIcon('img/jsq.png'))
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
        self.gridLayout_2.setHorizontalSpacing(3)
        self.gridLayout_2.setVerticalSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
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
        self.pushButton_17 = QtWidgets.QPushButton(jisuanqi)
        self.pushButton_17.setObjectName("pushButton_17")
        self.gridLayout_2.addWidget(self.pushButton_17, 2, 4, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(jisuanqi)
        self.textEdit.setEnabled(False)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_2.addWidget(self.textEdit, 0, 0, 1, 5)
        self.lineEdit = QtWidgets.QLineEdit(jisuanqi)
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setFocus()
        self.gridLayout_2.addWidget(self.lineEdit, 1, 0, 1, 5)
        self.pushButton_18 = QtWidgets.QPushButton(jisuanqi)
        self.pushButton_18.setObjectName("pushButton_18")
        self.gridLayout_2.addWidget(self.pushButton_18, 3, 4, 1, 1)
        self.pushButton_19 = QtWidgets.QPushButton(jisuanqi)
        self.pushButton_19.setObjectName("pushButton_19")
        self.gridLayout_2.addWidget(self.pushButton_19, 4, 4, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(jisuanqi)
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout_2.addWidget(self.pushButton_16, 5, 4, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(jisuanqi)
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout_2.addWidget(self.pushButton_15, 5, 2, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout_2)

        self.retranslateUi(jisuanqi)
        QtCore.QMetaObject.connectSlotsByName(jisuanqi)
        # mycode
        self.ji = '' # 多行文本框赋值用
        self.pushButton_13.clicked.connect(lambda:self.numss('0'))
        self.pushButton.clicked.connect(lambda:self.numss('1'))
        self.pushButton_7.clicked.connect(lambda:self.numss('2'))
        self.pushButton_8.clicked.connect(lambda:self.numss('3'))
        self.pushButton_3.clicked.connect(lambda:self.numss('4'))
        self.pushButton_4.clicked.connect(lambda:self.numss('5'))
        self.pushButton_5.clicked.connect(lambda:self.numss('6'))
        self.pushButton_2.clicked.connect(lambda:self.numss('7'))
        self.pushButton_10.clicked.connect(lambda:self.numss('8'))
        self.pushButton_11.clicked.connect(lambda:self.numss('9'))
        self.pushButton_14.clicked.connect(lambda:self.numss('.'))
        self.pushButton_6.clicked.connect(lambda:self.numss('+'))
        self.pushButton_9.clicked.connect(lambda:self.numss('-'))
        self.pushButton_12.clicked.connect(lambda:self.numss('*'))
        self.pushButton_16.clicked.connect(lambda:self.numss('/'))
        self.pushButton_17.clicked.connect(lambda:self.numss('('))
        self.pushButton_18.clicked.connect(lambda:self.numss(')'))
        self.pushButton_19.clicked.connect(lambda:self.numss('C'))
        self.pushButton_19.setShortcut('escape')
        self.pushButton_15.clicked.connect(lambda:self.numss('='))
        self.lineEdit.returnPressed.connect(lambda:self.numss('='))

    def numss(self,nnum):
        if nnum == 'C':
            self.lineEdit.clear()
            self.textEdit.clear()
        elif nnum == '=':
            try:
                tt = self.lineEdit.text()
                num = eval(tt.replace('×','*'))
                self.lineEdit.setText(str(num))
                self.ji += tt + '=' +str(num) + '\n'
                self.textEdit.setText(self.ji)
            except:
                self.lineEdit.setText('输入有误，请重新输入')
        else:
            self.lineEdit.setText(self.lineEdit.text() + nnum)

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
        self.pushButton_17.setText(_translate("jisuanqi", "("))
        self.pushButton_18.setText(_translate("jisuanqi", ")"))
        self.pushButton_19.setText(_translate("jisuanqi", "C"))
        self.pushButton_16.setText(_translate("jisuanqi", "/"))
        self.pushButton_15.setText(_translate("jisuanqi", "="))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    jisuanqi = QtWidgets.QWidget()
    ui = Jisuanqi()
    ui.setupUi(jisuanqi)
    jisuanqi.show()
    sys.exit(app.exec_())

