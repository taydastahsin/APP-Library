from PyQt5.QtWidgets import *
from library import Ui_MainWindow

class librarycontrol(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.home_index=5
        self.book_add_index=4
        self.sorumlu_add_index=3
        self.book_get_index=2
        self.book_take_index=1


        self.ui.actionKitap_Ekle.triggered.connect(self.book_add)
        self.ui.actionSorumlu_Ekle.triggered.connect(self.sorumlu_add)
        self.ui.actionKitap_Ver.triggered.connect(self.book_get)
        self.ui.actionKitap_Al.triggered.connect(self.book_take)

        self.ui.pushButton.clicked.connect(self.login)
        self.ui.actionSorumlu_Ekle.setEnabled(False)
        self.ui.actionKitap_Ekle.setEnabled(False)
        self.ui.actionKitap_Al.setEnabled(False)
        self.ui.actionKitap_Ver.setEnabled(False)

        self.home()

    def home(self):
        self.ui.stackedWidget.setCurrentIndex(self.home_index)
    def book_add (self):
        self.ui.stackedWidget.setCurrentIndex(self.book_add_index)
    def sorumlu_add (self):
        self.ui.stackedWidget.setCurrentIndex(self.sorumlu_add_index)
    def book_get (self):
        self.ui.stackedWidget.setCurrentIndex(self.book_get_index)
    def book_take (self):
        self.ui.stackedWidget.setCurrentIndex(self.book_take_index)

    def login(self):
        a=self.ui.lineEdit .text()
        b=self.ui.lineEdit_2.text()

        if a == "admin" and b =="12345" :
            self.ui.actionSorumlu_Ekle.setEnabled(True)
            self.ui.actionKitap_Ekle.setEnabled(True)
            self.ui.actionKitap_Al.setEnabled(True)
            self.ui.actionKitap_Ver.setEnabled(True)



app =QApplication([])
window=librarycontrol()
window.show()
app.exec_()
