from PyQt5.QtWidgets import *
from library import Ui_MainWindow
import json

class librarycontrol(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.home_index=0
        self.book_add_index=1
        self.book_get_index=2
        self.book_take_index=3


        self.ui.actionKitap_Ekle.triggered.connect(self.book_add)
        self.ui.actionKitap_Ver.triggered.connect(self.book_get)
        self.ui.actionKitap_Al.triggered.connect(self.book_take)
        self.ui.actionG_ster.triggered.connect(self.look_book)

        self.ui.pushButton.clicked.connect(self.login)
        self.ui.actionKitap_Ekle.setEnabled(False)
        self.ui.actionKitap_Al.setEnabled(False)
        self.ui.actionKitap_Ver.setEnabled(False)
        self.ui.actionG_ster.setEnabled(False)

        self.home()

    def home(self):
        self.ui.stackedWidget.setCurrentIndex(self.home_index)

    def book_add (self):
        self.ui.stackedWidget.setCurrentIndex(self.book_add_index)
        self.ui.pushButton_2.clicked.connect(self.book_add_save)
    def book_add_save(self):
        a= self.ui.lineEdit_3.text()
        b=self.ui.lineEdit_5.text()

        dict = {"book_no": a,"book_name":b

                }

        with open('book_add.json', 'w') as json_file:
            json.dump(dict, json_file)

        self.ui.lineEdit_3.clear()
        self.ui.lineEdit_5.clear()

    def book_get (self):
        self.ui.stackedWidget.setCurrentIndex(self.book_get_index)
        self.ui.pushButton_4.clicked.connect(self.book_get_save)
    def book_get_save(self):
        a = self.ui.lineEdit_6.text()
        b= self.ui.lineEdit_7.text()
        c= self.ui.lineEdit_8.text()
        d= self.ui.lineEdit_9.text()

        data = {"book_no": a,"book_name":b,
                "student_name":c,"student_no":d

                }

        data = {data[i]: data[i + 1] for i in range(0, len(data), 2)}

        with open("book_get.json", "w") as j:
            json.dump(data, j)






        self.ui.lineEdit_6.clear()
        self.ui.lineEdit_7.clear()
        self.ui.lineEdit_8.clear()
        self.ui.lineEdit_9.clear()

    def book_take (self):
        self.ui.stackedWidget.setCurrentIndex(self.book_take_index)
        self.ui.pushButton_5.clicked.connect(self.book_take_Save)
    def book_take_save(self):
        a = self.ui.lineEdit_13.text()
        b = self.ui.lineEdit_11.text()
        c = self.ui.lineEdit_12.text()
        d = self.ui.lineEdit_10.text()

        dict = {"book_no": a, "book_name": b,
                "student_name": c, "student_no": d

                }

        with open('book_take.json', 'w') as json_file:
            json.dump(dict, json_file)

    def look_book(self):
        pass

    def login(self):
        a=self.ui.lineEdit .text()
        b=self.ui.lineEdit_2.text()

        if a == "admin" and b =="12345" :
            self.ui.actionKitap_Ekle.setEnabled(True)
            self.ui.actionKitap_Al.setEnabled(True)
            self.ui.actionKitap_Ver.setEnabled(True)
            self.ui.actionG_ster.setEnabled(True)
            self.book_get()
        else :
            self.ui.lineEdit.clear()
            self.ui.lineEdit_2.clear()
            QMessageBox.warning(self, "Hatalı Giriş", "Lütfen Tekrar Deneyiniz!!!!!!")




app =QApplication([])
window=librarycontrol()
window.show()
app.exec_()
