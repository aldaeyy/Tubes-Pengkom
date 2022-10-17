# TUGAS BESAR PENGENALAN KOMPUTASI
# KU1102-31

# Kelompok 13
# 16722047 - Jessica Budiman
# 16722052 - Delon Khaerun Alief
# 16722117 - Yuba Felda Tustika
# 16722167 - Selpia Anggraeni Permatasari
# 16722292 - Maulida Rahma Britania

# Deskripsi: Program ini akan mengingatkan user untuk melakukan sesuatu
# KAMUS
# event_reminder: list[str]
# event_reminder: list[list[str]]
# deskripsi_event: list[list[list[str]]]
# hari_ini: list[int]
# berhenti: boolean
# pilihan, index_list, index_hapus, index_ubah: int

# Fungsi-fungsi
# def pilihan_menu(): menampilkan pilihan menu
def pilihan_menu():
    print("Ketik '1' untuk menambah event reminder")
    print("Ketik '2' untuk melihat event reminder")
    print("Ketik '3' untuk menghapus event reminder")
    print("Ketik '4' untuk mengubah event reminder")
    print("Ketik '5' untuk keluar dari program\n")

# def menu_ubah(): menampilkan menu ubah
def menu_ubah():
        print("Ketik '1' untuk mengubah nama event reminder")
        print("Ketik '2' untuk menghapus event reminder")
        print("Ketik '3' untuk mengubah tanggal event reminder")
        print("Ketik '4' untuk mengubah jam event reminder")
        print("Ketik '4' untuk mengubah deskripsi event reminder")

# def tambah_event_reminder(): menambahkan reminder ke list
def tambah_event_reminder():
    global index_list
    nama_event = input("Masukkan nama list: ")
    tanggal_event = input("Masukkan tanggal event: ")
    bulan_event = input("Masukkan bulan event: ")
    tahun_event = input("Masukkan tahun event: ")
    tanggal = dt(tahun_event, bulan_event, tanggal_event)  # type: ignore
    event_reminder[index_list] = nama_event
    deskripsi_event[index_list][0] = tanggal  # type: ignore
    index_list += 1

def new_func():
    deskripsi_event[index_list][0]

# def tampilkan_event_reminder(): menampilkan list reminder
def tampilkan_event_reminder():
    for i in range(index_list):
        print(f"{i+1}. {event_reminder[i]}")
    print('')

# def hapus_event_reminder(): menghapus reminder dari list
def hapus_event_reminder():
    global index_hapus, index_list
    while index_hapus < 1 or index_hapus > 5:
        index_hapus = int(input("Masukkan nomor event yang ingin dihapus: "))
    print(f"Event yang akan dihapus: {event_reminder[index_hapus-1]}")
    konfirmasi = input("Apakah anda yakin? (Y/N): ").lower()
    if konfirmasi == "y":
        event_reminder[index_hapus-1] = ""
        print("Event berhasil dihapus\n")
        for i in range(index_hapus, index_list):
            event_reminder[i-1] = event_reminder[i]
        index_list -= 1
        event_reminder[index_list] = ""
    else:
        print("Event tidak jadi dihapus\n")

# def ubah_nama_event_reminder(): mengubah nama list reminder
def ubah_nama_event_reminder():
    global index_ubah
    index_ubah = int(input("Masukkan nomor list yang ingin diubah: "))
    nama_list_baru = input("Masukkan nama list baru: ")
    event_reminder[index_ubah-1] = nama_list_baru

# def tampilkan_reminder_hari_ini(): menampilkan reminder hari ini
def tampilkan_reminder_hari_ini():
    pass

# def tampilkan_reminder_bulan_ini(): menampilkan reminder bulan ini
def tampilkan_reminder_minggu_ini():
    pass

# def tampilkan_reminder_tahun_ini(): menampilkan reminder tahun ini
def tampilkan_reminder_bulan_ini():
    pass

# def tampilkan_reminder(): menampilkan reminder
def tampilkan_reminder():
    print(event_reminder)

# ALGORITMA
from datetime import date as dt

# Inisialisasi
event_reminder = ['']*10
deskripsi_event = [['']*7]*10
hari_ini = [0]*3
berhenti = False
index_list = index_hapus = index_ubah = index_event = 0
pilihan = pilihan_ubah = 0
hari_ini = dt.today()  # type: ignore

# Pembuka
print("Selamat datang di program reminder!")
print("Jumlah maksimal untuk event reminder adalah 10")

# Program utama
while not berhenti:
    pilihan_menu()
    pilihan = int(input("Masukkan pilihan: "))

    if pilihan == 1:
        if index_list < 5:
            tambah_event_reminder()
        else:
            print("Jumlah list sudah maksimal\n")
    if pilihan == 2:
        tampilkan_event_reminder()
    if pilihan == 3:
        hapus_event_reminder()
    if pilihan == 4:
        if index_list != 0:
            menu_ubah()
            pilihan_ubah = int(input("Masukkan pilihan: "))
            if pilihan_ubah == 1:
                tambah_event_reminder()
            if pilihan_ubah == 2:
                hapus_event_reminder()
            if pilihan_ubah == 3:
                pass
            if pilihan_ubah == 4:
                tampilkan_reminder()
                tampilkan_reminder_hari_ini()
                tampilkan_reminder_minggu_ini()
                tampilkan_reminder_bulan_ini()
            if pilihan_ubah == 5:
                ubah_nama_event_reminder()
            if pilihan_ubah == 6:
                pass
        else:
            print("Anda belum membuat list reminder!\n")
    if pilihan == 5:
        berhenti = True
