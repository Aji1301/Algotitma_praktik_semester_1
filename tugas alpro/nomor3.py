# # Data dalam sebuah tupel
# banyak_angka = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# # Inisialisasi variabel untuk menghitung angka genap dan ganjil
# angka_genap = 0
# angka_ganjil = 0

# # proses
# for angka in banyak_angka:
#     if angka % 2 == 0:
#         angka_genap += 1
#     else:
#         angka_ganjil += 1

# # Cetak jumlah angka genap dan ganjil
# print("Jumlah bilangan genap dalam tupel adalah:", angka_genap)
# print("Jumlah bilangan ganjil dalam tupel adalah:", angka_ganjil)

# def tukar(bil1, bil2):
#     """Subprogram untuk menukar dua bilangan."""
#     temp = bil1
#     bil1 = bil2
#     bil2 = temp
#     return bil1, bil2

# def main():
#     angka1 = int(input("Angka 1 = "))
#     angka2 = int(input("Angka 2 = "))

#     print("Sebelum ditukar:")
#     print("Angka 1 =", angka1)
#     print("Angka 2 =", angka2)

#     # Panggil fungsi tukar untuk menukar nilai angka1 dan angka2
#     menukar = tukar(angka1, angka2)
#     print("Menukar untuk menukar", menukar)
    

#     # print("\nSetelah ditukar:")
#     # print("Angka 1 =", angka1)
#     # print("Angka 2 =", angka2)
# if __name__ == "__main__":
# # Panggil fungsi menukar_dan_tampilkan
#     main()


# def mencari(angka1, angka2):
#     """Fungsi untuk menemukan bilangan terkecil dari dua bilangan."""
#     if angka1 < angka2:
#         return angka1
#         return angka2
#     else:
#         return angka2

# def maini():
#     print("mencari angka terkecil")
#     angka1 = int(input("Angka 1 = "))
#     angka2 = int(input("Angka 2 = "))

#     print("Awal angka 1 =", angka1)
#     print("Awal angka 2 =", angka2)

#     # Panggil fungsi find_minimum dan cetak hasilnya
#     bilangan_terkecil = mencari(angka1, angka2)
#     print("Bilangan terkecil =", bilangan_terkecil)

# if __name__== "__main__":
#     maini()



def tukar(a, b):
    """Subprogram untuk menukar dua bilangan."""
    temp = a
    a = b
    b = temp
    return a, b

def menukar_dan_tampilkan():
    angka1 = int(input("Angka 1 = "))
    angka2 = int(input("Angka 2 = "))

    print("Sebelum ditukar:")
    print("Angka 1 =", angka1)
    print("Angka 2 =", angka2)

    # Panggil fungsi tukar untuk menukar nilai angka1 dan angka2
    angka1, angka2 = tukar(angka1, angka2)

    print("\nSetelah ditukar:")
    print("Angka 1 =", angka1)
    print("Angka 2 =", angka2)

# Panggil fungsi menukar_dan_tampilkan
menukar_dan_tampilkan()
