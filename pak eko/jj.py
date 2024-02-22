print("==========================")
print("=====warung kredipeti=====")
print("==========menu============")
print("========makanan===========")
satu = "nasi goreng : 10.000\nmie goreng  : 20.000"
print(satu)
print("========minuman===========")
dua = "es teh   : 10.000\nes jeruk : 20.000"
print(dua)
print("==========================")

def hitung_total(harga, jumlah):
    return harga * jumlah

def kasir_sederhana():
    daftar_barang = {}
    total_pembelian = 0

    while True:
        print("\n=== Program Kasir Sederhana ===")
        print("1. Tambah Barang")
        print("2. Lihat Keranjang Belanja")
        print("3. Selesai Belanja")


        pilihan = input("Pilih menu (1/2/3): ")

        if pilihan == '1':
            nama_barang = input("Masukkan nama barang: ")
            harga_barang = float(input("Masukkan harga barang per item: "))
            jumlah_barang = int(input("Masukkan jumlah barang: "))

            total_barang = hitung_total(harga_barang, jumlah_barang)

            daftar_barang[nama_barang] = {"harga": harga_barang, "jumlah": jumlah_barang, "total": total_barang}

            print(f"{nama_barang} ditambahkan ke keranjang belanja.")

        elif pilihan == '2':
            print("\n=== Keranjang Belanja ===")
            for nama, barang in daftar_barang.items():
                print(f"{nama}: {barang['jumlah']} x {barang['harga']} = {barang['total']}")

            total_pembelian = sum(barang["total"] for barang in daftar_barang.values())
            print(f"\nTotal Pembelian: {total_pembelian}")

        elif pilihan == '3':
            print(f"\nTotal Pembelian: {total_pembelian}")
            print("Terima kasih telah berbelanja. Selamat datang kembali!")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

# Panggil fungsi kasir_sederhana untuk menjalankan program
kasir_sederhana()
def hitung_total(harga, jumlah):
    return harga * jumlah

def tambah_pesanan(daftar_pesanan):
    nama_produk = input("Masukkan nama makanan/minuman: ")
    harga_produk = float(input("Masukkan harga per item: "))
    jumlah_pesanan = int(input("Masukkan jumlah pesanan: "))

    total_pesanan = hitung_total(harga_produk, jumlah_pesanan)

    daftar_pesanan[nama_produk] = {"harga": harga_produk, "jumlah": jumlah_pesanan, "total": total_pesanan}

    print(f"{jumlah_pesanan} {nama_produk} ditambahkan ke keranjang belanja.")

def lihat_keranjang(daftar_pesanan):
    print("\n=== Keranjang Belanja ===")
    for nama, pesanan in daftar_pesanan.items():
        print(f"{nama}: {pesanan['jumlah']} x {pesanan['harga']} = {pesanan['total']}")

    total_pembelian = sum(pesanan["total"] for pesanan in daftar_pesanan.values())
    print(f"\nTotal Pembelian: {total_pembelian}")

def selesai_belanja(daftar_pesanan):
    lihat_keranjang(daftar_pesanan)
    print("Terima kasih telah berbelanja. Selamat datang kembali!")

def kasir_makanan_minuman():
    daftar_pesanan = {}
