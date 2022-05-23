from PyQt5.QtWidgets import *
from library import Ui_MainWindow
import sqlite3
import datetime
from PyQt5.QtGui import QIntValidator,QIcon




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
        self.book_change_password_index=6



        self.ui.pushButton.clicked.connect(self.home)
        self.ui.pushButton_2.clicked.connect(self.book_add)
        self.ui.pushButton_7.clicked.connect(self.book_get)
        self.ui.pushButton_3.clicked.connect(self.book_take)
        self.ui.pushButton_4.clicked.connect(self.book_look)
        self.ui.pushButton_5.clicked.connect(self.book_find)
        self.ui.pushButton_6.clicked.connect(self.book_change_password)


        self.ui.pushButton_8.clicked.connect(self.login)
        self.ui.pushButton_9.clicked.connect(self.book_add_save)
        self.ui.pushButton_10.clicked.connect(self.book_get_save)
        self.ui.pushButton_11.clicked.connect(self.book_take_save)
        self.ui.pushButton_12.clicked.connect(self.book_look_button)
        self.ui.pushButton_13.clicked.connect(self.book_find_button)
        self.ui.pushButton_14.clicked.connect(self.book_change_password_button)
        self.ui.pushButton_15.clicked.connect(self.book_delete_button)



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

        self.ui.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);color: rgb(255, 0, 0);")
        self.ui.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.pushButton_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.pushButton_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.pushButton_6.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.ui.pushButton.setEnabled(False)
        self.ui.pushButton_2.setEnabled(False)
        self.ui.pushButton_7.setEnabled(False)
        self.ui.pushButton_3.setEnabled(False)
        self.ui.pushButton_4.setEnabled(False)
        self.ui.pushButton_5.setEnabled(False)
        self.ui.pushButton_6.setEnabled(False)

    def book_add(self):
        self.ui.stackedWidget.setCurrentIndex(self.book_add_index)

        self.ui.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);color: rgb(255, 0, 0);")
        self.ui.pushButton_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.pushButton_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.pushButton_6.setStyleSheet("background-color: rgb(255, 255, 255);")

    def book_get(self):
        self.ui.stackedWidget.setCurrentIndex(self.book_get_index)

        self.ui.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.pushButton_7.setStyleSheet("background-color: rgb(255, 255, 255);color: rgb(255, 0, 0);")
        self.ui.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.pushButton_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.pushButton_6.setStyleSheet("background-color: rgb(255, 255, 255);")

    def book_take(self):
        self.ui.stackedWidget.setCurrentIndex(self.book_take_index)

        self.ui.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.pushButton_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 255);color: rgb(255, 0, 0);")
        self.ui.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.pushButton_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.pushButton_6.setStyleSheet("background-color: rgb(255, 255, 255);")

    def book_look(self):
        self.ui.stackedWidget.setCurrentIndex(self.book_look_index)

        self.ui.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.pushButton_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 255);color: rgb(255, 0, 0);")
        self.ui.pushButton_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.pushButton_6.setStyleSheet("background-color: rgb(255, 255, 255);")

    def book_find(self):
        self.ui.stackedWidget.setCurrentIndex(self.book_find_index)

        self.ui.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.pushButton_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.pushButton_5.setStyleSheet("background-color: rgb(255, 255, 255);color: rgb(255, 0, 0);")
        self.ui.pushButton_6.setStyleSheet("background-color: rgb(255, 255, 255);")

    def book_change_password(self):
        self.ui.stackedWidget.setCurrentIndex(self.book_change_password_index)

        self.ui.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.pushButton_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.pushButton_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.pushButton_6.setStyleSheet("background-color: rgb(255, 255, 255);color: rgb(255, 0, 0);")




    # Tamamlandı.
    def login(self):
        id = self.ui.lineEdit.text()
        pw = self.ui.lineEdit_2.text()

        db = sqlite3.connect("DbLibrary.db")
        db.execute('create table if not exists login(username text,password text,id int)')
        db.execute("insert into login(username,password,id) values('astra','astra.1352',1)")
        cursor=db.cursor()
        cursor.execute("select * from login where username=? and password=?",(id,pw))
        row=cursor.fetchone()
        if row:

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



    # Tamamlandı.
    def book_add_save(self):
        try:
            baglanti = sqlite3.connect("DbLibrary.db")
            islem = baglanti.cursor()
            baglanti.commit()

            table = islem.execute(
                "create table if not exists bookadd(bookName text,bookNo int,bookWriter text,bookHome text,bookTranstle text,bookPage int,bookPart text)")
            baglanti.commit()

            a = self.ui.lineEdit_3.text()
            b = int(self.ui.lineEdit_4.text())
            c = self.ui.lineEdit_5.text()
            d = self.ui.lineEdit_6.text()
            e = self.ui.lineEdit_7.text()
            f = int(self.ui.lineEdit_8.text())
            g = self.ui.lineEdit_17.text()


            ekle = "insert into bookadd (bookName,bookNo,bookWriter,bookHome,bookTranstle,bookPage,bookPart) values (?,?,?,?,?,?,?)"
            islem.execute(ekle, (a, b, c, d, e, f,g))
            baglanti.commit()

            self.ui.lineEdit_3.clear()
            self.ui.lineEdit_4.clear()
            self.ui.lineEdit_5.clear()
            self.ui.lineEdit_6.clear()
            self.ui.lineEdit_7.clear()
            self.ui.lineEdit_8.clear()
            self.ui.lineEdit_17.clear()

        except:
            QMessageBox.warning(self, "Hata Mesajı", "Veri Kaydı Yapılamadı .")

    # Tamamlandı.
    def book_get_save(self):
        try:
            baglanti = sqlite3.connect("DbLibrary.db")
            islem = baglanti.cursor()
            baglanti.commit()

            islem.execute(
                "create table if not exists bookget(bookName text,bookNo int,studentName text,studentSurname text,studentNo text,studentSchool text,telNo int,dateNow text)")
            baglanti.commit()

            a = self.ui.lineEdit_9.text()
            b = int(self.ui.lineEdit_10.text())
            c = self.ui.lineEdit_11.text()
            d = self.ui.lineEdit_12.text()
            e = int(self.ui.lineEdit_13.text())
            f = int(self.ui.lineEdit_14.text())
            g= self.ui.comboBox.currentText()
            h=datetime.datetime.now()



            ekle= "insert into bookget (bookName,bookNo,studentName,studentSurname,studentNo,studentSchool,telNo,dateNow) values (?,?,?,?,?,?,?,?)"
            islem.execute(ekle,(a,b,c,d,e,g,f,h))
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
        try:
            db = sqlite3.connect("DbLibrary.db")
            cursor = db.cursor()

            silincek_veri=self.ui.lineEdit_15.text()
            silincek_veri_1=self.ui.lineEdit_16.text()

            command ="delete from bookget where bookName = ? or bookNo = ?"

            cursor.execute(command,(silincek_veri,silincek_veri_1))
            db.commit()

            self.ui.lineEdit_15.clear()
            self.ui.lineEdit_16.clear()
        except:
            QMessageBox.warning(self, "Hata Mesajı", "Lütfen Verileri Düzgün giriniz!!!!! .")

    # Tamamlandı.
    def book_look_button(self):
        try:
            db = sqlite3.connect("DbLibrary.db")
            cursor = db.cursor()

            find= str(self.ui.lineEdit_28.text())

            command = "SELECT * FROM bookget WHERE studentNo LIKE '%s' LIMIT 100;" % ("%" + find + "%")

            result =cursor.execute(command)

            self.ui.tableWidget.setRowCount(0)

            for row_number,row_data in enumerate(result):
                self.ui.tableWidget.insertRow(row_number)
                for column_number,data in enumerate(row_data):
                    self.ui.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str(data)))
        except:
            QMessageBox.warning(self, "Hata Mesajı", "Veri Bulma İşlemi Yapılamadı .")

    # Tamamlandı.
    def book_find_button(self):
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

    # Tamamlandı.
    def book_delete_button(self):
        try:
            db = sqlite3.connect("DbLibrary.db")
            cursor = db.cursor()

            silincek_veri = self.ui.lineEdit_24.text()

            command = "delete from bookadd where bookName = ? "

            cursor.execute(command, (silincek_veri,))
            db.commit()

            self.ui.lineEdit_24.clear()
        except:
            QMessageBox.warning(self, "Hata Mesajı", "Lütfen Verileri Düzgün giriniz!!!!! .")

    # Tamamlandı.
    def book_change_password_button(self):
        db = sqlite3.connect("DbLibrary.db")
        cursor = db.cursor()

        usernew =self.ui.lineEdit_25.text()
        pwnew = self.ui.lineEdit_26.text()
        id =1
        try:
            if usernew =="" or pwnew=="":
                QMessageBox.critical(self, "Hata Mesajı", "Lütfen kullanıcı adını ve şifreyi giriniz!!!!!!")
            else:

                cursor.execute("update login set username = ?,password = ? where id = ? ",(usernew,pwnew,id))
                db.commit()
                QMessageBox.critical(self, "Başarılı Değiştirme", "Şifreniz Değiştirilmiştir.")

                self.home()

                self.ui.lineEdit_25.clear()
                self.ui.lineEdit_26.clear()


        except:
            QMessageBox.critical(self, "Hata Mesajı", "Lütfen Tekrar Yazınız!!!!!!")

            ekle = "insert into bookadd (username,password ) values (?,?)"
            cursor.execute(ekle, (usernew, pwnew))

            self.ui.lineEdit_25.clear()
            self.ui.lineEdit_26.clear()







uygulama = QApplication([])
pencere = library_admin()
pencere.show()
uygulama.exec_()