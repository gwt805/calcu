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
from PyQt5.QtCore import QCoreApplication
import img

class Jsq(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(358, 372)
        # fix window size
        self.setFixedWidth(350)
        self.setFixedHeight(350)
        self.setWindowIcon(QIcon(':img/jsq_logo.svg'))
        self.setWindowTitle('计算器')
        # let the window center
        screen = QDesktopWidget().screenGeometry()
        window_size = self.geometry()
        self.move(int((screen.width() - window_size.width()) / 2) , int((screen.height() - window_size.height()) / 2))

        # sys tray
        self.tray = QSystemTrayIcon()
        self.tray.setIcon(QIcon(':img/jsq_logo.svg'))
        showAction = QAction("打开", self, triggered = self.Show)
        quitAction = QAction("退出", self, triggered = QCoreApplication.instance().quit)
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
        self.grid = QGridLayout()
        self.grid.setSizeConstraint(QLayout.SetNoConstraint)
        self.grid.setHorizontalSpacing(3)
        self.grid.setVerticalSpacing(6)

        self.textEdit = QTextBrowser(self)
        self.textEdit.setEnabled(True)
        self.lineEdit = QLineEdit(self)
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setFocus()

        self.num_0 = QPushButton("0",self)
        self.num_1 = QPushButton("1",self)
        self.num_2 = QPushButton("2",self)
        self.num_3 = QPushButton("3",self)
        self.num_4 = QPushButton("4",self)
        self.num_5 = QPushButton('5',self)
        self.num_6 = QPushButton("6",self)
        self.num_7 = QPushButton('7',self)
        self.num_8 = QPushButton("8",self)
        self.num_9 = QPushButton("9",self)
        self.symbol_add = QPushButton("+",self)
        self.symbol_subtraction = QPushButton("-",self)
        self.symbol_multiplication = QPushButton("×",self)
        self.symbol_division = QPushButton("/",self)
        self.symbol_point = QPushButton(".",self)
        self.symbol_left_brackets = QPushButton("(",self)
        self.symbol_right_brackets = QPushButton(")",self)
        self.symbol_clear = QPushButton("C",self)
        self.symbol_equal = QPushButton("=",self)

        self.grid.addWidget(self.textEdit, 0, 0, 1, 5)
        self.grid.addWidget(self.lineEdit, 1, 0, 1, 5)
        
        self.grid.addWidget(self.num_0, 5, 0, 1, 1)
        self.grid.addWidget(self.num_1, 2, 0, 1, 1)
        self.grid.addWidget(self.num_2, 2, 1, 1, 1)
        self.grid.addWidget(self.num_3, 2, 2, 1, 1)
        self.grid.addWidget(self.num_4, 3, 0, 1, 1)
        self.grid.addWidget(self.num_5, 3, 1, 1, 1)
        self.grid.addWidget(self.num_6, 3, 2, 1, 1)
        self.grid.addWidget(self.num_7, 4, 0, 1, 1)
        self.grid.addWidget(self.num_8, 4, 1, 1, 1)
        self.grid.addWidget(self.num_9, 4, 2, 1, 1)

        self.grid.addWidget(self.symbol_left_brackets, 3, 3, 1, 1)# 换位
        self.grid.addWidget(self.symbol_subtraction, 2, 3, 1, 1)
        self.grid.addWidget(self.symbol_multiplication, 4, 3, 1, 1)
        self.grid.addWidget(self.symbol_division, 4, 4, 1, 1) 
        self.grid.addWidget(self.symbol_add, 2, 4, 1, 1)# 换位
        self.grid.addWidget(self.symbol_right_brackets, 3, 4, 1, 1)
        self.grid.addWidget(self.symbol_point, 5, 1, 1, 1)
        self.grid.addWidget(self.symbol_clear, 5, 2, 1, 1) 
        self.grid.addWidget(self.symbol_equal, 5, 3, 1, 2)

        self.verticalLayout.addLayout(self.grid)
        self.jsq_logic()

        
        self.show()
    def jsq_logic(self):
        # mycode
        self.ji = '' # 多行文本框赋值用
        self.num_0.clicked.connect(lambda:self.numss('0'))
        self.num_1.clicked.connect(lambda:self.numss('1'))
        self.num_2.clicked.connect(lambda:self.numss('2'))
        self.num_3.clicked.connect(lambda:self.numss('3'))
        self.num_4.clicked.connect(lambda:self.numss('4'))
        self.num_5.clicked.connect(lambda:self.numss('5'))
        self.num_6.clicked.connect(lambda:self.numss('6'))
        self.num_7.clicked.connect(lambda:self.numss('7'))
        self.num_8.clicked.connect(lambda:self.numss('8'))
        self.num_9.clicked.connect(lambda:self.numss('9'))
        self.symbol_point.clicked.connect(lambda:self.numss('.'))
        self.symbol_add.clicked.connect(lambda:self.numss('+'))
        self.symbol_subtraction.clicked.connect(lambda:self.numss('-'))
        self.symbol_multiplication.clicked.connect(lambda:self.numss('*'))
        self.symbol_division.clicked.connect(lambda:self.numss('/'))
        self.symbol_left_brackets.clicked.connect(lambda:self.numss('('))
        self.symbol_right_brackets.clicked.connect(lambda:self.numss(')'))
        self.symbol_clear.clicked.connect(lambda:self.numss('C'))
        self.symbol_clear.setShortcut('escape')
        self.symbol_equal.clicked.connect(lambda:self.numss('='))
        self.lineEdit.returnPressed.connect(lambda:self.numss('='))

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

    def closeEvent(self, event): # 重写关闭事件
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

