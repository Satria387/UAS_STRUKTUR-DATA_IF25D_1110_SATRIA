# FILE 3
from database import (
    lihat_tiket, tambah_tiket, edit_tiket, hapus_tiket, cari_tiket,
    pesan_tiket, lihat_riwayat
)

def menu_utama():
    print('=' * 28)
    print('   SISTEM PEMESANAN TIKET')
    print('=' * 28)

    while True:
        print('----- MENU UTAMA ----')
        print('1. Lihat Daftar Tiket')
        print('2. Cari Tiket')
        print('3. Pesan Tiket')
        print('4. Lihat Riwayat Pemesanan')
        print('5. Tambah Tiket Baru')
        print('6. Edit Tiket')
        print('7. Hapus Tiket')
        print('0. Keluar')

        pilihan = input('Pilih menu (0-7): ').strip()

        if pilihan == '1':
            lihat_tiket()
        elif pilihan == '2':
            cari_tiket()
        elif pilihan == '3':
            pesan_tiket()
        elif pilihan == '4':
            lihat_riwayat()
        elif pilihan == '5':
            tambah_tiket()
        elif pilihan == '6':
            edit_tiket()
        elif pilihan == '7':
            hapus_tiket()
        elif pilihan == '0':
            print('Terima Kasih!!')
            break
        else:
            print('Menu tidak valid, coba lagi')

menu_utama()
