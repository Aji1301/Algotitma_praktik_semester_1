'''import a as f1
# Input dua angka dari pengguna
angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))

# Menu operasi
print("Pilih operasi:")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

# Input pilihan operasi
pilihan = input("Masukkan pilihan (1/2/3/4): ")

if pilihan == '1':
    hasil = (angka1, angka2)
    print(f1.a(angka1, angka2))
elif pilihan == '2':
    hasil = kurang(angka1, angka2)
    print("Hasil pengurangan:", hasil)
elif pilihan == '3':
    hasil = kali(angka1, angka2)
    print("Hasil perkalian:", hasil)
elif pilihan == '4':
    hasil = bagi(angka1, angka2)
    print("Hasil pembagian:", hasil)
else:
    print("Pilihan tidak valid")
'''