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

        self.ui.pushButton_8.clicked.connect(self.login)
        self.ui.pushButton_9.clicked.connect(self.book_add_save)
        self.ui.pushButton_10.clicked.connect(self.book_get_save)
        self.ui.pushButton_11.clicked.connect(self.book_take_save)
        self.ui.pushButton_12.clicked.connect(self.book_look_button)
        self.ui.pushButton_13.clicked.connect(self.book_find_button)
        self.ui.pushButton_15.clicked.connect(self.app_pin_trans_button)

        self.ui.pushButton.setEnabled(False)
        self.ui.pushButton_2.setEnabled(False)
        self.ui.pushButton_7.setEnabled(False)
        self.ui.pushButton_3.setEnabled(False)
        self.ui.pushButton_4.setEnabled(False)
        self.ui.pushButton_5.setEnabled(False)
        self.ui.pushButton_6.setEnabled(False)

        self.home()


    def home(self):
        self.ui.stackedWidget.setCurrentIndex(self.home_index)

        self.ui.pushButton.setEnabled(False)
        self.ui.pushButton_2.setEnabled(False)
        self.ui.pushButton_7.setEnabled(False)
        self.ui.pushButton_3.setEnabled(False)
        self.ui.pushButton_4.setEnabled(False)
        self.ui.pushButton_5.setEnabled(False)
        self.ui.pushButton_6.setEnabled(False)
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


    def login(self):
        a=self.ui.lineEdit.text()
        b=self.ui.lineEdit_2.text()

        if a=="admin" and b =="1234" :
            self.ui.pushButton.setEnabled(True)
            self.ui.pushButton_2.setEnabled(True)
            self.ui.pushButton_7.setEnabled(True)
            self.ui.pushButton_3.setEnabled(True)
            self.ui.pushButton_4.setEnabled(True)
            self.ui.pushButton_5.setEnabled(True)
            self.ui.pushButton_6.setEnabled(True)

            self.book_get()

            self.ui.lineEdit.clear()
            self.ui.lineEdit_2.clear()

        else:
            QMessageBox.critical(self,"Hatalı Giriş","Lütfen id ve şifrenizi doğru giriniz.")

            self.ui.lineEdit.clear()
            self.ui.lineEdit_2.clear()




    def book_add_save(self):
        pass
    def book_get_save(self):
        pass
    def book_take_save(self):
        pass
    def book_look_button(self):
        pass
    def book_find_button(self):
        pass
    def app_pin_trans_button(self):
        pass



uygulama = QApplication([])
pencere = library_admin()
pencere.show()
uygulama.exec_()