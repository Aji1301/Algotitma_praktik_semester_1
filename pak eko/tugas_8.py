

# Input data
nama_pembeli = int(input("Nama Pembeli"))
print("====== KREDIPETI =======")
print("===== MENUNYA GUES =====")
print(nama_pembeli)
pesanan_makanan = ["2 Nasi Goreng"]
pesanan_minuman = ["1 Es Jeruk"]
total_tagihan = 33000
uang_diberikan = 50000
kembalian = uang_diberikan - total_tagihan

# Print the receipt
print("=== STRUK PEMBELIAN ===")
import datetime
now = datetime.datetime.now()
print("Waktu hari ini =",now)

print(f"Nama : {nama_pembeli}\n")
print("Beli :", end=" ")
for item in pesanan_makanan + pesanan_minuman:
    print(item, end=", ")
print(f"\nTagihan : {total_tagihan}")
print(f"Uang : {uang_diberikan}")
print(f"Kembalian : {kembalian}\n")
print("TERIMA KASIH")
# Information
def pilih_makanan():
    print("Silakan pilih menu makanan:")
    print("1. Nasi Goreng")
    print("2. Mie Goreng")

    pilihan_menu = input("Masukkan nomor pilihan Anda (1 atau 2): ")

    if pilihan_menu == '1':
        makanan = "Nasi Goreng"
    elif pilihan_menu == '2':
        makanan = "Mie Goreng"
    else:
        print("Pilihan tidak valid. Silakan masukkan 1 atau 2.")
        return

    jumlah_porsi = int(input(f"Berapa banyak porsi {makanan} yang ingin Anda beli? "))

    print(f"Anda memilih {makanan} sebanyak {jumlah_porsi} porsi. Selamat menikmati!")

# Panggil fungsi untuk meminta pengguna memilih makanan
pilih_makanan()
nama = "Naruto"
beli = "3 Nasi Goreng\n      1 Es Jeruk"
tagihan = {"Nasi Goreng": 40000, "Es Jeruk": 900000}
total_tagihan = sum(tagihan.values())
uang_diberikan = 900000
kembalian = uang_diberikan - total_tagihan

# Output
print("Nama:", nama)
print("Beli:", beli)
print("Tagihan:", tagihan)
print("Uang: Rp.", total_tagihan)
print("Rp.", uang_diberikan)
print("Kembalian : Rp.", kembalian)



class Pesanan:
    def __init__(self, nama, jumlah):
        self.nama = nama
        self.jumlah = jumlah

def pesan_makanan():
    print("Mau pesan makan apa? [1/2]:")
    makanan = input()
    return Pesanan("Makanan", int(makanan))

def pesan_minuman():
    print("Mau pesan minum apa? [1/2]:")
    minuman = input()
    return Pesanan("Minuman", int(minuman))

def main():
    pesanan_makanan = pesan_makanan()
    print("Berapa? [1/2/3/...]:")
    jumlah_makanan = int(input())
    pesanan_makanan.jumlah = jumlah_makanan

    pesanan_minuman = pesan_minuman()
    print("Berapa? [1/2/3/...]:")
    jumlah_minuman = int(input())
    pesanan_minuman.jumlah = jumlah_minuman

    total_harga = pesanan_makanan.jumlah * 20000 + pesanan_minuman.jumlah * 5000

    print("Masukkan uang yang diberi:")
    uang_diberi = int(input())

    if uang_diberi < total_harga:
        print("Uang Anda tidak cukup. Mohon masukkan uang yang cukup.")
    else:
        kembalian = uang_diberi - total_harga
        print(f"Terima kasih! Pesanan Anda telah diterima.\nKembalian Anda: {kembalian}")

if __name__ == "__main__":
    main()


def makanan():
    global total_makanan, jumlah_porsi, nama_makanan
def minuman():
    global total_minuman, jumlah_gelas, nama_minuman
menu_makanan = int(input("masukan pilihan (1/2)?"))
jumlah_porsi = int(input("masukan pilihan porsi"))

if menu_makanan == 1:
    total_makanan = jumlah_porsi * 10000
    print("Nasi goreng",jumlah_porsi,"porsi = Rp.",total_makanan)
    nama_makanan = ("Nasi goreng")
elif menu_makanan == 2:
    total_makanan = jumlah_porsi * 12000
    print("Mie goreng",jumlah_porsi,"porsi = Rp.",total_makanan)
else:
    print("pilihan tidak tersedia")

menu_minuman = int(input("masukan pilihan (1/2)?"))
jumlah_gelas = int(input("masukan pilihan porsi"))
if menu_minuman == 1:
    total_minuman = jumlah_gelas * 10000
    print("Nasi goreng",jumlah_gelas,"porsi = Rp.",total_minuman)
    nama_minuman = ("Nasi goreng")
elif menu_minuman == 2:
    total_minuman = jumlah_gelas * 12000
    print("Mie goreng",jumlah_gelas,"porsi = Rp.",total_minuman)
else:
    print("pilihan tidak tersedia")

# makanan()
# minuman()
# jumlah_semuanya = total_makanan + total_minuman
# print(nama_makanan)
# print(jumlah_porsi)
# print(nama_minuman)
# print(jumlah_gelas)
# print(jumlah_semuanya)

# import random

# circle = ["Anto", "Budi", "Citra", "Devi"]
# weeks = ["Minggu ke-1", "Minggu ke-2", "Minggu ke-3", "Minggu ke-4"]

# print("==== JADWAL MENJAGA CUPANG ====")

# for i in range(4):
#     caretaker = random.choice(circle)
#     circle.remove(caretaker)

#     remaining_circle = ', '.join(circle) if i < 3 else "Habis"
#     print(f"{weeks[i]}: {caretaker}, Sisa data: {remaining_circle}")

#     if i < 3:
#         print("")

# print("==== SEMANGAT MENJAGA CUPANG! ====")