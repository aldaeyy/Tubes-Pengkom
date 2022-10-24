# TUGAS BESAR PENGENALAN KOMPUTASI
# KU1102-31

# COUNTING DAYS

# Kelompok 13
# 16722047 - Jessica Budiman
# 16722052 - Delon Khaerun Alief
# 16722117 - Yuba Felda Tustika
# 16722167 - Selpia Anggraeni Permatasari
# 16722292 - Maulida Rahma Britania

# Deskripsi: Program ini akan mengingatkan user untuk melakukan sesuatu

# KAMUS
# list_event : array of string

# class Event
class Event():
    def __init__(self, nomor, nama, tanggal, waktu, sisa, prioritas, lokasi, tags, deskripsi):
        self.nomor = nomor
        self.nama = nama
        self.tanggal = tanggal
        self.waktu = waktu
        self.sisa = sisa
        self.prioritas = prioritas
        self.lokasi = lokasi
        self.tags = tags
        self.deskripsi = deskripsi
    
    def __str__(self) -> str:
        print(f"EVENT KE-{self.nomor}")
        print("Nama     : ", self.nama)
        print("Tanggal  : ", self.tanggal)
        print("Waktu    : ", self.waktu)
        print("Sisa hari: ", self.sisa, "hari")
        print("Prioritas: ", self.prioritas)
        print("Lokasi   : ", self.lokasi)
        print("Tags     : ", self.tags)
        print("Deskripsi: ", self.deskripsi)
        print()
        return ""
        
def menu_utama():
    print("MENU UTAMA")
    print("1. Tambah Event")
    print("2. Lihat Event")
    print("3. Hapus Event")
    print("4. Ubah Event")
    print("5. Cari Event")
    print("6. Keluar\n")

def menu_ubah():
    print("1. Nama event")
    print("2. Tanggal event")
    print("3. Waktu event")
    print("4. Prioritas")
    print("5. Lokasi")
    print("6. Tags")
    print("7. Deskripsi\n")

def menu_cari():
    print("1. Cari berdasarkan nama")
    print("2. Cari berdasarkan tanggal")
    print("3. Cari berdasarkan prioritas")
    print("4. Cari berdasarkan tags")
    print("5. Kembali ke menu utama\n")

def tambah_event():
    global jumlah_event
    print("TAMBAH EVENT")
    nama = input("Masukkan nama event: ").upper()
    tanggal_event = int(input("Masukkan tanggal event: "))
    bulan_event = int(input("Masukkan bulan event: "))
    tahun_event = int(input("Masukkan tahun event: "))
    tanggal = datetime.date(tahun_event, bulan_event, tanggal_event).strftime("%A, %d %B %Y")
    pilihan = input("Apakah anda ingin menginputkan waktu event? (Y/N): ").lower()
    if pilihan == "y":
        jam_mulai = int(input("Masukkan jam mulai event: "))
        menit_mulai = int(input("Masukkan menit mulai event: "))
        waktu_mulai = datetime.time(jam_mulai, menit_mulai)
        jam_selesai = int(input("Masukkan jam selesai event: "))
        menit_selesai = int(input("Masukkan menit selesai event: "))
        waktu_selesai = datetime.time(jam_selesai, menit_selesai)
        waktu = f"{waktu_mulai} - {waktu_selesai}"
    else:
        waktu = "Seharian"
    
    sisa_hari = (datetime.date(tahun_event, bulan_event, tanggal_event) - datetime.date.today()).days
    event = Event(jumlah_event, nama, tanggal, waktu, sisa_hari, None, None, None, None)
    list_event.append(event)
    jumlah_event += 1
    print("Event berhasil ditambahkan!\n")

def lihat_event_hari_ini():
    print("LIHAT EVENT HARI INI")
    for event in list_event:
        if event.tanggal == datetime.date.today():
            print(event)

def lihat_event_besok():
    print("LIHAT EVENT BESOK")
    for event in list_event:
        if event.tanggal == datetime.date.today() + datetime.timedelta(days=1):
            print(event)

def lihat_event_minggu_ini():
    print("LIHAT EVENT MINGGU INI")
    for event in list_event:
        if event.tanggal >= datetime.date.today() and event.tanggal <= datetime.date.today() + datetime.timedelta(days=7):
            print(event)

def lihat_event_terlewat():
    print("LIHAT EVENT TERLEWAT")
    for event in list_event:
        if event.tanggal < datetime.date.today():
            print(event)

def lihat_semua_event():
    print("LIHAT SEMUA EVENT")
    for event in list_event:
        print(event)

def lihat_event():
    print("LIHAT EVENT")
    print("1. Lihat event hari ini")
    print("2. Lihat event besok")
    print("3. Lihat event minggu ini")
    print("4. Lihat event terlewat")
    print("5. Lihat semua event")
    print("6. Kembali\n")
    pilihan = int(input("Masukkan pilihan: "))
    if pilihan == 1:
        lihat_event_hari_ini()
    elif pilihan == 2:
        lihat_event_besok()
    elif pilihan == 3:
        lihat_event_minggu_ini()
    elif pilihan == 4:
        lihat_event_terlewat()
    elif pilihan == 5:
        lihat_semua_event()
    elif pilihan == 6:
        return
    else:
        print("Pilihan tidak valid!\n")

def hapus_event():
    print("HAPUS EVENT")
    lihat_semua_event()
    nomor_event = int(input("Masukkan nomor event yang ingin dihapus: "))
    print(list_event[nomor_event - 1])
    konfirmasi = input("Apakah anda yakin ingin menghapus event ini? (Y/N): ").lower()
    if konfirmasi == "y":
        list_event.pop(nomor_event)
        print("Event berhasil dihapus!\n")
    else:
        print("Event tidak jadi dihapus!\n")

def ubah_event():
    print("UBAH EVENT")
    lihat_semua_event()
    nomor_event = int(input("Masukkan nomor event yang ingin diubah: "))
    print(list_event[nomor_event - 1])
    menu_ubah()
    pilihan = int(input("Masukkan pilihan yang ingin diubah: "))
    if pilihan == 1:
        nama = input("Masukkan nama event: ").upper()
        list_event[nomor_event - 1].nama = nama
    elif pilihan == 2:
        tanggal_event = int(input("Masukkan tanggal event: "))
        bulan_event = int(input("Masukkan bulan event: "))
        tahun_event = int(input("Masukkan tahun event: "))
        sisa_hari = (datetime.date(tahun_event, bulan_event, tanggal_event) - datetime.date.today()).days
        tanggal = datetime.date(tahun_event, bulan_event, tanggal_event).strftime("%A, %d %B %Y")
        list_event[nomor_event - 1].sisa = sisa_hari
        list_event[nomor_event - 1].tanggal = tanggal
    elif pilihan == 3:
        pilihan2 = input("Apakah anda ingin menginputkan waktu event? (Y/N): ").lower()
        if pilihan2 == "y":
            jam_mulai = int(input("Masukkan jam mulai event: "))
            menit_mulai = int(input("Masukkan menit mulai event: "))
            waktu_mulai = datetime.time(jam_mulai, menit_mulai)
            jam_selesai = int(input("Masukkan jam selesai event: "))
            menit_selesai = int(input("Masukkan menit selesai event: "))
            waktu_selesai = datetime.time(jam_selesai, menit_selesai)
            waktu = f"{waktu_mulai} - {waktu_selesai}"
        else:
            waktu = "Seharian"
        list_event[nomor_event - 1].waktu = waktu
    elif pilihan == 4:
        pilihan2 = input("Ketik '1' untuk prioritas rendah, '2' untuk prioritas sedang, dan '3' untuk prioritas tinggi: ")
        if pilihan2 == "1":
            prioritas = "Rendah"
        elif pilihan2 == "2":
            prioritas = "Sedang"
        elif pilihan2 == "3":
            prioritas = "Tinggi"
        else:
            prioritas = None
        list_event[nomor_event - 1].prioritas = prioritas
    elif pilihan == 5:
        list_event[nomor_event - 1].lokasi = input("Masukkan lokasi event: ")
    elif pilihan == 6:
        list_event[nomor_event - 1].deskripsi = input("Masukkan deskripsi event: ")
    elif pilihan == 7:
        return
    else:
        print("Pilihan tidak valid!\n")
    print("Event berhasil diubah!\n")

def cari_event():
    print("CARI EVENT")
    lihat_semua_event()
    menu_cari()
    pilihan = input("Masukkan pilihan yang mau diubah")
    if pilihan == "1":
        nama = input("Masukkan nama event: ").upper()
        for event in list_event:
            if event.nama == nama:
                print(event)
    elif pilihan == "2":
        tanggal_event = int(input("Masukkan tanggal event: "))
        bulan_event = int(input("Masukkan bulan event: "))
        tahun_event = int(input("Masukkan tahun event: "))
        tanggal = datetime.date(tahun_event, bulan_event, tanggal_event).strftime("%A, %d %B %Y")
        for event in list_event:
            if event.tanggal == tanggal:
                print(event)
    elif pilihan == "3":
        prioritas = input("Ketik '1' untuk prioritas rendah, '2' untuk prioritas sedang, dan '3' untuk prioritas tinggi: ")
        if prioritas == "1":
            for event in list_event:
                if event.prioritas == "Rendah":
                    print(event)
        elif prioritas == "2":
            for event in list_event:
                if event.prioritas == "Sedang":
                    print(event)
        elif prioritas == "3":
            for event in list_event:
                if event.prioritas == "Tinggi":
                    print(event)
        else:
            print("Prioritas tidak valid!\n")

# ALGORITMA
import datetime
from locale import setlocale, LC_ALL

# inisialisasi lokasi agar program tahuan bahasa Indonesia
setlocale(LC_ALL, 'id_ID.utf8')

# Inisialisasi
list_event = []
jumlah_event = 1

while True:
    try:
        menu_utama()
        pilihan = int(input("Masukkan pilihan: "))
        if pilihan == 1:
            tambah_event()
        elif pilihan == 2:
            if jumlah_event == 1:
                print("Tidak ada event yang bisa dilihat!\n")
            else:
                lihat_event()
        elif pilihan == 3:
            if jumlah_event == 1:
                print("Tidak ada event yang bisa hapus!\n")
            else:
                hapus_event()
        elif pilihan == 4:
            if jumlah_event == 1:
                print("Tidak ada event yang bisa diubah!\n")
            else:
                ubah_event()
        elif pilihan == 5:
            if jumlah_event == 1:
                print("Tidak ada event yang bisa dicari!\n")
            else:
                cari_event()
        elif pilihan == 6:
            break
        else:
            print("Pilihan tidak valid!\n")
    except ValueError:
        print("Input tidak valid!\n")

print("Terima kasih telah menggunakan program ini!")