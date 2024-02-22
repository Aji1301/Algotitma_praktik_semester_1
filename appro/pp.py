# import mysql.connector

# db = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='db_uty',
# )

# if db.is_connected():
#     print("Connected")

def insert_data(db):
    cursor = db.cursor()
    nim = input("Masukan NIM     : ")
    nama = input("Masukan nama   : ")
    prodi = input("Masukan prodi : ")
    nilai = input("Masukan nilai : ")

    sql = "INSERT INTO mahasiswa (nim, nama, prodi, nilai_) VALUES (%s, %s, %s, %s)"
    val = (nim, nama, prodi, nilai)
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil ditambahkan".format(cursor.rowcount))

def show_data(db):
    cursor = db.cursor()
    sql = "SELECT * FROM mahasiswa"
    cursor.execute(sql)
    tangkap = cursor.fetchall()

    for data in tangkap:
        print("======================")
        print(">>> DATA MAHASISWA <<<")
        print("NIM               : ", data[0])
        print("NAMA              : ", data[1])
        print("prodi             : ", data[2])
        print("NILAI             : ", data[3])
        print("======================")
        # print(data)

def edit_data(db):
    cursor = db.cursor()
    nim_lama = input("Masukan NIM data yang akan diubah : ")
    nim_baru = input("Masukan NIM baru     : ")
    nama_baru = input("Masukan nama baru   : ")
    prodi_baru = input("Masukan prodi baru : ")
    nilai_baru = input("Masukan nilai baru : ")

    sql = "UPDATE mahasiswa SET nim=%s, nama=%s, prodi=%s, nilai_=%s WHERE nim=%s"
    val = (nim_baru, nama_baru, prodi_baru, nilai_baru, nim_lama)
    cursor.execute(sql, val)
    db.commit()

    print("{} data berhasil diubah".format(cursor.rowcount))

def delete_data(db):
    cursor = db.cursor()
    nim_dihapus = input("Pilih NIM yang ingin dihapus : ")
    sql = "DELETE FROM mahasiswa WHERE NPM=%s"
    val = (nim_dihapus,)
    cursor.execute(sql, val)
    db.commit()

    print("{} data berhasil dihapus".format(cursor.rowcount))

def search_data(db):
    cursor = db.cursor()
    keywords = input("Masukan kunci nim : ")
    sql = "SELECT * FROM mahasiswa WHERE nim LIKE %s"
    val = (keywords,)

    cursor.execute(sql, val)
    r = cursor.fetchall()

    if cursor.rowcount == 0:
        print("Tidak ada data yang di tampilkan")
    else:
        for data in r :
            print("========================")
            print(">>>> DATA MAHASISWA <<<<")
            print("========================")
            print("NIM       : ", data[0])
            print("NAMA      : ", data[1])
            print("PRODI     : ", data[2])
            print("NILAI     : ", data[3])
            print("========================")



# insert_data(db)
# show_data(db)
# edit_data(db)
# delete_data(db)
# search_data(db)

while True:
    print("\nMenu:")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Edit Data")
    print("4. Hapus Data")
    print("5. Mencari Data")
    print("6. Keluar")

    pilihan = input("Pilih nomor menu (1-6): ")

    if pilihan == '1':
        insert_data(db)
    elif pilihan == '2':
        show_data(db)
    elif pilihan == '3':
        edit_data(db)
    elif pilihan == '4':
        delete_data(db)
    elif pilihan == '5':
        search_data(db)
    elif pilihan == '6':
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid. Silakan masukkan nomor menu yang benar.")
