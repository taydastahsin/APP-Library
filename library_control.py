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



        self.ui.pushButton.clicked.connect(self.home)
        self.ui.pushButton_2.clicked.connect(self.book_add)
        self.ui.pushButton_7.clicked.connect(self.book_get)
        self.ui.pushButton_3.clicked.connect(self.book_take)
        self.ui.pushButton_4.clicked.connect(self.book_look)
        self.ui.pushButton_5.clicked.connect(self.book_find)


        self.ui.pushButton_8.clicked.connect(self.login)
        self.ui.pushButton_9.clicked.connect(self.book_add_save)
        self.ui.pushButton_10.clicked.connect(self.book_get_save)
        self.ui.pushButton_11.clicked.connect(self.book_take_save)
        self.ui.pushButton_12.clicked.connect(self.book_look_button)
        self.ui.pushButton_13.clicked.connect(self.book_find_button)


        self.ui.pushButton.setEnabled(False)
        self.ui.pushButton_2.setEnabled(False)
        self.ui.pushButton_7.setEnabled(False)
        self.ui.pushButton_3.setEnabled(False)
        self.ui.pushButton_4.setEnabled(False)
        self.ui.pushButton_5.setEnabled(False)


        self.home()


    def home(self):
        self.ui.stackedWidget.setCurrentIndex(self.home_index)

        self.ui.pushButton.setEnabled(False)
        self.ui.pushButton_2.setEnabled(False)
        self.ui.pushButton_7.setEnabled(False)
        self.ui.pushButton_3.setEnabled(False)
        self.ui.pushButton_4.setEnabled(False)
        self.ui.pushButton_5.setEnabled(False)
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

    # Not: Giriş id ve şifreyi veri tabanına bağlancak
    def login(self):
        baglanti = sqlite3.connect("DbLibrary.db")
        islem = baglanti.cursor()
        baglanti.commit()

        islem.execute(
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
            self.book_get()

            self.ui.lineEdit.clear()
            self.ui.lineEdit_2.clear()

        else:
            QMessageBox.critical(self, "Hatalı Giriş", "Lütfen id ve şifrenizi doğru giriniz.")

            self.ui.lineEdit.clear()
            self.ui.lineEdit_2.clear()

    # Not: Otomatik zaman eklenecek
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
        f = int(self.ui.lineEdit_8.text())

        try:
            ekle = "insert into bookadd (bookName,bookNo,bookWriter,bookHome,bookTranstle,bookPage) values (?,?,?,?,?,?)"
            islem.execute(ekle, (a, b, c, d, e, f))
            baglanti.commit()

            self.ui.lineEdit_3.clear()
            self.ui.lineEdit_4.clear()
            self.ui.lineEdit_5.clear()
            self.ui.lineEdit_6.clear()
            self.ui.lineEdit_7.clear()
            self.ui.lineEdit_8.clear()

        except:
            QMessageBox.warning(self, "Hata Mesajı", "Veri Kaydı Yapılamadı .")

    # Not: Otomatik zaman eklenecek
    def book_get_save(self):
        baglanti = sqlite3.connect("DbLibrary.db")
        islem = baglanti.cursor()
        baglanti.commit()

        islem.execute(
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

            self.ui.lineEdit_9.clear()
            self.ui.lineEdit_10.clear()
            self.ui.lineEdit_11.clear()
            self.ui.lineEdit_12.clear()
            self.ui.lineEdit_13.clear()
            self.ui.lineEdit_14.clear()

        except :
            QMessageBox.warning(self, "Hata Mesajı", "Veri Kaydı Yapılamadı .")

    # Tamamlandı.
    def book_take_save(self):
        db = sqlite3.connect("DbLibrary.db")
        cursor = db.cursor()

        silincek_veri=self.ui.lineEdit_15.text()
        silincek_veri_1=self.ui.lineEdit_16.text()

        command ="delete from bookget where bookName = ? or bookNo = ?"
        try:
            cursor.execute(command,(silincek_veri,silincek_veri_1))
            db.commit()
        except:
            QMessageBox.warning(self, "Hata Mesajı", "Lütfen Verileri Düzgün giriniz!!!!! .")

    # Tamamlandı.
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

    def book_find_button(self):#Bozuk Düzenlecek "like" metodunu kullan
        db = sqlite3.connect("DbLibrary.db")
        cursor = db.cursor()
        find=str(self.ui.lineEdit_24.text())

        command = "SELECT * FROM bookadd WHERE bookName LIKE '%s' LIMIT 100;"%("%"+find+"%")

        try:
            data = cursor.execute(command)
            result =data.fetchall()

            self.ui.tableWidget_2.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.ui.tableWidget_2.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.ui.tableWidget_2.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        except:
            QMessageBox.warning(self, "Hata Mesajı", "Veri Bulma İşlemi Yapılamadı .")







uygulama = QApplication([])
pencere = library_admin()
pencere.show()
uygulama.exec_()