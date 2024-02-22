import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'db_uty',
)

if db.is_connected():
    print("Connected")

def insert_data(db):
    cursor = db.cursor()


    cursor = db.cursor()

    nim = input("Masukan NIM       : ")
    nama = input("Masukan nama     : ")
    prodi = input("Masukan prodi   : ")
    matkul = input("Masukan matkul  : ")
    nilaiUH1 = int(input("Masukan nilai UH 1 : "))
    nilaiUH2 = int(input("Masukan nilai UH 2 : "))
    nilaiUTS = int(input("Masukan nilai UTS  : "))
    nilaiUAS = int(input("Masukan nilai UAS  : "))

    jmlUH = nilaiUH1 + nilaiUH2
    rata_rata = jmlUH / 2

    akhirUH = 0.3 * rata_rata
    akhirUTS = 0.3 * nilaiUTS
    akhirUAS = 0.4 * nilaiUAS
    total_nilai = akhirUH + akhirUTS + akhirUAS

    if 0 <= total_nilai < 20:
        nilai_huruf = "E"
    elif 20 <= total_nilai < 40:
        nilai_huruf = "D"
    elif 40 <= total_nilai < 60:
        nilai_huruf = "C"
    elif 60 <= total_nilai < 80:
        nilai_huruf = "B"
    else:
        nilai_huruf = "A"

    sql = "INSERT INTO mahasiswa (nim, nama, prodi, matkul, nilai_UH1, nilai_UH2, nilai_UTS, nilai_UAS, total_nilai, nilai_huruf) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (nim, nama, prodi, matkul, nilaiUH1, nilaiUH2, nilaiUTS, nilaiUAS, total_nilai, nilai_huruf)

    try:
        cursor.execute(sql, val)
        db.commit()
        print("{} data berhasil ditambahkan".format(cursor.rowcount))

    except Exception as e:
        print("Error:", e)
        db.rollback()

    finally:
        cursor.close()

    db.close()


def show_data(db):
    cursor = db.cursor()
    sql = "SELECT * FROM mahasiswa"

    cursor.execute(sql,)
    tangkap = cursor.fetchall()

    for data in tangkap:
        print("======================")
        print(">>> DATA MAHASISWA <<<")
        print("NIM               : ", data[0])
        print("NAMA              : ", data[1])
        print("PRODI             : ", data[2])
        print("MATKUL            : ", data[3])
        print("TOTAL NILAI       : ", data[8])
        print("NILAI HURUF       : ", data[9])
        print("======================")

def edit_data(db):
        cursor = db.cursor()

        # Input nim and field to be updated
        nim_lama = input("Masukkan NIM data yang akan diubah: ")
        # Select existing data based on NIM
        sql_select = "SELECT * FROM mahasiswa WHERE nim=%s"
        cursor.execute(sql_select, (nim_lama,))
        result = cursor.fetchall()

        if not result:
            print("Data dengan NIM {} tidak ditemukan.".format(nim_lama))
            return
        data = result[0]

        print("======================")
        print(">>> DATA MAHASISWA <<<")
        print("NIM               : ", data[0])
        print("NAMA              : ", data[1])
        print("PRODI             : ", data[2])
        print("MATKUL            : ", data[3])
        print("TOTAL NILAI       : ", data[8])
        print("NILAI HURUF       : ", data[9])
        print("======================")

        print("==== OPSI PERUBAHAN ====")
        print("[1]. Ubah NIM")
        print("[2]. Ubah NAMA")
        print("[3]. Ubah PRODI")
        print("========================")

        pilih_data = input("Data yang ingin diubah? (1/2/3): ")
        pilihan = ['nim', 'nama', 'prodi']
        if pilih_data.lower() not in ['1', '2', '3']:
            print("Pilihan field tidak valid.")
            return
        data_baru = input("Masukkan {} baru: ".format(pilihan[int(pilih_data)-1]))
            # UPDATE query
        sql_update = "UPDATE mahasiswa SET {}=%s WHERE nim=%s".format(pilihan[int(pilih_data)-1])
        val = (data_baru, nim_lama)
        cursor.execute(sql_update, val)

        db.commit()
        print("{} data berhasil diubah".format(cursor.rowcount))

def delete_data(db):

    cursor = db.cursor()
    
    nim_dihapus = input("Pilih nim yang ingin di hapus  :")
    sql = "DELETE FROM mahasiswa WHERE nim=%s"
    val = (nim_dihapus,)
    cursor.execute(sql, val)
    db.commit()

    print("{} data berhasil dihapus")


# delete_data(db)
# edit_data(db)
# insert_data(db)
# show_data(db)
    
while True:
    print("\nMenu:")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Edit Data")
    print("4. Hapus Data")
    print("5. Keluar")

    pilihan = input("Pilih nomor menu (1-5): ")

    if pilihan == '1':
        insert_data(db)
    elif pilihan == '2':
        show_data(db)
    elif pilihan == '3':
        edit_data(db)
    elif pilihan == '4':
        delete_data(db)
    elif pilihan == '5':
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid. Silakan masukkan nomor menu yang benar.")