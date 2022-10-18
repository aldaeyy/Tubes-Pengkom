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
# event_reminder: array of string
# keterangan_event: array of array of string
# index_event, index_hapus, index_ubah: integer
# tanggal_event, bulan_event, tahun_event: integer
# pilihan_waktu, pilihan_menu, pilihan_ubah, pilihan_keterangan: integer
# jam_event, menit_event: integer
# konfirmasi, nama_event, prioritas, lokasi, tags, deskripsi: string
# sisa_hari: timedelta
# hari_ini, tanggal: datetime
# waktu: time

# def menu_utama(): menampilkan pilihan menu
def menu_utama():
    print("Ketik '1' untuk menambah event reminder")
    print("Ketik '2' untuk melihat event reminder")
    print("Ketik '3' untuk menghapus event reminder")
    print("Ketik '4' untuk mengubah event reminder")
    print("Ketik '5' untuk keluar dari program\n")

# def menu_ubah(): menampilkan menu ubah
def menu_ubah():
        print("Ketik '1' untuk mengubah nama event reminder")
        print("Ketik '2' untuk mengubah tanggal event reminder")
        print("Ketik '3' untuk mengubah jam event reminder")
        print("Ketik '4' untuk mengubah atau menambah keterangan event reminder (opsional)")
        print("Ketik '5' untuk kembali ke menu utama\n")

# def menu_keterangan(): menampilkan menu keterangan
def menu_keterangan():
    print("Ketik '1' untuk mengubah atau menambah prioritas")
    print("Ketik '2' untuk mengubah atau menambah lokasi")
    print("Ketik '3' untuk mengubah atau menambah tags")
    print("Ketik '4' untuk mengubah atau menambah deskripsi")
    print("Ketik '5' untuk kembali ke menu utama\n")

# def tambah_event_reminder(): menambahkan reminder ke list
def tambah_event_reminder():
    global index_event
    nama_event = input("Masukkan nama event: ").upper()
    try:
        tanggal_event = int(input("Masukkan tanggal event: "))
        bulan_event = int(input("Masukkan bulan event: "))
        tahun_event = int(input("Masukkan tahun event: "))

        pilihan_waktu = input("Ketik 'Y' untuk menyetel waktu event secara spesifik: ").lower()
        if pilihan_waktu == 'y':
            jam_event = int(input("Masukkan jam event: "))
            menit_event = int(input("Masukkan menit event: "))
            waktu = tm(jam_event, menit_event).strftime("%H:%M")  # type: ignore
            keterangan_event[index_event][1] = waktu
        else:
            keterangan_event[index_event][1] = "Seharian"  # type: ignore
        # Menambahkan event ke list
        tanggal = dt(tahun_event, bulan_event, tanggal_event)
        event_reminder[index_event] = nama_event
        keterangan_event[index_event][0] = tanggal  # type: ignore
        index_event += 1
        index_event = min(index_event, 10)
        print("Event berhasil ditambahkan\n")

    except:
        print("Tanggal tidak valid\n")

# def tampilkan_event_reminder(): menampilkan event reminder
def tampilkan_event_reminder():
    nomor = 1
    print("DAFTAR EVENT UNTUK HARI INI")
    for i in range(index_event):
        sisa_hari = keterangan_event[i][0] - hari_ini  # type: ignore
        if sisa_hari.days == 0:
            print(f"""{nomor}. {event_reminder[i]}:
   Tanggal Event   : {keterangan_event[i][0]:%d-%m-%Y}
   Waktu Event     : {keterangan_event[i][1]}
   Prioritas       : {keterangan_event[i][2]}
   Lokasi          : {keterangan_event[i][3]}
   Tags            : {keterangan_event[i][4]}
   Deskripsi       : {keterangan_event[i][5]}""")
            nomor += 1
    if nomor == 1:
        print("Tidak ada event untuk hari ini\n")
    print('')
    nomor = 1

    print("DAFTAR EVENT UNTUK BESOK")
    for i in range(index_event):
        sisa_hari = keterangan_event[i][0] - hari_ini  # type: ignore
        if sisa_hari.days == 1:
            print(f"""{nomor}. {event_reminder[i]}:
   Tanggal Event   : {keterangan_event[i][0]:%d-%m-%Y}
   Waktu Event     : {keterangan_event[i][1]}
   Prioritas       : {keterangan_event[i][2]}
   Lokasi          : {keterangan_event[i][3]}
   Tags            : {keterangan_event[i][4]}
   Deskripsi       : {keterangan_event[i][5]}""")
            nomor += 1
    if nomor == 1:
        print("Tidak ada event untuk besok\n")
    print('')
    nomor = 1

    print("DAFTAR EVENT UNTUK SEMINGGU")
    for i in range(index_event):
        sisa_hari = keterangan_event[i][0] - hari_ini  # type: ignore
        if 0 <= sisa_hari.days <= 7:
            print(f"""{nomor}. {event_reminder[i]}:
   Tanggal Event   : {keterangan_event[i][0]:%d-%m-%Y}
   Waktu Event     : {keterangan_event[i][1]}
   Sisa hari       : {sisa_hari.days} hari  
   Prioritas       : {keterangan_event[i][2]}
   Lokasi          : {keterangan_event[i][3]}
   Tags            : {keterangan_event[i][4]}
   Deskripsi       : {keterangan_event[i][5]}""")
            nomor += 1
    if nomor == 1:
        print("Tidak ada event untuk seminggu\n")
    print('')
    nomor = 1

    print("DAFTAR EVENT YANG SUDAH LEWAT")
    for i in range(index_event):
        sisa_hari = keterangan_event[i][0] - hari_ini  # type: ignore
        if sisa_hari.days < 0:
            print(f"""{nomor}. {event_reminder[i]}:
   Tanggal Event   : {keterangan_event[i][0]:%d-%m-%Y}
   Waktu Event     : {keterangan_event[i][1]}
   Hari terlewat   : {-1 * sisa_hari.days} hari
   Prioritas       : {keterangan_event[i][2]}
   Lokasi          : {keterangan_event[i][3]}
   Tags            : {keterangan_event[i][4]}
   Deskripsi       : {keterangan_event[i][5]}""")
            nomor += 1
    if nomor == 1:
        print("Tidak ada event yang sudah terlewat\n")
    print('')
    nomor = 1

    print("DAFTAR SEMUA EVENT")
    for i in range(index_event):
        sisa_hari = keterangan_event[i][0] - hari_ini  # type: ignore
        print(f"""{i+1}. {event_reminder[i]}:
   Tanggal Event   : {keterangan_event[i][0]:%d-%m-%Y}
   Waktu Event     : {keterangan_event[i][1]}
   Sisa hari       : {sisa_hari.days} hari
   Prioritas       : {keterangan_event[i][2]}
   Lokasi          : {keterangan_event[i][3]}
   Tags            : {keterangan_event[i][4]}
   Deskripsi       : {keterangan_event[i][5]}""")
    print('')

# def hapus_event_reminder(): menghapus reminder dari event
def hapus_event_reminder():
    global index_hapus, index_event
    try:
        index_hapus = int(input("Masukkan nomor event yang ingin dihapus: "))
        if event_reminder[index_hapus-1] != "":
            print(f"Event yang akan dihapus: {event_reminder[index_hapus-1]}")
            konfirmasi = input("Apakah anda yakin? (Y/N): ").lower()
            if konfirmasi == "y":
                event_reminder[index_hapus-1] = ""  # menghapus event

                for i in range(6):  # menghapus keterangan dari event reminder
                    keterangan_event[index_hapus-1][i] = "-"

                for i in range(index_hapus, index_event):  # menggeser event
                    event_reminder[i-1] = event_reminder[i]
                    for j in range(1, 6):
                        keterangan_event[i-1][j] = keterangan_event[i][j]

                event_reminder[index_event] = ""  # menghapus event terakhir
                for i in range(6):  # menghapus keterangan dari event reminder terakhir
                    keterangan_event[index_event-1][i] = "-"
                print("Event berhasil dihapus\n")

                index_event -= 1  # mengurangi index event

            else:  # konfirmasi == "n" atau yang lainnya
                print("Event tidak jadi dihapus\n")

        else:  # event yang ingin dihapus tidak ada
            print("Event tidak ditemukan\n")

    except ValueError:
        print("Nomor event tidak valid\n")

# def ubah_nama_event_reminder(): mengubah nama event reminder
def ubah_nama_event_reminder():
    global index_ubah
    try:
        index_ubah = int(input("Masukkan nomor event yang ingin diubah: "))
        nama_event_baru = input("Masukkan nama event baru: ").upper()
        event_reminder[index_ubah-1] = nama_event_baru  # mengubah nama event
        print("Nama event berhasil diubah\n")
    except:
        print("Nomor event tidak valid\n")

# def ubah_tanggal_event_reminder(): mengubah tanggal event reminder
def ubah_tanggal_event_reminder():
    global index_ubah, index_event
    try:
        index_ubah = int(input("Masukkan nomor event yang ingin diubah: "))
        if index_ubah < 1 or index_ubah > index_event:  # event yang ingin diubah belum dibuat
            print("Nomor event tidak ditemukan\n")
        else:  # event yang ingin diubah sudah dibuat
            tanggal_event_baru = int(input("Masukkan tanggal event baru: "))
            bulan_event_baru = int(input("Masukkan bulan event baru: "))
            tahun_event_baru = int(input("Masukkan tahun event baru: "))
            tanggal = dt(tahun_event_baru, bulan_event_baru, tanggal_event_baru)  
            keterangan_event[index_ubah-1][0] = tanggal  # type: ignore
            print("Tanggal event berhasil diubah\n")
    except:
        print("Tanggal tidak valid\n")

# def ubah_waktu_event_reminder(): mengubah waktu event reminder
def ubah_waktu_event_reminder():
    global index_ubah
    try:
        index_ubah = int(input("Masukkan nomor event yang ingin diubah: "))
        if index_ubah < 1 or index_ubah > index_event:  # event yang ingin diubah belum dibuat
            print("Nomor event tidak ditemukan\n")
        else:  # event yang ingin diubah sudah dibuat
            pilihan_waktu = input("Ketik 'Y' untuk menyetel waktu event secara spesifik: ").lower()
            if pilihan_waktu == 'y':
                jam_event_baru = int(input("Masukkan jam event baru: "))
                menit_event_baru = int(input("Masukkan menit event baru: "))
                # mengubah waktu event
                keterangan_event[index_ubah-1][1] = tm(jam_event_baru, menit_event_baru).strftime("%H:%M")  # type: ignore
            else:  # pilihan_waktu == 'n' atau yang lainnya
                keterangan_event[index_ubah-1][1] = "Seharian"
            print("Waktu event berhasil diubah\n")
    except:
        print("Waktu tidak valid\n")

# def ubah_prioritas_event_reminder(): mengubah prioritas event reminder
def ubah_prioritas_event_reminder():
    global index_ubah
    try:
        index_ubah = int(input("Masukkan nomor event yang ingin diubah: "))
        print("Ketik '1' untuk prioritas rendah, '2' untuk prioritas sedang, dan '3' untuk prioritas tinggi")
        prioritas_event_baru = int(input("Masukkan pilihan: "))
        if prioritas_event_baru == 1:  # prioritas rendah
            keterangan_event[index_ubah-1][2] = "Rendah"
        elif prioritas_event_baru == 2:  # prioritas sedang
            keterangan_event[index_ubah-1][2] = "Sedang"
        elif prioritas_event_baru == 3:  # prioritas tinggi
            keterangan_event[index_ubah-1][2] = "Tinggi"
        else:  # prioritas_event_baru != 1, 2, atau 3
            print("Input tidak valid\n")
        print("Prioritas event berhasil diubah\n")
    except:
        print("Input tidak valid\n")

# def ubah_lokasi_event_reminder(): mengubah lokasi event reminder
def ubah_lokasi_event_reminder():
    global index_ubah
    try:
        index_ubah = int(input("Masukkan nomor event yang ingin diubah: "))
        lokasi_event_baru = input("Masukkan lokasi event baru: ")
        keterangan_event[index_ubah-1][3] = lokasi_event_baru  # mengubah lokasi event
        print("Lokasi event berhasil diubah\n")
    except:
        print("Input tidak valid\n")

# def ubah_tags_event_reminder(): mengubah tags event reminder
def ubah_tags_event_reminder():
    global index_ubah
    try:
        index_ubah = int(input("Masukkan nomor event yang ingin diubah: "))
        tags_event_baru = input("Masukkan tags event baru: ")
        keterangan_event[index_ubah-1][4] = tags_event_baru  # mengubah tags event
        print("Tags event berhasil diubah\n")
    except:
        print("Input tidak valid\n")

# def ubah_deskripsi_event_reminder(): mengubah deskripsi event reminder
def ubah_deskripsi_event_reminder():
    global index_ubah
    try:
        index_ubah = int(input("Masukkan nomor event yang ingin diubah: "))
        deskripsi_event_baru = input("Masukkan deskripsi event baru: ")
        keterangan_event[index_ubah-1][5] = deskripsi_event_baru  # mengubah deskripsi event
        print("Deskripsi event berhasil diubah\n")
    except:
        print("Input tidak valid\n")


# ALGORITMA
from datetime import date as dt  # untuk keperluan tanggal, format = YYYY-MM-DD
from datetime import time as tm  # untuk keperluan waktu, format = HH:MM:SS

# Inisialisasi
event_reminder = ['' for i in range(10)]
keterangan_event = [['-' for i in range(6)] for j in range(10)]
index_event = index_hapus = index_ubah = pilihan = pilihan_ubah = tanggal_event = bulan_event = tahun_event = jam_event = menit_event = detik_event = sisa_hari = 0 
berjalan = True
ubah_keterangan = False
hari_ini = dt.today()
konfirmasi = ''

# Pembuka
print("Welcome to Counting Days!")
print("Jumlah maksimal untuk event reminder adalah 10")

# Program utama
while berjalan:
    menu_utama()  # menampilkan menu utama, 1 = tambah, 2 = tampilkan, 3 = hapus, 4 = ubah, 5 = keluar
    try:
        pilihan = int(input("Masukkan pilihan: "))  
        if pilihan == 1:  # menambahkan event reminder
            if index_event < 10:  # jika masih ada slot kosong
                tambah_event_reminder()
            else:
                print("Jumlah event sudah maksimal\n")
        if pilihan == 2:  # menampilkan event reminder
            if index_event > 0:  # jika ada event yang tersimpan
                tampilkan_event_reminder()
            else:
                print("Tidak ada event yang tersimpan\n")
        if pilihan == 3:  # menghapus event reminder
            if index_event > 0:  # jika ada event yang tersimpan
                hapus_event_reminder()
            else:
                print("Tidak ada event yang tersimpan\n")
        if pilihan == 4:  # mengubah event reminder
            if index_event > 0:  # jika ada event yang tersimpan
                ubah_keterangan = True
                while ubah_keterangan:
                    menu_ubah()  # menampilkan menu ubah, 1 = ubah nama event, 2 = ubah tanggal event, 3 = ubah waktu event, 4 = ubah keterangan event, 5 = kembali
                    pilihan_ubah = int(input("Masukkan pilihan: "))
                    if pilihan_ubah == 1:  # mengubah nama event reminder
                        ubah_nama_event_reminder()
                    if pilihan_ubah == 2:  # mengubah tanggal event reminder
                        ubah_tanggal_event_reminder()
                    if pilihan_ubah == 3:  # mengubah waktu event reminder
                        ubah_waktu_event_reminder()
                    if pilihan_ubah == 4:  # mengubah atau menambah keterangan event reminder
                        menu_keterangan()  # menampilkan menu keterangan, 1 = prioritas, 2 = lokasi, 3 = tags, 4 = deskripsi, 5 = kembali
                        pilihan_keterangan = int(input("Masukkan pilihan: "))
                        if pilihan_keterangan == 1:  # mengubah prioritas event reminder
                            ubah_prioritas_event_reminder()
                        if pilihan_keterangan == 2:  # mengubah lokasi event reminder
                            ubah_lokasi_event_reminder()
                        if pilihan_keterangan == 3:  # mengubah tags event reminder
                            ubah_tags_event_reminder()
                        if pilihan_keterangan == 4:  # mengubah deskripsi event reminder
                            ubah_deskripsi_event_reminder() 
                        if pilihan_keterangan == 5:  # kembali ke menu utama
                            ubah_keterangan = False 
                    if pilihan_ubah == 5:  # kembali ke menu utama
                        ubah_keterangan = False                   
            else:  # jika tidak ada event yang tersimpan
                print("Tidak ada event yang tersimpan\n")
        if pilihan == 5:  # keluar dari program
            konfirmasi = input("Apakah anda yakin ingin keluar? (Y/N): ").lower()
            if konfirmasi == 'y':
                berjalan = False
                print("Terima kasih telah menggunakan program reminder")   
        pilihan = 0  # mengembalikan pilihan ke 0
    except:
        print("Pilihan tidak valid\n")
