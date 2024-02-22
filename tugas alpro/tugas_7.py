# # list untuk menyimpan teman-teman
# teman = []

# # pengulangan untuk meminta input teman
# while True:
#     teman_baru = input("Inputkan teman yang ke-{0}: ".format(len(teman)))
#     teman.append(teman_baru)
    
#     lagi = input("Mau isi lagi? (y/t): ")
    
#     if lagi.lower() != 'y':
#         break

# # Tampilkan hasilnya
# print("==============")
# print("Kamu memiliki {} teman".format(len(teman)))
# for i, nama in enumerate(teman):
#     print("•{}".format(nama))


data_mahasiswa = []

def tambah_data():
    nim = input("Masukkan NIM: ")
    nama = input("Masukkan Nama: ")
    asal = input("Masukkan Asal: ")
    data_mahasiswa.append({"nim": nim, "nama": nama, "asal": asal})
    print("Data berhasil ditambahkan.")

def tampilkan_data():
    if not data_mahasiswa:
        print("Belum ada data.")
    else:
        print("nim | nama   | asal")
        print("----|--------|------")
        for mahasiswa in data_mahasiswa:
            print(f"{mahasiswa['nim']} | {mahasiswa['nama']} | {mahasiswa['asal']}")

def hapus_data():
    if not data_mahasiswa:
        print("Belum ada data untuk dihapus.")
    else:
        nim_hapus = input("Masukkan NIM yang ingin dihapus: ")
        for mahasiswa in data_mahasiswa:
            if mahasiswa['nim'] == nim_hapus:
                data_mahasiswa.remove(mahasiswa)
                print(f"Data dengan NIM {nim_hapus} berhasil dihapus.")
                break
        else:
            print(f"Tidak ditemukan data dengan NIM {nim_hapus}.")

while True:
    print("\nMenu:")
    print("1. Tambah Data.")
    print("2. Tampilkan Data.")
    print("3. Hapus Data.")
    print("0. Exit.")

    pilihan = input("Masukkan pilihan Anda: ")

    if pilihan == '1':
        tambah_data()
    elif pilihan == '2':
        tampilkan_data()
    elif pilihan == '3':
        hapus_data()
    elif pilihan == '0':
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")