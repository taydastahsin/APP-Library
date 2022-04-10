from PyQt5.QtWidgets import *
from library import Ui_MainWindow
import sqlite3
from PyQt5.QtSql import *

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
        baglanti = sqlite3.connect("DbLibrary.db")
        islem = baglanti.cursor()
        baglanti.commit()

        table = islem.execute(
            "create table if not exists login(adminName text,adminPin int)")
        baglanti.commit()

        a=self.ui.lineEdit.text()
        b=int(self.ui.lineEdit_2.text())
        # insert yerine update kullan // Giriş id ve şifreyi veritabanına eşitleyip koşullandır.
        #ekle = "insert into login (adminName,adminPin) values (?,?)"
        #islem.execute(ekle, (a, b))
        #baglanti.commit()

        if a == "admin" and b == 1234:
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
            QMessageBox.critical(self, "Hatalı Giriş", "Lütfen id ve şifrenizi doğru giriniz.")

            self.ui.lineEdit.clear()
            self.ui.lineEdit_2.clear()





    def book_add_save(self):
        baglanti = sqlite3.connect("DbLibrary.db")
        islem = baglanti.cursor()
        baglanti.commit()

        table = islem.execute(
            "create table if not exists bookadd(bookName text,bookNo int,bookWriter text,bookHome text,bookTranstle text,bookPage int)")
        baglanti.commit()

        a = self.ui.lineEdit_3.text()
        b = int(self.ui.lineEdit_4.text())
        c = self.ui.lineEdit_5.text()
        d = self.ui.lineEdit_6.text()
        e = self.ui.lineEdit_7.text()
        f = int (self.ui.lineEdit_8.text())

        try:
            ekle= "insert into bookadd (bookName,bookNo,bookWriter,bookHome,bookTranstle,bookPage) values (?,?,?,?,?,?)"
            islem.execute(ekle,(a,b,c,d,e,f))
            baglanti.commit()
        except :
            QMessageBox.warning(self, "Hata Mesajı", "Veri Kaydı Yapılamadı .")








    def book_get_save(self):
        # Not: Otomatik zaman eklenecek
        baglanti = sqlite3.connect("DbLibrary.db")
        islem = baglanti.cursor()
        baglanti.commit()

        table = islem.execute(
            "create table if not exists bookget(bookName text,bookNo int,studentName text,studentSurname text,studentNo int,telNo int)")
        baglanti.commit()

        a = self.ui.lineEdit_9.text()
        b = int(self.ui.lineEdit_10.text())
        c = self.ui.lineEdit_11.text()
        d = self.ui.lineEdit_12.text()
        e = int(self.ui.lineEdit_13.text())
        f = int(self.ui.lineEdit_14.text())


        try:
            ekle= "insert into bookget (bookName,bookNo,studentName,studentSurname,studentNo,telNo) values (?,?,?,?,?,?)"
            islem.execute(ekle,(a,b,c,d,e,f))
            baglanti.commit()
        except :
            QMessageBox.warning(self, "Hata Mesajı", "Veri Kaydı Yapılamadı .")







    def book_take_save(self):
        #Silme işlemi yapılcak
        pass

    def book_look_button(self):
        db = sqlite3.connect("DbLibrary.db")
        cursor = db.cursor()

        command =""" select * from bookget"""

        result =cursor.execute(command)

        self.ui.tableWidget.setRowCount(0)

        for row_number,row_data in enumerate(result):
            self.ui.tableWidget.insertRow(row_number)
            for column_number,data in enumerate(row_data):
                self.ui.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str(data)))

    def book_find_button(self):
        #Bulma yapılcak
        pass

    def app_pin_trans_button(self):
        #Update yapılcak
        pass



uygulama = QApplication([])
pencere = library_admin()
pencere.show()
uygulama.exec_()