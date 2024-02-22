# Nama : AJI

import datetime

def cetak_struk(nama_pemesan, pesanan_makanan, pesanan_minuman, total_tagihan, uang_diberi):
    tanggal_beli = datetime.datetime.now()
    
    print("\n=============================")
    print("========= S T R U K =========")
    print(f"=== Tanggal beli {tanggal_beli.strftime('%Y-%m-%d')}")
    print("=============================")
    print(f"=== Pemesan      : {nama_pemesan}")
    
    if pesanan_makanan:
        print("=== Beli:")
        for makanan, jumlah in pesanan_makanan.items():
            print(f"===   {makanan}   : Rp. {jumlah * menu_makanan[makanan]}")
    
    if pesanan_minuman: 
            print(f"===   {minuman}     : Rp. {jumlah * menu_minuman[minuman]}")
    
    print("=============================")
    print(f"=== Total Tagihan  : {total_tagihan}")
    print(f"=== Uang           : {uang_diberi}")
    print(f"=== Kembalian      : {uang_diberi - total_tagihan}")
    print("========= Terima Kasih ======")
    print("=============================")

# Menu Makanan
menu_makanan = {
    "Nasi Goreng": 15000,
    "Mie Goreng": 10000,
}

# Menu Minuman
menu_minuman = {
    "Es Teh": 2000,
    "Es Jeruk": 3000,
}

# Input Nama Pembeli
nama_pemesan = input("Masukkan Nama Pembeli: ")

# Pilihan Makanan
print("\n============================")
print("=========Warung gaul========")
print("========Menu Makanan========")
for i, (makanan, harga) in enumerate(menu_makanan.items(), start=1):
    print(f"{i}. {makanan} - Rp {harga}")

# Pilihan Minuman
print("============================")
print("========Menu Minuman========")
for i, (minuman, harga) in enumerate(menu_minuman.items(), start=1):
    print(f"{i}. {minuman} - Rp {harga}")

pilihan_makanan = int(input("Pilih Makanan (1/2): "))
jumlah_makanan = int(input("Jumlah Makanan yang Dipesan: "))

pilihan_minuman = int(input("Pilih Minuman (1/2): "))
jumlah_minuman = int(input("Jumlah Minuman yang Dipesan: "))

# Menghitung Total Tagihan
total_tagihan = (jumlah_makanan * menu_makanan[list(menu_makanan.keys())[pilihan_makanan - 1]]) + \
                 (jumlah_minuman * menu_minuman[list(menu_minuman.keys())[pilihan_minuman - 1]])

# Input Uang yang Diberikan
uang_diberi = int(input("Masukkan Uang yang Diberikan: "))
print("============================")

# Cetak Struk
cetak_struk(nama_pemesan, {list(menu_makanan.keys())[pilihan_makanan - 1]: jumlah_makanan},
            {list(menu_minuman.keys())[pilihan_minuman - 1]: jumlah_minuman}, total_tagihan, uang_diberi)