# def data():
#     nim = input('masukan nim:')
#     nama = input('masukan nama:')
#     asal = input('masukan asal:')

#     nim_tetap = "5019"
#     nama_tetap = "naruto"
#     asal_tetap = "jepang"

#     if nim ==  nim_tetap:
#         print("nim salah")
#         if nama == nama_tetap:
#         print("nama salah")
#                 if asal == asal_tetap:
#                 print("nama salah")

# data()
# data_mahasiswa = []

# def data():
#     nim = input('masukan NIM: ')
#     nama = input('masukan Nama:')
#     asal = input('masukan Asal:')
#     mahasiswa = {"NIM": nim, "Nama": nama, "asal": asal}
#     print("Data berhasil dimasukan.")
#     data_mahasiswa.append(mahasiswa)
#     print("Data berhasil dimasukan.")

# def tampilkan_data():
#     if not data_mahasiswa:
#         print("Belum ada data yang di masukan.")
#     else:
#         ("Data yang tersimpan")
#         for idx, mahasi









    # print("\n1. Masukan Data")
    # print("2.")

def masukkan_data():
    nim = input("Masukkan NIM: ")
    nama = input("Masukkan Nama: ")
    asal = input("Masukkan Asal: ")
    mahasiswa = {"NIM": nim, "Nama": nama, "Asal": asal}
    print("Data berhasil dimasukkan.")

# def tampilkan_data():
#     if not data_mahasiswa:
#         print("Belum ada data yang dimasukkan.")
#     else:
#         print("Data yang tersimpan:")
#         for idx, mahasiswa in enumerate(data_mahasiswa, 1):
#             print(f"{idx}. NIM: {mahasiswa['NIM']}, Nama: {mahasiswa['Nama']}, Asal: {mahasiswa['Asal']}")

# def hapus_data():
#     if not data_mahasiswa:
#         print("Belum ada data yang dimasukkan.")
#     else:
#         tampilkan_data()
#         indeks_hapus = int(input("Masukkan nomor data yang ingin dihapus: "))
#         if 1 <= indeks_hapus <= len(data_mahasiswa):
#             data_mahasiswa.pop(indeks_hapus - 1)
#             print("Data berhasil dihapus.")
#         else:
#             print("Nomor data tidak valid.")

while True:
    print("\n1. Masukkan data.")
    # print("2. Tampilkan data.")
    # print("3. Hapus data.")
    # print("0. Exit.")
    
    pilihan = input("Masukkan pilihan anda: ")

    if pilihan == '1':
        masukkan_data()
    # elif pilihan == '2':
    #     tampilkan_data()
    # elif pilihan == '3':
    #     hapus_data()
    elif pilihan == '0':
        break
    else:
        print("Pilihan tidak valid. Silakan pilih lagi.")