
list_npm = [5,2,3,4,1,1,3,2,1]

def tambah_nim():
    nim = input("Masukkan NIM: ")
    list_npm.append({"nim": nim,})
    print("Data berhasil ditambahkan.")

def tampilkan_data():
    if not list_npm:
        print("Belum ada npm yang di cari.")
    # elif list_npm == 5:
    #     print("false")
    # elif list_npm == 4:
    #     print("true")
    # elif list_npm == 3:
    #     print("false")
    # elif list_npm == 2:
    #     print("false")
    # elif list_npm == 1:
    #     print("false")
    
    else:
        print("nim ")
        for mahasiswa in list_npm:
            print(f"{mahasiswa['nim']}")

while True:
    print("\nMenu:")
    print("1. Tambah Data.")
    print("2. Tampilkan Data.")
    print("0. Exit.")

    pilihan = input("Masukkan pilihan Anda: ")

    if pilihan == '1':
        tambah_nim()
    elif pilihan == '2':
        tampilkan_data()
    elif pilihan == '0':
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")