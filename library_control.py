from PyQt5.QtWidgets import *
from library import Ui_MainWindow

class library_admin (QMainWindow) :
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.home_index =0
        self.book_add_index =1
        self.book_get_index =2
        self.book_take_index=3
        self.book_look_index=4
        self.book_find_index=5
        self.app_pin_trans_index=6

        self.ui.pushButton.clicked.connect(self.home)
        self.ui.pushButton_2.clicked.connect(self.book_add)
        self.ui.pushButton_7.clicked.connect(self.book_get)
        self.ui.pushButton_3.clicked.connect(self.book_take)
        self.ui.pushButton_4.clicked.connect(self.book_look)
        self.ui.pushButton_5.clicked.connect(self.book_find)
        self.ui.pushButton_6.clicked.connect(self.app_pin_trans)


    def home(self):
        self.ui.stackedWidget.setCurrentIndex(self.home_index)
    def book_add(self):
        self.ui.stackedWidget.setCurrentIndex(self.book_add_index)
    def book_get(self):
        self.ui.stackedWidget.setCurrentIndex(self.book_get_index)
    def book_take(self):
        self.ui.stackedWidget.setCurrentIndex(self.book_take_index)
    def book_look(self):
        self.ui.stackedWidget.setCurrentIndex(self.book_look_index)
    def book_find(self):
        self.ui.stackedWidget.setCurrentIndex(self.book_find_index)
    def app_pin_trans(self):
        self.ui.stackedWidget.setCurrentIndex(self.app_pin_trans_index)

uygulama = QApplication([])
pencere = library_admin()
pencere.show()
uygulama.exec_()