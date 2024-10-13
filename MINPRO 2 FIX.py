from prettytable import PrettyTable
import os
import sys
os.system ("cls")

data_tabel = [
    [1,"Camel","001","A"],
    [2,"Kiki","002","B"],
    [3,"Inoy","003","C"],
    [4,"Putra","004","A+"],
    [5,"Mai","005","B"],
    [6,"Dilla","006","B+"],
    [7,"Nayla","007","C"],
    [8,"Alief","008","E"],
    [9,"Bakugo","009","A++"]
]

def lihat_nilai(): 
    table = PrettyTable()
    table.field_names = ["Nomor","Nama Siswa","NISN","Nilai"]
    for item in data_tabel:
        table.add_row(item)
    print(table)

data_login_guru = {
    "Pak A": "ips",
    "Pak B": "ipa",
    "Pak C": "bhs"
}

data_login_murid = {
    "Alief": "alip",
    "Bakugo": "bkgalak",
    "Nayla": "nyl1",
    "Dilla": "dla",
    "Mai": "may",
    "Putra": "ptr",
    "Inoy": "iny",
    "Kiki": "kkk",
    "Camel": "cml"
}

def homepage():
    while True:
        print("=" * 10 + " Selamat Datang di Sistem Pembagian Nilai! " + "=" * 10)
        print("1. Login sebagai guru.")
        print("2. Login sebagai murid")
        pilihan = input("Silakan pilih mode login (1/2): ")
        
        if pilihan == "1":
            login_guru()
            break
        elif pilihan == "2":
            login_murid()
            break
        else:
            print("Mode Login tidak ada, silakan coba kembali!")

def login_guru():
    while True:
        username_guru = input("Masukkan username: ")
        password_guru = input("Masukkan password: ")
        
        if username_guru in data_login_guru and data_login_guru[username_guru] == password_guru:
            print("Selamat datang. Silahkan lanjut.")
            menu_guru()
            return
        else:
            print("Data salah. Coba lagi.")

def login_murid():
    while True:
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        
        if username in data_login_murid and data_login_murid[username] == password:
            print("Selamat datang. Silahkan lanjut.")
            menu_murid()
            return
        else:
            print("Data salah. Coba lagi.")

def menu_guru():
    while True:
        print("=" * 10 + " Selamat Datang, pengajar tangguh! " + "=" * 10)
        print("1. Tambah data nilai murid.")
        print("2. Lihat data nilai murid.")
        print("3. Ubah data nilai murid.")
        print("4. Hapus data nilai murid.")
        print("0. Logout.")
        fitur = input("Silakan pilih: ")
        if fitur == "1":
            tambah_nilai()
        elif fitur == "2":
            lihat_nilai()
        elif fitur == "3":
            ubah_nilai()
        elif fitur == "4":
            hapus_nilai()
        elif fitur == "0":
            mode_login = input ("Apakah anda ingin keluar (1) atau kembali (2)? (1/2) : ")
            if mode_login == "1":
                exit()
            elif mode_login == "2":
                menu_guru()
        else:
            print("Tidak ada fitur tersebut, coba yang lain!")

def menu_murid():
    while True:
        print("=" * 10 + " Selamat Datang, pelajar tangguh! " + "=" * 10)
        print("1. Lihat nilai murid.")
        print("2. Ajukan perubahan nilai.")
        print("0. Logout.")
        fitur = input("Silakan pilih: ")
        if fitur == "1":
            lihat_nilai()
        elif fitur == "2":
            ajuan()
        elif fitur == "0":
            mode_login = input ("Apakah anda ingin keluar (1) atau kembali (2)? (1/2) : ")
            if mode_login == "1":
                exit()
            elif mode_login == "2":
                menu_murid()
        else:
            print("Tidak ada fitur tersebut, coba yang lain!")

def tambah_nilai():
    nama_siswa = input('Masukkan nama siswa: ')
    nisn = input('Masukkan NISN siswa: ')
    nilaii = input('Masukkan nilai siswa: ')
    for user in data_tabel:
        if user[1] == nama_siswa:
            print('Data sudah ada!')
            return
    nama_baru = len(data_tabel) + 1
    data_tabel.append([nama_baru, nama_siswa, nisn, nilaii])
    print('Data siswa berhasil ditambahkan.')

def ubah_nilai():
    update = str(input("Masukkan nama siswa yang mau diubah: "))
    for i in range(len(data_tabel)): 
        if data_tabel[i][1] == update:
            nama_baru = input("Masukkan nama siswa yang baru: ")
            nisn_baru = input("Masukkan NISN siswa yang baru: ")
            nilai_baru = input("Masukkan nilai yang baru: ")
            data_tabel[i][1] = nama_baru
            data_tabel[i][2] = nisn_baru
            data_tabel[i][3] = nilai_baru
            lihat_nilai()
            print("Berhasil mengubah data siswa.")
            break
    else:
        print("Nama tidak ditemukan, masukkan data yang benar.")
        ubah_nilai()

def hapus_nilai():
    hapus = input("Masukkan nama siswa yang ingin dihapus: ")
    for i, siswa in enumerate(data_tabel):
        if siswa[1] == hapus:  
            del data_tabel[i]
            print(f"Data siswa {hapus} berhasil dihapus.")
            lihat_nilai()

def ajuan():
    print("Anda akan mengajukan perubahan nilai. Silahkan isi data diri dan alasan.")
    nama_ajuan = input("Nama: ")
    kelas_ajuan = input("Kelas: ")
    alasan_ajuan = input("Alasan: ")
    print("Pengajuan telah terkirim. Tunggu informasi selanjutnya.")
    mode_login = input("Apakah anda ingin keluar (1) atau kembali (2)? (1/2) : ")
    if mode_login == "1":
        exit()
    elif mode_login == "2":
        menu_murid()

def exit():
    print("Terima kasih sudah berkunjung!")
    raise SystemExit

homepage()