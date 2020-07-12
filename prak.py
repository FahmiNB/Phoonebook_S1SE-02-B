#Untuk mengimport library yang digunakan
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *
from EntryForm import *
from PyQt5 import QtGui


class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.loadData()

    def setupUi(self):
        self.setFixedSize(340, 300) # untuk mengatur ukuran form
        self.move(300, 300) # untuk mengatur posisi
        self.setWindowIcon(QtGui.QIcon('icon.png')) # memberi icon pada pojok kiri atas
        self.setWindowTitle("Phonebook Manager") # memberi judul di atas

        self.table = QTableWidget() # tabel yg terdapat di tengah

        self.addButton = QPushButton("Tambah") # menambah tombol Tambah
        self.addButton.setStyleSheet('background-color:rgb(0,100,0);color : white'); # Memberi warna hijau pada tombol Tambah dan font nya putih
        self.editButton = QPushButton("Ubah")
        self.editButton.setStyleSheet('background-color:rgb(139,69,19);color : white'); # Memberi warna coklat pada tombol Ubah dan font nya putih
        self.deleteButton = QPushButton("Hapus")
        self.deleteButton.setStyleSheet('background-color:rgb(255,0,0);color : white'); # Memberi warna Merah pada tombol Hapus dan font nya putih

        hbox = QHBoxLayout() # membuat Layout Horizontal
        hbox.addWidget(self.addButton) # paling kiri
        hbox.addWidget(self.editButton) # di tengah
        hbox.addWidget(self.deleteButton) # paling kanan
        hbox.addStretch() # untuk jarak spasi

        layout = QVBoxLayout() # vertikal Laoyout untuk kolom
        layout.addWidget(self.table) # memebri tabel
        layout.addLayout(hbox) # horizontal untuk baris
        self.setLayout(layout)

        self.addButton.clicked.connect(self.addButtonClick) # memasang method addButtonClick
        self.editButton.clicked.connect(self.editButtonClick) # memasang method editButtonClick
        self.deleteButton.clicked.connect(self.deleteButtonClick) # memasang method deleteButtonClick

    # Mengatur tabel
    def loadData(self):
        self.table.clear() # Di awal ksosongkan databse
        self.table.setRowCount(self.getRowCount()) # Mengatur menggunakan baris
        self.table.setColumnCount(3) # Terdapat 3 kolom
        columnHeaders = ["ID", "Nama", "No. HP"] # Isi kolom
        self.table.setHorizontalHeaderLabels(columnHeaders) # Set layout horizontal agar rapi
        self.table.setStyleSheet('font-family: sans-serif;') # Jenis font

        #TAMPILAN Data
        # Mengoperasikan database
        query = QSqlQuery()
        ID, NAMA, NOHP = range(3) # Mengidentifikasi kolom
        row = 0
        # Menampilkan data
        query.exec_("SELECT * FROM phonebook") 
        while query.next(): # Mengecek isi kolom
            for i in range(3):
                item = QTableWidgetItem()
                item.setText(str(query.value(i)))
                self.table.setItem(row, i, item)
            row += 1
        item = QTableWidgetItem()
        item.setText(str(self.getRowCount()))
        self.table.setItem(6, 0, item)

    # Menghitung banyaknya data dan manipulasi dengan urutanya
    def getRowCount(self): # Membuat method
        query = QSqlQuery()
        query.exec_("SELECT COUNT(id) FROM phonebook")
        query.next()
        rowCount = query.value(0)
        return rowCount

    #TOMBOL TAMBAH 
    def addButtonClick(self): # Membuat method
        self.entryForm = EntryForm() # Memanggil dialog EntryForm
        self.mode = 0 # Dengan mode 0, berarti mode tambah
        if self.entryForm.exec_() == QDialog.Accepted: # Bila Ok maka proses dilanjutkan untuk di tambah
            id = self.getRowCount() + 1 # menambahkan count 1
            # Menggunakan perintah INSERT untuk menambahkan
            query = QSqlQuery()
            query.exec_(
                "INSERT INTO phonebook VALUES (%d,'%s', '%s')"
                % (
                    id,
                    self.entryForm.nameLineEdit.text(), # Berdasarkan nama yang di inputkan di form
                    self.entryForm.phoneLineEdit.text(), # Berdasarkan nomor yang di inputkan di form
                )
            )
        self.loadData()

    # Edit data
    def editButtonClick(self): # Membuat method
        self.entryForm = EntryForm() # Memanggil dialog EntryForm
        self.mode = 1 # Dengan mode 0, berarti mode edit
        # Menggunakan Form nameEdit 
        self.entryForm.nameLineEdit.setText(
            self.table.item(self.table.currentRow(), 1).text() # berdasarkan form yang dipilih 
        )
        # Menggunakan Form phoneEdit
        self.entryForm.phoneLineEdit.setText(
            self.table.item(self.table.currentRow(), 2).text() # berdasarkan form yang dipilih 
        )
        if self.entryForm.exec_() == QDialog.Accepted: # Bila Ok maka proses dilanjutkan untuk di Edit
            id = int(self.table.item(self.table.currentRow(), 0).text()) # Berdasarkan id yang di pilih
        # Menggunakan perintah UPDATE untuk Edit data
            query = QSqlQuery()
            query.exec_(
                """UPDATE phonebook SET nama = '%s', nohp = '%s 'WHERE id = %d"""
                % (
                    self.entryForm.nameLineEdit.text(), # Berdasarkan nama yang di inputkan di form
                    self.entryForm.phoneLineEdit.text(), # Berdasarkan nomor yang di inputkan di form
                    id,
                )
            )
            self.loadData()
    # HAPUS DATA
    def deleteButtonClick(self): 
        id = int(self.table.item(self.table.currentRow(), 0).text()) # Berdasak id yang di pilih
        # Menggunakan perintah DELETE untuk Hapus data
        query = QSqlQuery()
        query.exec_("DELETE FROM phonebook WHERE id = %d" % id)
        self.loadData()


if __name__ == "__main__":
    a = QApplication(sys.argv)
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("test.db")
    if not db.open():
        print("ERROR: " + db.lastError().text())
        sys.exit(1)
    form = MainForm()
    form.show()

    a.exec_()
