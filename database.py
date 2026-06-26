# FILE 2
import csv
import os
from datetime import datetime
from struktur_data import LinkedList, Queue, bubble_sort, linear_search

FOLDER_DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')

antrian = Queue()

# FUNGSI CSV
def baca_csv(nama_file):
    path = os.path.join(FOLDER_DATA, nama_file)
    if not os.path.exists(path):
        return []
    with open(path, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def tulis_csv(nama_file, data, kolom):
    path = os.path.join(FOLDER_DATA, nama_file)
    with open(path, 'w', newline='', encoding='utf-8') as f:
        penulis = csv.DictWriter(f, fieldnames=kolom)
        penulis.writeheader()
        penulis.writerows(data)

# FUNGSI TIKET
KOLOM_TIKET = ['nama_acara', 'harga', 'stok']

def lihat_tiket():
    data = baca_csv('tiket.csv')
    if not data:
        print('Belum ada tiket.')
        return []
    data_urut = bubble_sort(data, 'harga')
    print('\n===================== DAFTAR TIKET ====================')
    print(f'{"No":<4} {"Nama Acara":<30} {"Harga":>10} {"Stok":>8}')
    print('-' * 55)
    for i, t in enumerate(data_urut, 1):
        print(f'{i:<4} {t["nama_acara"]:<30} Rp{int(t["harga"]):>10,} {t["stok"]:>6}')
    return data_urut

def tambah_tiket():
    print('\n=== TAMBAH TIKET ===')
    nama = input('Nama Acara : ').strip()
    harga = input('Harga      : ').strip()
    stok = input('Stok       : ').strip()
    if not nama or not harga or not stok:
        print('Semua field wajib diisi!')
        return
    try:
        int(harga)
        int(stok)
    except:
        print('Harga dan stok harus angka!')
        return
    data = baca_csv('tiket.csv')
    data.append({'nama_acara': nama, 'harga': harga, 'stok': stok})
    tulis_csv('tiket.csv', data, KOLOM_TIKET)
    print('Tiket berhasil ditambahkan!')

def edit_tiket():
    data_urut = lihat_tiket()
    if not data_urut:
        return
    try:
        nomor = int(input('\nPilih nomor tiket yang mau diedit: '))
        if nomor < 1 or nomor > len(data_urut):
            print('Nomor tidak valid!')
            return
        tiket = data_urut[nomor - 1]
    except:
        print('Nomor tidak valid!')
        return
    print('(Tekan Enter untuk tidak mengubah)')
    nama = input(f'Nama Acara [{tiket["nama_acara"]}]: ').strip() or tiket['nama_acara']
    harga = input(f'Harga [{tiket["harga"]}]: ').strip() or tiket['harga']
    stok = input(f'Stok [{tiket["stok"]}]: ').strip() or tiket['stok']
    data_semua = baca_csv('tiket.csv')
    for t in data_semua:
        if t['nama_acara'] == tiket['nama_acara']:
            t['nama_acara'] = nama
            t['harga'] = harga
            t['stok'] = stok
    tulis_csv('tiket.csv', data_semua, KOLOM_TIKET)
    print('Tiket berhasil diubah!')

def hapus_tiket():
    data_urut = lihat_tiket()
    if not data_urut:
        return
    try:
        nomor = int(input('\nPilih nomor tiket yang mau dihapus: '))
        if nomor < 1 or nomor > len(data_urut):
            print('Nomor tidak valid!')
            return
        tiket = data_urut[nomor - 1]
    except:
        print('Nomor tidak valid!')
        return
    konfirmasi = input(f'Yakin hapus "{tiket["nama_acara"]}"? (y/n): ').strip().lower()
    if konfirmasi == 'y':
        data_semua = baca_csv('tiket.csv')
        data_baru = [t for t in data_semua if t['nama_acara'] != tiket['nama_acara']]
        tulis_csv('tiket.csv', data_baru, KOLOM_TIKET)
        print('Tiket berhasil dihapus!')
    else:
        print('Dibatalkan.')

def cari_tiket():
    kata = input('Cari tiket: ').strip()
    data = baca_csv('tiket.csv')
    hasil = linear_search(data, 'nama_acara', kata)
    if not hasil:
        print('Tiket tidak ditemukan!')
        return
    print(f'\nHasil pencarian "{kata}":')
    for i, t in enumerate(hasil, 1):
        print(f'  {i}. {t["nama_acara"]} - Rp{int(t["harga"]):,} (Stok: {t["stok"]})')

# FUNGSI PEMESANAN
KOLOM_PESAN = ['nama_pemesan', 'nama_acara', 'jumlah', 'total', 'tanggal']

def pesan_tiket():
    data_urut = lihat_tiket()
    if not data_urut:
        return

    try:
        nomor = int(input('\nPilih nomor tiket: '))
        if nomor < 1 or nomor > len(data_urut):
            print('Nomor tidak valid!')
            return
        tiket = data_urut[nomor - 1]
    except:
        print('Nomor tidak valid!')
        return

    if int(tiket['stok']) == 0:
        print('Stok tiket habis!')
        return

    nama = input('Nama pemesan: ').strip()
    try:
        jumlah = int(input(f'Jumlah tiket (stok: {tiket["stok"]}): '))
    except:
        print('Jumlah harus angka!')
        return

    if jumlah <= 0 or jumlah > int(tiket['stok']):
        print('Jumlah tidak valid!')
        return

    total = int(tiket['harga']) * jumlah
    print(f'Total bayar: Rp{total:,}')
    konfirmasi = input('Konfirmasi pesan? (y/n): ').strip().lower()
    if konfirmasi != 'y':
        print('Pemesanan dibatalkan.')
        return

    # Masukkan ke antrian
    permintaan = {
        'nama': nama,
        'nama_acara': tiket['nama_acara'],
        'jumlah': jumlah,
        'total': total
    }
    antrian.masuk(permintaan)
    print(f'Masuk antrian... (posisi {antrian.ukuran()})')

    # Proses antrian
    while not antrian.kosong():
        req = antrian.keluar()

        # Kurangi stok tiket
        data_tiket = baca_csv('tiket.csv')
        for t in data_tiket:
            if t['nama_acara'] == req['nama_acara']:
                t['stok'] = str(int(t['stok']) - req['jumlah'])
        tulis_csv('tiket.csv', data_tiket, KOLOM_TIKET)

        # Simpan ke riwayat pemesanan
        baris_baru = {
            'nama_pemesan': req['nama'],
            'nama_acara': req['nama_acara'],
            'jumlah': req['jumlah'],
            'total': req['total'],
            'tanggal': datetime.now().strftime('%Y-%m-%d')
        }
        riwayat = baca_csv('pemesanan.csv')
        riwayat.append(baris_baru)
        tulis_csv('pemesanan.csv', riwayat, KOLOM_PESAN)

        print('Pemesanan berhasil disimpan!')

def lihat_riwayat():
    data = baca_csv('pemesanan.csv')
    if not data:
        print('Belum ada riwayat pemesanan.')
        return
    riwayat = LinkedList()
    for p in data:
        teks = f"{p['nama_pemesan']} | {p['nama_acara']} | {p['jumlah']} tiket | Rp{int(p['total']):,} | {p['tanggal']}"
        riwayat.tambah(teks)
    print('\n=== RIWAYAT PEMESANAN ===')
    riwayat.tampilkan()
