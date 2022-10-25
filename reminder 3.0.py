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
from ast import Str


class Event():
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
        return ""
        
def menu_utama():
    print("MENU UTAMA")
    print("1. Tambah Event")
    print("2. Lihat Event")
    print("3. Hapus Event")
    print("4. Ubah Event")
    print("5. Cari Event")
    print("6. Keluar\n")

def menu_lihat():
    print("1. Lihat event hari ini")
    print("2. Lihat event besok")
    print("3. Lihat event minggu ini")
    print("4. Lihat event terlewat")
    print("5. Lihat semua event")
    print("6. Kembali\n")

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
    tanggal_input = input("Masukkan tanggal event (DD/MM/YYYY): ")
    tanggal_input = tanggal_input.split("/")
    tanggal_input = list(map(int, tanggal_input))
    tanggal = datetime.date(tanggal_input[2], tanggal_input[1], tanggal_input[0]).strftime("%A, %d %B %Y")
    pilihan = input("Apakah Anda ingin menginputkan waktu event? (Y/N): ").lower()
    if pilihan == "y":
        waktu = input("Masukkan waktu event (HH:MM): ")
        waktu = waktu.split(":")
        waktu = list(map(int, waktu))
        waktu = datetime.time(waktu[0], waktu[1]).strftime("%H:%M")
        pilihan2 = input("Apakah Anda ingin menambahkan waktu berakhir event? (Y/N): ").lower()
        if pilihan2 == "y":
            waktu_akhir = input("Masukkan waktu berakhir event (HH:MM): ")
            waktu_akhir = waktu_akhir.split(":")
            waktu_akhir = list(map(int, waktu_akhir))
            waktu_akhir = datetime.time(waktu_akhir[0], waktu_akhir[1]).strftime("%H:%M")
            waktu = waktu + ' - ' + waktu_akhir
    else:
        waktu = "Seharian"
    
    sisa_hari = datetime.date(tanggal_input[2], tanggal_input[1], tanggal_input[0]) - datetime.date.today()
    sisa_hari = sisa_hari.days
    event = Event(jumlah_event + 1, nama, tanggal, waktu, sisa_hari, None, None, None, None, False)
    list_event.append(event)
    jumlah_event += 1
    print("Event berhasil ditambahkan!\n")

def lihat_event_hari_ini():
    ada = 0
    print("LIHAT EVENT HARI INI")
    for event in list_event:
        if event.sisa == 0:
            ada += 1
            print(event)
    
    if ada == 0:
        print("Tidak ada event hari ini\n")

def lihat_event_besok():
    ada = 0
    print("LIHAT EVENT BESOK")
    for event in list_event:
        if event.sisa == 1:
            ada += 1
            print(event)
    
    if ada == 0:
        print("Tidak ada event besok\n")

def lihat_event_minggu_ini():
    ada = 0
    print("LIHAT EVENT MINGGU INI")
    for event in list_event:
        if 0 <= event.sisa <= 7:
            ada += 1
            print(event)
    
    if ada == 0:
        print("Tidak ada event minggu ini\n")

def lihat_event_terlewat():
    ada = 0
    print("LIHAT EVENT TERLEWAT")
    for event in list_event:
        if event.sisa < 0:
            ada += 1
            print(event)
    
    if ada == 0:
        print("Tidak ada event terlewat\n")

def lihat_semua_event():
    print("LIHAT SEMUA EVENT")
    for event in list_event:
        print(event)

def lihat_event():
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

def hapus_event():
    global jumlah_event
    print("HAPUS EVENT")
    lihat_semua_event()
    nomor_event = int(input("Masukkan nomor event yang ingin dihapus ('0' untuk batal hapus event): "))
    if nomor_event == 0:
        print("Batal hapus event\n")
    else:
        print(list_event[nomor_event - 1])
        konfirmasi = input("Apakah anda yakin ingin menghapus event ini? (Y/N): ").lower()
        if konfirmasi == "y":
            list_event.pop(nomor_event - 1)
            for i in range(nomor_event - 1, jumlah_event - 1):
                list_event[i].nomor -= 1
            print("Event berhasil dihapus!\n")
            jumlah_event -= 1
        else:
            print("Event tidak jadi dihapus!\n")

def ubah_event():
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
                tanggal_input = input("Masukkan tanggal event (DD/MM/YYYY): ")
                tanggal_input = tanggal_input.split("/")
                tanggal_input = list(map(int, tanggal_input))
                tanggal = datetime.date(tanggal_input[2], tanggal_input[1], tanggal_input[0]).strftime("%A, %d %B %Y")
                sisa_hari = datetime.date(tanggal_input[2], tanggal_input[1], tanggal_input[0]) - datetime.date.today()
                sisa_hari = sisa_hari.days
                list_event[nomor_event - 1].sisa = sisa_hari
                list_event[nomor_event - 1].tanggal = tanggal
            elif pilihan == 3:
                pilihan2 = input("Apakah anda ingin menginputkan waktu event? (Y/N): ").lower()
                if pilihan2 == "y":
                    waktu = input("Masukkan waktu event (HH:MM): ")
                    waktu = waktu.split(":")
                    waktu = list(map(int, waktu))
                    waktu = datetime.time(waktu[0], waktu[1]).strftime("%H:%M")
                    pilihan2 = input("Apakah Anda ingin menambahkan waktu berakhir event? (Y/N): ").lower()
                    if pilihan2 == "y":
                        waktu_akhir = input("Masukkan waktu berakhir event (HH:MM): ")
                        waktu_akhir = waktu_akhir.split(":")
                        waktu_akhir = list(map(int, waktu_akhir))
                        waktu_akhir = datetime.time(waktu_akhir[0], waktu_akhir[1]).strftime("%H:%M")
                        waktu = waktu + ' - ' + waktu_akhir
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
                list_event[nomor_event - 1].tags = input("Masukkan tags event: ")
            elif pilihan == 7:
                list_event[nomor_event - 1].deskripsi = input("Masukkan deskripsi event: ")
            elif pilihan == 8:
                break
            else:
                print("Pilihan tidak valid!\n")
            print("Event berhasil diubah!\n")

def cari_event():
    print("CARI EVENT")
    while True:            
        menu_cari()
        pilihan = input("Masukkan pilihan: ")
        ada = 0
        if pilihan == "1":
            nama = input("Masukkan nama event: ").upper()
            for event in list_event:
                if event.nama == nama:
                    ada += 1
                    print(event)
            if ada == 0:
                print("Tidak ada event dengan nama tersebut!\n")
        elif pilihan == "2":
            tanggal_event = int(input("Masukkan tanggal event (DD): "))
            bulan_event = int(input("Masukkan bulan event (MM): "))
            tahun_event = int(input("Masukkan tahun event (YYYY): "))
            tanggal = datetime.date(tahun_event, bulan_event, tanggal_event).strftime("%A, %d %B %Y")
            for event in list_event:
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

def notifikasi():
    for event in list_event:
        if event.tanggal == datetime.date.today().strftime("%A, %d %B %Y") and event.waktu == "Seharian" and event.status == False:
            event.status = True
            notification.notify(
                title = event.nama,
                message = f"Event {event.nama} hari ini!",
                app_icon = None,
                timeout = 10
            )  # type: ignore
        elif event.tanggal == datetime.date.today().strftime("%A, %d %B %Y") and event.waktu == datetime.datetime.now().strftime("%H:%M") and event.status == False:
            event.status = True
            notification.notify(
                title = event.nama,
                message = f"Event {event.nama} hari ini!",
                app_icon = None,
                timeout = 10
            )  # type: ignore


# ALGORITMA
import datetime
from locale import setlocale, LC_ALL
from plyer import notification

# inisialisasi lokasi agar program tahuan bahasa Indonesia
setlocale(LC_ALL, 'id_ID.utf8')


# Inisialisasi
list_event = []
jumlah_event = 0

# pembuka
print("Welcome to Counting Days!")
print("Silahkan memasukkan event yang ingin Anda ingatkan\n")

# program utama
while True:
    try:
        menu_utama()
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

    if jumlah_event > 0:
        notifikasi()

print("Terima kasih telah menggunakan program ini!")
input("Tekan enter untuk keluar...")