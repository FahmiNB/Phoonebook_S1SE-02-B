#Untuk mengimport library yang digunakan
from PyQt5.QtWidgets import (
    QDialog,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
)
from PyQt5 import QtGui


class EntryForm(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(300, 100) # untuk mengatur ukuran form
        self.move(320, 280) # untuk mengatur posisi
        self.setWindowIcon(QtGui.QIcon('icon.png')) # memberi icon pada pojok kiri atas
        self.setWindowTitle("Tambah/Ubah Kontak") # memberi judul di atas

        self.mode = -1  # 0: mode tambah, 1: mode ubah

         # menambah tombol OK
        self.okButton = QPushButton("OK")
        # memberi jenis font
        self.okButton.setStyleSheet('font-family: sans-serif;;') 
         # Memberi warna hijau pada tombol OK dan font nya putih
        self.okButton.setStyleSheet('background-color:rgb(60,179,113);color : white'); 
        # menambah tombol Batal
        self.cancelButton = QPushButton("Batal") 
        # memberi jenis font
        self.cancelButton.setStyleSheet('font-family: sans-serif;;') 
        # Memberi warna Merah pada tombol Batal dan font nya putih
        self.cancelButton.setStyleSheet('background-color:rgb(255,0,0);color : white'); 

        hbox = QHBoxLayout() # menggunakan Layout horizontal biar tombol sejajar
        hbox.addWidget(self.okButton) # tombol ok di kiri
        hbox.addWidget(self.cancelButton) # tombol cancel di kanan

        self.label1 = QLabel("Nama Lengkap:") # memberi label Nama lengkap
        self.label1.setStyleSheet('font-family: sans-serif;')  # memberi jenis font
        self.nameLineEdit = QLineEdit() # memberi form kosong LineEdit
        self.label2 = QLabel("Nomor HP:") # memberi label Nama Nomor HP
        self.label1.setStyleSheet('font-family: sans-serif;') # memberi jenis font

        # Megkososngkan Form
        self.phoneLineEdit = QLineEdit()
        if self.mode == 0:
            self.nameLineEdit.clear()
            self.phoneLineEdit.clear()

        # Mengagatur layout dengan index
        layout = QGridLayout()
        #label Nama berada Kolom pertama baris pertama paling pojok kiri atas
        layout.addWidget(self.label1, 0, 0) 
        # Form nama bedara kolom pertama baris kedua
        layout.addWidget(self.nameLineEdit, 0, 1)  
        # Label nomor berada kolom kedua baris pertama
        layout.addWidget(self.label2, 1, 0) 
        # Form nomor berada kolom kedua baris kedua
        layout.addWidget(self.phoneLineEdit, 1, 1) 
        # Tombol OK,Cancel berada kolom ketiga baris ke dua
        layout.addLayout(hbox, 2, 1) 
        self.setLayout(layout)

        #memanggil method accecpt dan reject
        self.okButton.clicked.connect(self.accept)
        self.cancelButton.clicked.connect(self.reject)
