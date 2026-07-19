import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        #navigation
        navBar=QToolBar()
        self.addToolBar(navBar)

        back_button = QAction('<-', self)
        back_button.triggered.connect(self.browser.back)
        navBar.addAction(back_button)

        frwd_button = QAction('->', self)
        frwd_button.triggered.connect(self.browser.forward)
        navBar.addAction(frwd_button)

        refresh_button = QAction('Reload', self)
        refresh_button.triggered.connect(self.browser.reload)
        navBar.addAction(refresh_button)

        home_button = QAction('Home', self)
        home_button.triggered.connect(self.navigate_home)
        navBar.addAction(home_button)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate)
        navBar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)
    
    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))

    def navigate(self):
        url=self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self,q):
        self.url_bar.setText(q.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName("ShuShu's Browser")
window =MainWindow()
app.exec_()