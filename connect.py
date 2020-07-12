from PyQt5.QtSql import *


def connectdb():
    db = QSqlDatabase.addDatabase("QSQLITE") # menggunakan library QSQLITE
    db.setDatabaseName("test.db") # membuat database test.db
    # mengecek bilsa benar atau salah
    if db.open():
        # print("Koneksi telah dibuat")
        #createdb()
        #insertdb()
        showdb()
    else:
        print("ERROR: " + db.lastError().text())

# PEMBUATAN TABEL
def createdb():
    # membuat tabel dengan query CREATE TABLE 
    query = QSqlQuery()
    # struktur tabel yang di buat
    query.exec_(
        """CREATE TABLE phonebook(Id INTEGER NOT NULL PRIMARY KEY,Nama VARCHAR(25),Nohp VARCHAR (15))"""
    )
    if query.exec_:
        print("Buat tabel Berhasil")

	
connectdb()
