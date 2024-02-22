# # definision of the main function

# # def get_name ():
# #     name = 'masukan nama mu:'

# #     return name

# # def main ():
# #     hello = get_name()
# #     print ('helo')

# # def main():
# #     value = 99
# #     print ('The value is', value) 
# #     change_me (value)
# #     print ('Back in main the value is', value)

# # def change_me (arg):
# #     print ('I am changing the value.' )
# #     arg = 0 
# #     print ('Now the value is', arg)
# # # Call the main function.
# # main ()

# # 


# bilangan_1 = input('masukan bilangan 1:')
# bilangan_2 = input('masukan bilangan 2:')

# tukar = bilangan_1
# bilangan_1 = bilangan_2
# bilangan_2 = tukar

# print('bilangan 1:',bilangan_1)
# print('bilangan 2:',bilangan_2)


# def nilai_trkecil(nilai1, nilai2):
#     if nilai1 < nilai2 :
#         return nilai1
#     else:
#         return nilai2

# nilai1 = float(input('masukan nilai:'))
# nilai2 = float(input('masukan nilai2:'))

# hasil_nilai = nilai_trkecil(nilai1, nilai2)
# print(hasil_nilai)

# def Hitung_HurufAngka():
#     s = input("input a srting = ")
#     d = l = 0
#     for c in s:
#         if c.isdigit():
#             d = d+1
#         elif c.isalpha():
#             l = l+1
#         else:
#             pass
#     print("letters", 1)
#     print("Digits", d)

# def utama():
#     print("Program Hitung Angka dan Huruf")
#     Hitung_HurufAngka()
#     print("selesai")

# Mendefinisikan data matakuliah dan bobotnya
matakuliah = {
    "Agama": {"sks": 2, "nilai": "A", "bobot": 8},
    "Matematika": {"sks": 3, "nilai": "A", "bobot": 12},
    "Algoritma": {"sks": 3, "nilai": "C", "bobot": 6},
    "Pemrograman Web": {"sks": 2, "nilai": "B", "bobot": 6}
}

# Menghitung jumlah SKS dan nilai total bobot
jumlah_sks = 0
total_bobot = 0

for mata_kuliah in matakuliah.values():
    jumlah_sks += mata_kuliah["sks"]
    total_bobot += mata_kuliah["sks"] * mata_kuliah["bobot"]

# Menghitung IPK
ipk = total_bobot / jumlah_sks

# Mencetak hasil
print(f"Jumlah SKS: {jumlah_sks}")
print(f"Nilai IPK: {ipk:.2f}")
