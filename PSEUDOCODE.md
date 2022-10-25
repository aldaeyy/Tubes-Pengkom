```python
while True do:
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
```
