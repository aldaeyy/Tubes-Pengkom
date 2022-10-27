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
# jumlah_event : integer
# pilihan : integer

# class Event
class Event():
    # constructor
    def __init__(self, nomor, nama, tanggal, waktu, sisa, prioritas, lokasi, tags, deskripsi, status):
        self.nomor = nomor
        self.nama = nama
        self.tanggal = tanggal
        self.waktu = waktu
        self.sisa = sisa
        self.prioritas = prioritas
        self.lokasi = lokasi
        self.tags = tags
        self.deskripsi = deskripsi
        self.status = status
    
    # getter
    def __str__(self) -> str:
        return  f"""EVENT KE-{self.nomor}
Nama     : {self.nama}
Tanggal  : {self.tanggal}
Waktu    : {self.waktu}
Sisa     : {self.sisa} hari
Prioritas: {self.prioritas}
Lokasi   : {self.lokasi}
Tags     : {self.tags}
Deskripsi: {self.deskripsi}
"""
        
# definisi menu utama
def menu_utama():
    # menampilkan menu utama

    # KAMUS LOKAL
    # tidak tersedia

    print("MENU UTAMA")
    print("1. Tambah Event")
    print("2. Lihat Event")
    print("3. Hapus Event")
    print("4. Ubah Event")
    print("5. Cari Event")
    print("6. Keluar\n")

# definisi menu lihat
def menu_lihat():
    # menampilkan menu lihat

    # KAMUS LOKAL
    # tidak tersedia

    print("1. Lihat event hari ini")
    print("2. Lihat event besok")
    print("3. Lihat event minggu ini")
    print("4. Lihat event terlewat")
    print("5. Lihat semua event")
    print("6. Kembali\n")

# definisi menu ubah
def menu_ubah():
    # menampilkan menu ubah

    # KAMUS LOKAL
    # tidak tersedia

    print("1. Nama event")
    print("2. Tanggal event")
    print("3. Waktu event")
    print("4. Prioritas")
    print("5. Lokasi")
    print("6. Tags")
    print("7. Deskripsi\n")

# definisi menu cari
def menu_cari():
    # menampilkan menu cari

    # KAMUS LOKAL
    # tidak tersedia

    print("1. Cari berdasarkan nama")
    print("2. Cari berdasarkan tanggal")
    print("3. Cari berdasarkan prioritas")
    print("4. Cari berdasarkan tags")
    print("5. Kembali ke menu utama\n")

# definisi tambah event
def tambah_event():
    # menambahkan event ke list_event

    # KAMUS LOKAL
    # nama, tanggal_input, pilihan, pilihan2, waktu, tanggal, waktu_akhir : string
    # sisa_hari : integer
    # event : Event

    global jumlah_event
    print("TAMBAH EVENT")
    nama = input("Masukkan nama event: ").upper()
    tanggal_input = input("Masukkan tanggal event (DD/MM/YYYY): ")
    tanggal_input = tanggal_input.split("/")  # memisahkan tanggal, bulan, dan tahun
    tanggal_input = list(map(int, tanggal_input))  # mengubah string menjadi integer
    tanggal = datetime.date(tanggal_input[2], tanggal_input[1], tanggal_input[0]).strftime("%A, %d %B %Y")  # mengubah format tanggal
    pilihan = input("Apakah Anda ingin menginputkan waktu event? (Y/N): ").lower()
    if pilihan == "y":
        waktu = input("Masukkan waktu event (HH:MM): ")
        waktu = waktu.split(":")  # memisahkan jam dan menit
        waktu = list(map(int, waktu))  # mengubah string menjadi integer
        waktu = datetime.time(waktu[0], waktu[1]).strftime("%H:%M")  # mengubah format waktu
        pilihan2 = input("Apakah Anda ingin menambahkan waktu berakhir event? (Y/N): ").lower()
        if pilihan2 == "y":
            waktu_akhir = input("Masukkan waktu berakhir event (HH:MM): ")
            waktu_akhir = waktu_akhir.split(":")
            waktu_akhir = list(map(int, waktu_akhir))
            waktu_akhir = datetime.time(waktu_akhir[0], waktu_akhir[1]).strftime("%H:%M")
            waktu = waktu + ' - ' + waktu_akhir
    else:
        waktu = "Seharian"
    
    sisa_hari = datetime.date(tanggal_input[2], tanggal_input[1], tanggal_input[0]) - datetime.date.today()  # menghitung sisa hari
    sisa_hari = sisa_hari.days  # mengubah timedelta menjadi integer
    event = Event(jumlah_event + 1, nama, tanggal, waktu, sisa_hari, None, None, None, None, False)  # membuat objek event
    list_event.append(event)  # menambahkan objek event ke list_event
    jumlah_event += 1  # menambah jumlah event
    print("Event berhasil ditambahkan!\n")

# definisi lihat event hari ini
def lihat_event_hari_ini():
    # menampilkan event hari ini

    # KAMUS LOKAL
    # ada : integer

    ada = 0
    print("LIHAT EVENT HARI INI")
    for event in list_event:
        if event.sisa == 0:
            ada += 1
            print(event)
    
    if ada == 0:
        print("Tidak ada event hari ini\n")

# definisi lihat event besok
def lihat_event_besok():
    # menampilkan event besok

    # KAMUS LOKAL
    # ada : integer

    ada = 0
    print("LIHAT EVENT BESOK")
    for event in list_event:
        if event.sisa == 1:
            ada += 1
            print(event)
    
    if ada == 0:
        print("Tidak ada event besok\n")

# definisi lihat event minggu ini
def lihat_event_minggu_ini():
    # menampilkan event minggu ini

    # KAMUS LOKAL
    # ada : integer

    ada = 0
    print("LIHAT EVENT MINGGU INI")
    for event in list_event:
        if 0 <= event.sisa <= 7:
            ada += 1
            print(event)
    
    if ada == 0:
        print("Tidak ada event minggu ini\n")

# definisi lihat event terlewat
def lihat_event_terlewat():
    # menampilkan event terlewat

    # KAMUS LOKAL
    # ada : integer

    ada = 0
    print("LIHAT EVENT TERLEWAT")
    for event in list_event:
        if event.sisa < 0:
            ada += 1
            print(event)
    
    if ada == 0:
        print("Tidak ada event terlewat\n")

# definisi lihat semua event
def lihat_semua_event():
    # menampilkan semua event

    # KAMUS LOKAL
    # tidak tersedia

    print("LIHAT SEMUA EVENT")
    for event in list_event:
        print(event)

# definisi lihat event
def lihat_event():
    # melihat event

    # KAMUS LOKAL
    # pilihan : string

    while True:
        print("LIHAT EVENT")
        menu_lihat()
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
            break
        else:
            print("Pilihan tidak valid!\n")

# definisi cari event
def hapus_event():
    # menghapus event

    # KAMUS LOKAL
    # pilihan : string
    # nomor_event : integer
    # konfirmasi : string

    global jumlah_event
    print("HAPUS EVENT")
    lihat_semua_event()
    nomor_event = int(input("Masukkan nomor event yang ingin dihapus ('0' untuk batal hapus event): "))
    if nomor_event == 0:
        print("Batal hapus event\n")
    else:
        print(list_event[nomor_event - 1])  # menampilkan event yang akan dihapus
        konfirmasi = input("Apakah anda yakin ingin menghapus event ini? (Y/N): ").lower()  # konfirmasi hapus event
        if konfirmasi == "y":
            list_event.pop(nomor_event - 1)  # menghapus event
            for i in range(nomor_event - 1, jumlah_event - 1):  # mengubah nomor event
                list_event[i].nomor -= 1  # mengurangi nomor event
            print("Event berhasil dihapus!\n")
            jumlah_event -= 1
        else:  # batal hapus event
            print("Event tidak jadi dihapus!\n")

# definisi cari event
def ubah_event():
    # mengubah event

    # KAMUS LOKAL
    # nomor_event, sisa_hari : integer
    # nama, tanggal_input, pilihan, pilihan2, waktu, tanggal, waktu_akhir, prioritas : string

    print("UBAH EVENT")
    while True:
        lihat_semua_event()
        nomor_event = int(input("Masukkan nomor event yang ingin diubah ('0' untuk kembali ke menu utama): "))
        if nomor_event == 0:
            break
        else:
            print(list_event[nomor_event - 1])
            menu_ubah()
            pilihan = int(input("Masukkan pilihan yang ingin diubah: "))
            if pilihan == 1:
                nama = input("Masukkan nama event: ").upper()
                list_event[nomor_event - 1].nama = nama
            elif pilihan == 2:
                tanggal_input = input("Masukkan tanggal event (DD/MM/YYYY): ")  # input tanggal event
                tanggal_input = tanggal_input.split("/")  # memisahkan tanggal, bulan, dan tahun
                tanggal_input = list(map(int, tanggal_input))  # mengubah tanggal, bulan, dan tahun menjadi integer
                tanggal = datetime.date(tanggal_input[2], tanggal_input[1], tanggal_input[0]).strftime("%A, %d %B %Y")  # mengubah tanggal, bulan, dan tahun menjadi format hari, tanggal bulan tahun
                sisa_hari = datetime.date(tanggal_input[2], tanggal_input[1], tanggal_input[0]) - datetime.date.today()  # menghitung sisa hari
                sisa_hari = sisa_hari.days  # mengubah sisa hari menjadi integer
                list_event[nomor_event - 1].sisa = sisa_hari  # mengubah sisa hari
                list_event[nomor_event - 1].tanggal = tanggal  # mengubah tanggal
                list_event[nomor_event - 1].status = False  # mengubah status
            elif pilihan == 3:
                pilihan2 = input("Apakah anda ingin menginputkan waktu event? (Y/N): ").lower()
                if pilihan2 == "y":
                    waktu = input("Masukkan waktu event (HH:MM): ")  # input waktu event
                    waktu = waktu.split(":")  # memisahkan jam dan menit
                    waktu = list(map(int, waktu))  # mengubah jam dan menit menjadi integer
                    waktu = datetime.time(waktu[0], waktu[1]).strftime("%H:%M")  # mengubah jam dan menit menjadi format jam:menit
                    pilihan2 = input("Apakah Anda ingin menambahkan waktu berakhir event? (Y/N): ").lower()
                    if pilihan2 == "y":
                        waktu_akhir = input("Masukkan waktu berakhir event (HH:MM): ")
                        waktu_akhir = waktu_akhir.split(":")
                        waktu_akhir = list(map(int, waktu_akhir))
                        waktu_akhir = datetime.time(waktu_akhir[0], waktu_akhir[1]).strftime("%H:%M")
                        waktu = waktu + ' - ' + waktu_akhir
                else:
                    waktu = "Seharian"
                list_event[nomor_event - 1].waktu = waktu  # mengubah waktu
                list_event[nomor_event - 1].status = False  # mengubah status
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
                list_event[nomor_event - 1].tags = input("Masukkan tags event: ")
            elif pilihan == 7:
                list_event[nomor_event - 1].deskripsi = input("Masukkan deskripsi event: ")
            elif pilihan == 8:
                break
            else:
                print("Pilihan tidak valid!\n")  # pilihan tidak valid
            print("Event berhasil diubah!\n")  # event berhasil diubah

# definisi cari event
def cari_event():
    # mencari event

    # KAMUS LOKAL
    # pilihan, nama, tanggal_input, tanggal, prioritas, tags : string
    # ada : integer

    print("CARI EVENT")
    while True:            
        menu_cari()
        pilihan = input("Masukkan pilihan: ")
        ada = 0  # variabel untuk mengecek apakah ada event yang sesuai dengan pencarian
        if pilihan == "1":
            nama = input("Masukkan nama event: ").upper()
            for event in list_event:  # mencari event yang sesuai dengan nama
                if event.nama == nama:
                    ada += 1
                    print(event)
            if ada == 0:
                print("Tidak ada event dengan nama tersebut!\n")
        elif pilihan == "2":
            tanggal_input = input("Masukkan tanggal event (DD/MM/YYYY): ")
            tanggal_input = tanggal_input.split("/")
            tanggal_input = list(map(int, tanggal_input))
            tanggal = datetime.date(tanggal_input[2], tanggal_input[1], tanggal_input[0]).strftime("%A, %d %B %Y")
            for event in list_event:  # mencari event yang sesuai dengan tanggal
                if event.tanggal == tanggal:
                    ada += 1
                    print(event)
            if ada == 0:
                print("Tidak ada event dengan tanggal tersebut!\n")
        elif pilihan == "3":
            prioritas = input("Ketik '1' untuk prioritas rendah, '2' untuk prioritas sedang, dan '3' untuk prioritas tinggi: ")
            if prioritas == "1":
                for event in list_event:
                    if event.prioritas == "Rendah":
                        ada += 1
                        print(event)
            elif prioritas == "2":
                for event in list_event:
                    if event.prioritas == "Sedang":
                        ada += 1
                        print(event)
            elif prioritas == "3":
                for event in list_event:
                    if event.prioritas == "Tinggi":
                        ada += 1
                        print(event)
            else:
                print("Prioritas tidak valid!\n")
            if ada == 0:
                print("Tidak ada event dengan prioritas tersebut!\n")
        elif pilihan == "4":
            tags = input("Masukkan tags event: ")
            for event in list_event:
                if event.tags == tags:
                    ada += 1
                    print(event)
            if ada == 0:
                print("Tidak ada event dengan tags tersebut!\n")
        elif pilihan == "5":
            break
        else:
            print("Pilihan tidak valid!\n")

# definisi cek notifikasi
def cek_notifikasi():
    # menampilkan notifikasi

    # KAMUS LOKAL
    # tidak tersedia

    for event in list_event:  # mengecek apakah ada event yang belum selesai
        if event.tanggal == datetime.date.today().strftime("%A, %d %B %Y") and event.waktu == "Seharian" and event.status == False:
            event.status = True  # mengubah status menjadi selesai
            notification.notify(
                title = event.nama,  # judul notifikasi
                message = f"Event {event.nama} hari ini!",  # isi notifikasi
                app_icon = None,  # ikon notifikasi
                timeout = 10  # durasi notifikasi
            )  # type: ignore
        elif event.tanggal == datetime.date.today().strftime("%A, %d %B %Y") and event.waktu == datetime.datetime.now().strftime("%H:%M") and event.status == False:
            event.status = True  # mengubah status menjadi selesai
            notification.notify(
                title = event.nama,  # judul notifikasi
                message = f"Event {event.nama} hari ini!",  # isi notifikasi
                app_icon = None,  # ikon notifikasi
                timeout = 10  # durasi notifikasi
            )  # type: ignore


# ALGORITMA
# import library
import datetime  # untuk mengakses tanggal dan waktu
from locale import setlocale, LC_ALL  # untuk mengatur bahasa
from plyer import notification  # untuk mengakses notifikasi
import shelve  # untuk menyimpan event

setlocale(LC_ALL, 'id_ID.utf8')  # mengatur bahasa menjadi Indonesia

# Inisialisasi
list_event = []
jumlah_event = 0
pilihan = str()

# pembuka
print("Welcome to Counting Days!")
print("Silahkan memasukkan event yang ingin Anda ingatkan\n")

# program utama
while True:
    shelve_event = shelve.open("event")  # membuka file event
    jumlah_event = len(shelve_event)  # menghitung jumlah event
    list_event = list(shelve_event.values())  # mengubah event menjadi list
    try:
        menu_utama()  # menampilkan menu utama
        pilihan = int(input("Masukkan pilihan: "))
        if pilihan == 1:
            tambah_event()
        elif pilihan == 2:
            if jumlah_event == 0:
                print("Tidak ada event yang bisa dilihat!\n")
            else:
                lihat_event()
        elif pilihan == 3:
            if jumlah_event == 0:
                print("Tidak ada event yang bisa hapus!\n")
            else:
                hapus_event()
        elif pilihan == 4:
            if jumlah_event == 0:
                print("Tidak ada event yang bisa diubah!\n")
            else:
                ubah_event()
        elif pilihan == 5:
            if jumlah_event == 0:
                print("Tidak ada event yang bisa dicari!\n")
            else:
                cari_event()
        elif pilihan == 6:
            break
        else:
            print("Pilihan tidak valid!\n")
    except:
        print("Input tidak valid!\n")

    if jumlah_event > 0:  # mengecek apakah ada event yang tersimpan
        cek_notifikasi()  # menampilkan notifikasi
        shelve_event = shelve.open("event")  # membuka file event
        shelve_event.clear()  # menghapus semua event yang tersimpan
        for event in list_event:  # menambahkan event ke dictionary
            shelve_event[event.nama] = event
    shelve_event.close()  # menutup file event

# penutup
print("Terima kasih telah menggunakan program ini!")
input("Tekan enter untuk keluar...")