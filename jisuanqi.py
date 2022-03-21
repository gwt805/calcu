# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import (
    QWidget,
    QApplication,
    QSizePolicy,
    QVBoxLayout,
    QGridLayout,
    QLayout,
    QPushButton,
    QTextBrowser,
    QLineEdit,
    QSystemTrayIcon,
    QMenu,
    QAction,
    QMessageBox
)
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore
import img

class Jsq(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(358, 372)
        # fix window size
        self.setFixedWidth(300)
        self.setFixedHeight(300)
        self.setWindowIcon(QIcon(':img/jsq_logo.svg'))
        self.setWindowTitle('计算器')
        # let the window center
        screen = QDesktopWidget().screenGeometry()
        window_size = self.geometry()
        self.move(int((screen.width() - window_size.width()) / 2) , int((screen.height() - window_size.height()) / 2))

        # sys tray
        self.tray = QSystemTrayIcon()
        self.tray.setIcon(QIcon(':img/jsq_logo.svg'))
        showAction = QAction("&Show", self, triggered = self.Show)
        quitAction = QAction("&Quit", self, triggered = self.close)
        self.trayMenu = QMenu(self)
        self.trayMenu.addAction(showAction)
        self.trayMenu.addSeparator()
        self.trayMenu.addAction(quitAction)
        self.tray.setContextMenu(self.trayMenu)
        self.tray.show()

        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_2.setHorizontalSpacing(3)
        self.gridLayout_2.setVerticalSpacing(6)
        self.pushButton_4 = QPushButton('5',self)
        self.gridLayout_2.addWidget(self.pushButton_4, 3, 1, 1, 1)
        self.pushButton_2 = QPushButton('7',self)
        self.gridLayout_2.addWidget(self.pushButton_2, 4, 0, 1, 1)
        self.pushButton_6 = QPushButton("+",self)
        self.gridLayout_2.addWidget(self.pushButton_6, 3, 3, 1, 1)
        self.pushButton_3 = QPushButton("4",self)
        self.gridLayout_2.addWidget(self.pushButton_3, 3, 0, 1, 1)
        self.pushButton_5 = QPushButton("6",self)
        self.gridLayout_2.addWidget(self.pushButton_5, 3, 2, 1, 1)
        self.pushButton = QPushButton("1",self)
        self.gridLayout_2.addWidget(self.pushButton, 2, 0, 1, 1)
        self.pushButton_7 = QPushButton("2",self)
        self.gridLayout_2.addWidget(self.pushButton_7, 2, 1, 1, 1)
        self.pushButton_8 = QPushButton("3",self)
        self.gridLayout_2.addWidget(self.pushButton_8, 2, 2, 1, 1)
        self.pushButton_9 = QPushButton("-",self)
        self.gridLayout_2.addWidget(self.pushButton_9, 2, 3, 1, 1)
        self.pushButton_10 = QPushButton("8",self)
        self.gridLayout_2.addWidget(self.pushButton_10, 4, 1, 1, 1)
        self.pushButton_12 = QPushButton("×",self)
        self.gridLayout_2.addWidget(self.pushButton_12, 4, 3, 1, 1)
        self.pushButton_11 = QPushButton("9",self)
        self.gridLayout_2.addWidget(self.pushButton_11, 4, 2, 1, 1)
        self.pushButton_13 = QPushButton("0",self)
        self.gridLayout_2.addWidget(self.pushButton_13, 5, 0, 1, 1)
        self.pushButton_14 = QPushButton(".",self)
        self.gridLayout_2.addWidget(self.pushButton_14, 5, 1, 1, 1)
        self.pushButton_17 = QPushButton("(",self)
        self.gridLayout_2.addWidget(self.pushButton_17, 2, 4, 1, 1)
        self.textEdit = QTextBrowser(self)
        self.textEdit.setEnabled(True)
        self.gridLayout_2.addWidget(self.textEdit, 0, 0, 1, 5)
        self.lineEdit = QLineEdit(self)
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setFocus()
        self.gridLayout_2.addWidget(self.lineEdit, 1, 0, 1, 5)
        self.pushButton_18 = QPushButton(")",self)
        self.gridLayout_2.addWidget(self.pushButton_18, 3, 4, 1, 1)
        self.pushButton_19 = QPushButton("C",self)
        self.gridLayout_2.addWidget(self.pushButton_19, 4, 4, 1, 1)
        self.pushButton_16 = QPushButton("/",self)
        self.gridLayout_2.addWidget(self.pushButton_16, 5, 4, 1, 1)
        self.pushButton_15 = QPushButton("=",self)
        self.gridLayout_2.addWidget(self.pushButton_15, 5, 2, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout_2)

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
        self.show()

    def Show(self):
        self.showNormal()
        self.activateWindow()
        self.setWindowFlags(QtCore.Qt.Window)
        self.show()


    def numss(self,nnum):
        if nnum == 'C':
            self.lineEdit.clear()
            #self.textEdit.clear()
            self.ji = '' # 这里需要在清空一下，否则会把之前的记录加进来
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

    def closeEvent(self, event):
        reply = QMessageBox(QMessageBox.Question, self.tr("提示"), self.tr("确定要退出吗?"), QMessageBox.NoButton, self)
        yr_btn = reply.addButton(self.tr("是的我要退出"), QMessageBox.YesRole)
        reply.addButton(self.tr("最小化到托盘"), QMessageBox.NoRole)
        reply.exec_()
        if reply.clickedButton() == yr_btn:
            event.accept()
        else:
            event.ignore()
            # 最小化到托盘
            self.setWindowFlags(QtCore.Qt.SplashScreen | QtCore.Qt.FramelessWindowHint)
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    jisuanqi = Jsq()
    sys.exit(app.exec_())

