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
# event : array of string
# tanggal : array of datetime
# jam : array of string
# index_event : integer
# nomor = integer
# ubah = integer
# keterangan_event : array of array of string
# jam_mulai, menit_mulai, jam_selesai, menit_selesai = integer
# nama, prioritas, lokasi, tags, deskripsi : string
# tanggal_event, bulan_event, tahun_event : integer

# def tambah_event(): menambahkan event
def tambah_event():
    global index_event
    try:
        nama = input("Masukkan nama event: ").upper()
        tanggal_event = int(input("Masukkan tanggal event: "))
        bulan_event = int(input("Masukkan bulan event: "))
        tahun_event = int(input("Masukkan tahun event: "))
        event[index_event] = nama  # menambahkan nama event
        tanggal[index_event] = dt(tahun_event, bulan_event, tanggal_event)  # menambahkan tanggal event
        pilihan = input("Ketik 'y' jika ingin menambah waktu spesifik: ")
        if pilihan == 'y':  # menambahkan waktu event
            jam_mulai = int(input("Masukkan jam mulai: "))
            menit_mulai = int(input("Masukkan menit mulai: "))
            jam_selesai = int(input("Masukkan jam selesai: "))
            menit_selesai = int(input("Masukkan menit selesai: "))
            mulai = tm(jam_mulai, menit_mulai)  # menambahkan waktu mulai event
            selesai = tm(jam_selesai, menit_selesai)  # menambahkan waktu selesai event
            jam[index_event] = mulai.strftime("%H:%M") + " - " + selesai.strftime("%H:%M")  # type: ignore  # menambahkan waktu event
        else:  # jika tidak menambahkan waktu event
            jam[index_event] = "Seharian"  # type: ignore
        print("Event berhasil ditambahkan\n")
        index_event += 1  # menambahkan index event
    except ValueError:
        print("Input yang dimasukkan tidak valid\n")

# def tampilan(): menampilkan event
def tampilan(i, nomor):
    print(f"EVENT KE-{nomor}")
    print("Nama Event       :", event[i])
    print("Tanggal Event    :", tanggal[i].strftime("%d %B %Y"))
    print("Waktu event      :", jam[i])
    print("Sisa hari        :", (tanggal[i] - dt.today()).days, "hari")
    print("Prioritas        :", keterangan_event[i][0])
    print("Lokasi           :", keterangan_event[i][1])
    print("Tags             :", keterangan_event[i][2])
    print("Deskripsi        :", keterangan_event[i][3])
    print('')

# def lihat_event_hari_ini(): menampilkan event hari ini
def lihat_event_hari_ini():
    global index_event, nomor
    if index_event == 0:
        print("Tidak ada event\n")
    else:
        for i in range(index_event):
            if tanggal[i].strftime("%d %b %Y") == dt.today().strftime("%d %b %Y"):  # type: ignore  # menampilkan event hari ini
                tampilan(i, nomor)  
                nomor += 1  
    if nomor == 1:
        print("Tidak ada event hari ini\n")
    nomor = 1  # mengembalikan jumlah event ke 1

# def lihat_event_besok(): menampilkan event besok
def lihat_event_besok():
    global index_event, nomor
    if index_event == 0:
        print("Tidak ada event\n")
    else:
        for i in range(index_event):
            if (tanggal[i] - dt.today()).days == 1:
                tampilan(i, nomor)
                nomor += 1
    if nomor == 1:
        print("Tidak ada event besok\n")
    nomor = 1  # mengembalikan jumlah event ke 1

# def lihat_event_seminggu(): menampilkan event selama seminggu
def lihat_event_seminggu():
    global index_event, nomor
    if index_event == 0:
        print("Tidak ada event\n")
    else:
        for i in range(index_event):
            if (tanggal[i] - dt.today()).days <= 7:
                tampilan(i, nomor)
                nomor += 1
    if nomor == 1:
        print("Tidak ada event selama seminggu\n")
    nomor = 1  # mengembalikan jumlah event ke 1

# def lihat_event_terlewat(): menampilkan event yang terlewat
def lihat_event_terlewat():
    global index_event, nomor
    if index_event == 0:
        print("Tidak ada event\n")
    else:
        for i in range(index_event):
            if (tanggal[i] - dt.today()).days < 0:
                tampilan(i, nomor)
                nomor += 1
    if nomor == 1:
        print("Tidak ada event yang terlewat\n")
    nomor = 1  # mengembalikan jumlah event ke 1

# def lihat_semua_event(): menampilkan event
def lihat_semua_event():
    global index_event, nomor
    if index_event == 0:
        print("Tidak ada event\n")
    else:
        for i in range(index_event):
            tampilan(i, nomor)
            nomor += 1
    nomor = 1  # mengembalikan jumlah event ke 1
    
# def lihat_event(): menampilkan event
def lihat_event():
    while True:
        print("MENU LIHAT EVENT")
        print("1. Lihat Event Hari Ini")
        print("2. Lihat Event Besok")
        print("3. Lihat Event Seminggu")
        print("4. Lihat Event Terlewat")
        print("5. Lihat Semua Event")
        print("6. Kembali\n")
        print("Pilih menu: ", end="")
        try:
            menu = int(input())
        except ValueError:
            print("Input yang dimasukkan tidak valid\n")
            menu = 0
        if menu == 1:
            lihat_event_hari_ini()
        elif menu == 2:
            lihat_event_besok()
        elif menu == 3:
            lihat_event_seminggu()
        elif menu == 4:
            lihat_event_terlewat()
        elif menu == 5:
            lihat_semua_event()
        elif menu == 6:
            break
        else:
            print("Menu tidak tersedia\n")

# def hapus_event(): menghapus event
def hapus_event():
    global index_event
    if index_event == 0:  
        print("Tidak ada event\n")
    else:
        for i in range(index_event):
            tampilan(i, i+1)  # menampilkan event
        try:
            hapus = int(input("Masukkan nomor event yang ingin dihapus: "))
            if hapus > index_event or hapus < 1:  # jika nomor event tidak valid
                print("Nomor event tidak ada\n")
            else:  # jika nomor event valid
                print("Event yang akan dihapus:")
                tampilan(hapus-1, hapus)
                konfirmasi = input("Apakah anda yakin ingin menghapus event ini? (y/n): ").lower()  # konfirmasi
                if konfirmasi == "y":  # jika konfirmasi y
                    for i in range(hapus-1, index_event-1):  # menggeser event
                        event[i] = event[i+1]
                        tanggal[i] = tanggal[i+1]
                        jam[i] = jam[i+1]
                        for j in range(4):  # menggeser keterangan event
                            keterangan_event[i][j] = keterangan_event[i+1][j]
                    index_event -= 1  # mengurangi jumlah event
                    print("Event berhasil dihapus\n")  
                elif konfirmasi == "n":
                    print("Event tidak dihapus\n")
                else:
                    print("Input yang dimasukkan tidak valid\n")
        except ValueError:
            print("Input yang dimasukkan tidak valid\n")

# def ubah_event(): mengubah event
def ubah_event():
    global index_event
    if index_event == 0:  # jika tidak ada event
        print("Tidak ada event\n")
    else:  # jika ada event
        while True:
            for i in range(index_event):  # menampilkan event
                tampilan(i, i+1)  
            try:  # memasukkan nomor event yang ingin diubah
                ubah = int(input("Masukkan nomor event yang ingin diubah ('0' untuk kembali ke menu utama): "))
                if ubah > index_event or ubah < 0:  # jika nomor event tidak ada
                    print("Nomor event tidak ada\n")
                elif ubah == 0:  # jika nomor event 0
                    break
                else:
                    print("1. Nama event")
                    print("2. Tanggal event")
                    print("3. Prioritas")
                    print("4. Lokasi")
                    print("5. Tags")
                    print("6. Deskripsi\n")
                    print("Pilih menu: ", end="")
                    try:  # memasukkan menu yang ingin diubah
                        menu = int(input())
                    except ValueError:
                        print("Input yang dimasukkan tidak valid\n")
                        menu = 0
                    if menu == 1:  # mengubah nama event
                        nama = input("Masukkan nama event: ").upper()
                        event[ubah-1] = nama
                        print("Nama event berhasil diubah\n")
                    elif menu == 2:  # mengubah tanggal event
                        tanggal_event = int(input("Masukkan tanggal event: "))
                        bulan_event = int(input("Masukkan bulan event: "))
                        tahun_event = int(input("Masukkan tahun event: "))
                        tanggal[ubah-1] = dt(tahun_event, bulan_event, tanggal_event) 
                        print("Tanggal event berhasil diubah\n") 
                    elif menu == 3:  # mengubah prioritas
                        pilihan = input("Ketik '1' untuk prioritas rendah, '2' untuk prioritas sedang, dan '3' untuk prioritas tinggi: ")
                        if pilihan == "1":
                            keterangan_event[ubah-1][0] = "Rendah"
                            print("Prioritas berhasil diubah\n")
                        elif pilihan == "2":
                            keterangan_event[ubah-1][0] = "Sedang"
                            print("Prioritas berhasil diubah\n")
                        elif pilihan == "3":
                            keterangan_event[ubah-1][0] = "Tinggi"
                            print("Prioritas berhasil diubah\n")
                        else:
                            print("Input yang dimasukkan tidak valid\n")
                    elif menu == 4:  # mengubah lokasi
                        lokasi = input("Masukkan lokasi: ")
                        keterangan_event[ubah-1][1] = lokasi
                        print("Lokasi berhasil diubah\n")
                    elif menu == 5:  # mengubah tags
                        tags = input("Masukkan tags: ")
                        keterangan_event[ubah-1][2] = tags
                        print("Tags berhasil diubah\n")
                    elif menu == 6:  # mengubah deskripsi
                        deskripsi = input("Masukkan deskripsi: ")
                        keterangan_event[ubah-1][3] = deskripsi
                        print("Deskripsi berhasil diubah\n")
                    elif menu == 7:  # kembali ke menu sebelumnya
                        break
                    else:  # jika menu tidak tersedia
                        print("Menu tidak ada\n")
            except ValueError:  # jika input yang dimasukkan tidak valid
                print("Input yang dimasukkan tidak valid\n")

# def cari_event(): mencari event
def cari_event():
    global index_event, nomor
    if index_event == 0:  # jika tidak ada event
        print("Tidak ada event\n")
    else:  # jika ada event
        print("1. Cari berdasarkan nama event")
        print("2. Cari berdasarkan tanggal event")
        print("3. Cari berdasarkan prioritas")
        print("4. Cari berdasarkan tags")
        print("5. Kembali ke menu utama\n")
        print("Pilih menu: ", end="")
        try:  # memasukkan menu yang ingin dicari
            menu = int(input())
        except ValueError:
            print("Input yang dimasukkan tidak valid\n")
            menu = 0
        if menu == 1:  # mencari berdasarkan nama event
            nama = input("Masukkan nama event: ").upper()
            for i in range(index_event):
                if event[i] == nama:  # jika nama event sesuai
                    tampilan(i, nomor)
                    nomor += 1
            if nomor == 1:  # jika tidak ada event yang sesuai
                print("Event tidak ditemukan\n")
            else:
                nomor = 1
        elif menu == 2:  # mencari berdasarkan tanggal event
            tanggal_event = int(input("Masukkan tanggal event: "))
            bulan_event = int(input("Masukkan bulan event: "))
            tahun_event = int(input("Masukkan tahun event: "))
            tanggal_cari = dt(tahun_event, bulan_event, tanggal_event)
            for i in range(index_event):
                if tanggal[i] == tanggal_cari:
                    tampilan(i, nomor)
                    nomor += 1
            if nomor == 1:
                print("Event tidak ditemukan\n")
            else:
                nomor = 1
        elif menu == 3:  # mencari berdasarkan prioritas
            pilihan = input("Ketik '1' untuk prioritas rendah, '2' untuk prioritas sedang, dan '3' untuk prioritas tinggi: ")
            if pilihan == "1":
                for i in range(index_event):
                    if keterangan_event[i][0] == "Rendah":
                        tampilan(i, nomor)
                        nomor += 1
                if nomor == 1:
                    print("Event tidak ditemukan\n")
                else:
                    nomor = 1
            elif pilihan == "2":
                for i in range(index_event):
                    if keterangan_event[i][0] == "Sedang":
                        tampilan(i, nomor)
                        nomor += 1
                if nomor == 1:
                    print("Event tidak ditemukan\n")
                else:
                    nomor = 1
            elif pilihan == "3":
                for i in range(index_event):
                    if keterangan_event[i][0] == "Tinggi":
                        tampilan(i, nomor)
                        nomor += 1
                if nomor == 1:
                    print("Event tidak ditemukan\n")
                else:
                    nomor = 1
            else:
                print("Input yang dimasukkan tidak valid\n")
        elif menu == 4:  # mencari berdasarkan tags
            tags = input("Masukkan tags: ")
            for i in range(index_event):
                if keterangan_event[i][2] == tags:
                    tampilan(i, nomor)
                    nomor += 1
            if nomor == 1:
                print("Event tidak ditemukan\n")
            else:
                nomor = 1
        elif menu == 5:  # kembali ke menu utama
            pass
        else:  # jika menu tidak tersedia
            print("Menu tidak ada\n")


# ALGORTIMA
# import library
from datetime import date as dt
from datetime import time as tm
from locale import setlocale, LC_ALL

# inisialisasi lokasi agar program tahuan bahasa Indonesia
setlocale(LC_ALL, 'id_ID.utf8')

# inisialisasi variabel
event = ['' for i in range(10)]
tanggal = [dt(1,1,1) for i in range(10)]
jam = [tm(0,0) for i in range(10)]
keterangan_event = [['-' for i in range(4)] for j in range(10)]
index_event = 0
nomor = 1
ubah = 0
jam_mulai = menit_mulai = 0
jam_selesai = menit_selesai = 0
nama = prioritas = lokasi = tags = deskripsi = ''
tanggal_event = bulan_event = tahun_event = 0

# program utama
print("Welcome to Counting Days!")
print("Silahkan memasukkan event yang ingin Anda ingatkan\n")
print("Catatan: jumlah maksimal untuk event reminder adalah 10\n")

while True:
    print("MENU UTAMA")
    print("1. Tambah Event")
    print("2. Lihat Event")
    print("3. Hapus Event")
    print("4. Ubah Event")
    print("5. Cari Event")
    print("6. Keluar\n")
    print("Pilih menu: ", end="")
    try:  # Mencegah input selain integer
        menu = int(input())  # Input menu

        if menu == 1:  # Tambah event
            if index_event == 10:
                print("Jumlah event sudah maksimal\n")
            else:
                tambah_event()
        elif menu == 2:  # Lihat event
            if index_event == 0:
                print("Tidak ada event\n")
            else:
                lihat_event()
        elif menu == 3:  # Hapus event
            if index_event == 0:
                print("Tidak ada event\n")
            else:
                hapus_event()
        elif menu == 4:  # Ubah event
            if index_event == 0:
                print("Tidak ada event\n")
            else:
                ubah_event()
        elif menu == 5:  # Cari event
            if index_event == 0:
                print("Tidak ada event\n")
            else:
                cari_event()
        elif menu == 6:  # Keluar
            break  # Keluar dari program
        else:  # Input selain 1-6
            print("Menu tidak tersedia\n")
    except:  
        print("Input yang dimasukkan tidak valid\n")
        menu = 0
          