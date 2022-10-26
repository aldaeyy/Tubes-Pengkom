```python

{fungsi-fungsi} 
def menu_utama is
    output("MENU UTAMA")
    output("1. Tambah Event")
    output("2. Lihat Event")
    output("3. Hapus Event")
    output("4. Ubah Event")
    output("5. Cari Event")
    output("6. Keluar")

def tambah_event is
    input(nama_event)
    input(tanggal_event)
    input(waktu_event)
    list_event ← list_event + event

def lihat event is
    output(event for event in list_event)

def hapus_event is 
    lihat_event
    input(nomor_event, text="Masukkan nomor event yang ingin dihapus: ")
    list_event.pop(nomor_event - 1)

def ubah_event is
    input(nomor_event, text="Masukkan nomor event yang ingin diubah: ")
    input(pilihan, text="Masukkan isi yang ingin diubah: ")
    if pilihan == "nama" then
        input(nama)
        list_event[pilihan - 1].nama ← nama
    elif pilihan == "tanggal" then
        input(tanggal)
        list_event[pilihan - 1].tanggal ← tanggal
    elif pilihan == "waktu" then
        input(waktu)
        list_event[pilihan - 1].waktu ← waktu
    elif pilihan == "prioritas" then
        input(prioritas)
        list_event[pilihan - 1].prioritas ← prioritas
    elif pilihan == "lokasi" then
        input(lokasi)
        list_event[pilihan - 1].lokasi ← lokasi
    elif pilihan == "tags" then
        input(tags)
        list_event[pilihan - 1].tags ← tags
    elif pilihan == "deskripsi" then
        input(deskripsi)
        list_event[pilihan - 1].deskripsi ← deskripsi

def cari_event is
    input(pilihan, text="Masukkan pilihan berdasarkan apa pencariannya: ")
    if pilihan == "nama" then
        input(nama)
        for event in list_event
            if event.nama == nama then
                output(event)
    elif pilihan == "tanggal" then
        input(tanggal)
        for event in list_event
            if event.tanggal == tanggal then
                output(event)
    elif pilihan == "prioritas" then
        input(prioritas)
        for event in list_event
            if event.prioritas == prioritas then
                output(event)
    elif pilihan == "tags" then
        input(tags)
        for event in list_event
            if event.tags == tags then
                output(event)
    
def cek_notifikasi is
    for event in list_event
        if ((event.tanggal and event.waktu) == saat_ini) then
            output(notifikasi)

{inisiasi-variabel}
list_event ← list
jumlah_event ← 0

{program utama}
while (True) do
    menu_utama
    input(pilihan)

    if (pilihan == 1) then
        (tambah_event)
    elif (pilihan == 2) then
        (lihat_event)
    elif (pilihan == 3) then
        (hapus_event)
    elif (pilihan == 4) then
        (ubah_event)
    elif (pilihan == 5) then
        (cari_event)

    if (jumlah_event > 0) then
        cek_notifikasi

    until
        pilihan == 6

```