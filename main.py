# _*_ coding: UTF-8 _*_

import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QHBoxLayout, QPushButton, QMenuBar, QTextEdit, QAction


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setGeometry(600, 300, 500, 500)

        # 标题
        self.setWindowTitle('xml 编辑器')

        # 顶部菜单栏
        menuBar = self.menuBar()
        menuBar.setNativeMenuBar(False)
        self.fileMenu = menuBar.addMenu('File')
        self.setFileMenu()

        self.editMenu = menuBar.addMenu('Edit')
        self.setFileMenu()

        self.viewMenu = menuBar.addMenu('View')
        self.setViewMenu()

        self.toolMenu = menuBar.addMenu('Tool')
        self.setToolMenu()

        self.windowMenu = menuBar.addMenu('Window')
        self.setWindowMenu()

        self.helpMenu = menuBar.addMenu('Help')
        self.setHelpMenu()

        # 主体
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        # 状态栏
        status = self.statusBar()
        status.showMessage('Ready')

        # self.resize(900, 300)  # 设置窗口的大小
        # self.status.showMessage('正在处理中......', 0)  # 显示状态栏信息，默认为0(表示下一个操作前，一直显示状态栏；也可以设置显示时间，单位为毫秒)
        # self.setWindowTitle('PyQt MainWindow操作例子')  # 设置该窗口的名称
        # self.button1 = QPushButton('关闭当前窗口！')  # 创建一个按钮，并赋予相应的文本
        # self.button1.clicked.connect(self.onButtonClick)  # 关联按钮的点击信号与onButtonClickx信号槽
        # layout = QHBoxLayout()  # 设置水平布局
        # layout.addWidget(self.button1)  # 水平布局应用到button1
        # main_frame = QWidget()
        # main_frame.setLayout(layout)
        # self.setCentralWidget(main_frame)  # 设置窗口中心的控件

    def setFileMenu(self):
        # New Action
        newAction = QAction(QIcon('new.png'), 'New', self)
        newAction.setShortcut('Ctrl+N')
        newAction.setStatusTip('新建文件')
        # newAction.triggered.connect(self.close)
        self.fileMenu.addAction(newAction)

        # Open Action
        openAction = QAction(QIcon('open.png'), 'Open...', self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('打开文件')
        # openAction.triggered.connect(self.close)
        self.fileMenu.addAction(openAction)

        # Save Action
        saveAction = QAction(QIcon('save.png'), 'Save', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.setStatusTip('保存')
        # saveAction.triggered.connect(self.close)
        self.fileMenu.addAction(saveAction)

        # Save as Action
        saveAsAction = QAction(QIcon('saveAs.png'), 'Save as...', self)
        saveAsAction.setStatusTip('另存为')
        # saveAsAction.triggered.connect(self.close)
        self.fileMenu.addAction(saveAsAction)

        # Exit Action
        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('退出程序')
        exitAction.triggered.connect(self.close)
        self.fileMenu.addAction(exitAction)

    def setEditMenu(self):
        pass

    def setViewMenu(self):
        pass

    def setToolMenu(self):
        pass

    def setWindowMenu(self):
        pass

    def setHelpMenu(self):
        pass

    def onButtonClick(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('xml.ico'))
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
