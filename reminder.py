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
# index_event: integer
# index_hapus: integer
# index_ubah: integer
# nama_event: string
# tanggal_event: integer
# bulan_event: integer
# tahun_event: integer
# pilihan_waktu: string
# jam_event: integer
# menit_event: integer
# tanggal: datetime
# pilihan_menu: integer
# pilihan_ubah: integer
# pilihan_keterangan: integer
# prioritas: string
# lokasi: string
# tags: string
# deskripsi: string
# sisa_hari: timedelta
# waktu: time
# hari_ini: timedelta

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
        tanggal = dt(tahun_event, bulan_event, tanggal_event)
        event_reminder[index_event] = nama_event
        keterangan_event[index_event][0] = tanggal  # type: ignore
        index_event += 1
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
        print("Tidak ada event untuk hari ini atau besok\n")
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
        print("Tidak ada event untuk hari ini atau besok\n")
    print('')
    nomor = 1

    print("DAFTAR EVENT UNTUK SEMINGGU")
    for i in range(index_event):
        sisa_hari = keterangan_event[i][0] - hari_ini  # type: ignore
        if 0 <= sisa_hari.days <= 7:
            print(f"""{nomor}. {event_reminder[i]}:
   Tanggal Event   : {keterangan_event[i][0]:%d-%m-%Y}
   Waktu Event     : {keterangan_event[i][1]}
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
   Prioritas       : {keterangan_event[i][2]}
   Lokasi          : {keterangan_event[i][3]}
   Tags            : {keterangan_event[i][4]}
   Deskripsi       : {keterangan_event[i][5]}""")
            nomor += 1
    if nomor == 1:
        print("Tidak ada event untuk seminggu\n")
    print('')
    nomor = 1

    print("DAFTAR SEMUA EVENT")
    for i in range(index_event):
        print(f"""{i+1}. {event_reminder[i]}:
   Tanggal Event   : {keterangan_event[i][0]:%d-%m-%Y}
   Waktu Event     : {keterangan_event[i][1]}
   Prioritas       : {keterangan_event[i][2]}
   Lokasi          : {keterangan_event[i][3]}
   Tags            : {keterangan_event[i][4]}
   Deskripsi       : {keterangan_event[i][5]}""")
    print('')

# def hapus_event_reminder(): menghapus reminder dari event
def hapus_event_reminder():
    global index_hapus, index_event
    while index_hapus < 1 or index_hapus > 5:
        index_hapus = int(input("Masukkan nomor event yang ingin dihapus: "))
    if event_reminder[index_hapus-1] != "":
        print(f"Event yang akan dihapus: {event_reminder[index_hapus-1]}")
        konfirmasi = input("Apakah anda yakin? (Y/N): ").lower()
        if konfirmasi == "y":
            event_reminder[index_hapus-1] = ""
            for i in range(6):
                keterangan_event[index_hapus-1][i] = ""
            for i in range(index_hapus, index_event):
                event_reminder[i-1] = event_reminder[i]
                for j in range(index_event):
                    keterangan_event[i-1][j] = keterangan_event[i][j]
            index_event -= 1
            event_reminder[index_event] = ""
            for i in range(6):
                keterangan_event[index_event][i] = ""
            print("Event berhasil dihapus\n")
        else:
            print("Event tidak jadi dihapus\n")
    else:
        print("Event tidak ditemukan\n")

# def ubah_nama_event_reminder(): mengubah nama event reminder
def ubah_nama_event_reminder():
    global index_ubah
    index_ubah = int(input("Masukkan nomor event yang ingin diubah: "))
    nama_event_baru = input("Masukkan nama event baru: ").upper()
    event_reminder[index_ubah-1] = nama_event_baru
    print("Nama event berhasil diubah\n")

# def ubah_tanggal_event_reminder(): mengubah tanggal event reminder
def ubah_tanggal_event_reminder():
    global index_ubah
    index_ubah = int(input("Masukkan nomor event yang ingin diubah: "))
    tanggal_event_baru = int(input("Masukkan tanggal event baru: "))
    bulan_event_baru = int(input("Masukkan bulan event baru: "))
    tahun_event_baru = int(input("Masukkan tahun event baru: "))
    tanggal = dt(tahun_event_baru, bulan_event_baru, tanggal_event_baru)
    keterangan_event[index_ubah-1][0] = tanggal  # type: ignore
    print("Tanggal event berhasil diubah\n")

# def ubah_waktu_event_reminder(): mengubah waktu event reminder
def ubah_waktu_event_reminder():
    global index_ubah
    index_ubah = int(input("Masukkan nomor event yang ingin diubah: "))
    pilihan_waktu = input("Ketik 'Y' untuk menyetel waktu event secara spesifik: ").lower()
    if pilihan_waktu == 'y':
        jam_event_baru = int(input("Masukkan jam event baru: "))
        menit_event_baru = int(input("Masukkan menit event baru: "))
        keterangan_event[index_ubah-1][1] = tm(jam_event_baru, menit_event_baru).strftime("%H:%M")  # type: ignore
    else:
        keterangan_event[index_ubah-1][1] = "Seharian"
    print("Waktu event berhasil diubah\n")

# def ubah_prioritas_event_reminder(): mengubah prioritas event reminder
def ubah_prioritas_event_reminder():
    global index_ubah
    index_ubah = int(input("Masukkan nomor event yang ingin diubah: "))
    print("Ketik '1' untuk prioritas rendah, '2' untuk prioritas sedang, dan '3' untuk prioritas tinggi")
    prioritas_event_baru = int(input("Masukkan pilihan: "))
    if prioritas_event_baru == 1:
        keterangan_event[index_ubah-1][2] = "Rendah"
    elif prioritas_event_baru == 2:
        keterangan_event[index_ubah-1][2] = "Sedang"
    elif prioritas_event_baru == 3:
        keterangan_event[index_ubah-1][2] = "Tinggi"
    else:
        print("Input tidak valid\n")
    print("Prioritas event berhasil diubah\n")

# def ubah_lokasi_event_reminder(): mengubah lokasi event reminder
def ubah_lokasi_event_reminder():
    global index_ubah
    index_ubah = int(input("Masukkan nomor event yang ingin diubah: "))
    lokasi_event_baru = input("Masukkan lokasi event baru: ")
    keterangan_event[index_ubah-1][3] = lokasi_event_baru
    print("Lokasi event berhasil diubah\n")

# def ubah_tags_event_reminder(): mengubah tags event reminder
def ubah_tags_event_reminder():
    global index_ubah
    index_ubah = int(input("Masukkan nomor event yang ingin diubah: "))
    tags_event_baru = input("Masukkan tags event baru: ")
    keterangan_event[index_ubah-1][4] = tags_event_baru
    print("Tags event berhasil diubah\n")

# def ubah_deskripsi_event_reminder(): mengubah deskripsi event reminder
def ubah_deskripsi_event_reminder():
    global index_ubah
    index_ubah = int(input("Masukkan nomor event yang ingin diubah: "))
    deskripsi_event_baru = input("Masukkan deskripsi event baru: ")
    keterangan_event[index_ubah-1][5] = deskripsi_event_baru
    print("Deskripsi event berhasil diubah\n")


# ALGORITMA
from datetime import date as dt
from datetime import time as tm

# Inisialisasi
event_reminder = ['' for i in range(10)]
keterangan_event = [['-' for i in range(6)] for j in range(10)]
berjalan = True
index_event = index_hapus = index_ubah = pilihan = pilihan_ubah = tanggal_event = bulan_event = tahun_event = jam_event = menit_event = detik_event = sisa_hari = 0 
hari_ini = dt.today()

# Pembuka
print("Selamat datang di program reminder!")
print("Jumlah maksimal untuk event reminder adalah 10")

# Program utama
while berjalan:
    menu_utama()
    try:
        pilihan = int(input("Masukkan pilihan: "))
    except:
        print("Pilihan tidak valid\n")

    if pilihan == 1:
        if index_event < 5:
            tambah_event_reminder()
        else:
            print("Jumlah event sudah maksimal\n")
    if pilihan == 2:
        if index_event > 0:
            tampilkan_event_reminder()
        else:
            print("Tidak ada event yang tersimpan\n")
    if pilihan == 3:
        if index_event > 0:
            hapus_event_reminder()
        else:
            print("Tidak ada event yang tersimpan\n")
    if pilihan == 4:
        if index_event > 0:
            menu_ubah()
            pilihan_ubah = int(input("Masukkan pilihan: "))
            if pilihan_ubah == 1:
                ubah_nama_event_reminder()
            if pilihan_ubah == 2:
                ubah_tanggal_event_reminder()
            if pilihan_ubah == 3:
                ubah_waktu_event_reminder()
            if pilihan_ubah == 4:
                menu_keterangan()
                pilihan_keterangan = int(input("Masukkan pilihan: "))
                if pilihan_keterangan == 1:
                    ubah_prioritas_event_reminder()
                if pilihan_keterangan == 2:
                    ubah_lokasi_event_reminder()
                if pilihan_keterangan == 3:
                    ubah_tags_event_reminder()
                if pilihan_keterangan == 4:
                    ubah_deskripsi_event_reminder()                     
            if pilihan_ubah == 5:
                pass
        else:
            print("Tidak ada event yang tersimpan\n")
    if pilihan == 5:
        berjalan = False
    
    pilihan = 0
