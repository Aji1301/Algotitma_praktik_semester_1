import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='', #isi sesuai nama data yg ada di mysql mu
)

if db.is_connected():
    print("Connected")

    # UNTUK MENAMBAH DATA
def insert_data(db):
    cursor = db.cursor()
    nim       = input("Masukan NIM : ")
    nama     = input("Masukan nama : ")
    prodi   = input("Masukan prodi : ")
    matkul = input("Masukan matkul : ")

    sql = "INSERT INTO mahasiswa (nim, nama, prodi, matkul) VALUES (%s, %s, %s, %s)"
    val = (nim, nama, prodi, matkul)
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil ditambahkan".format(cursor.rowcount))

    # UNTUK MENAMPILKAN SEMUA DATA
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
        

while True:
    print("\nMenu:")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Selesai")

    pilihan = input("Pilih nomor menu [1/2] :") 

    if pilihan == "1":
        insert_data(db)
    elif pilihan == "2":
        show_data(db)
    elif pilihan == "3":
        print("Selesai untuk menambah data")
        break
    else:
        print("Pilihan tidak valid, mohon memilih lagi dengan benar")





    # nim = input("Masukan NIM     : ")
    # nama = input("Masukan nama    : ")
    # prodi = input("Masukan prodi   : ")
    # matkul = input("Masukan Matkul  : ")
    # nilaiUH1 = int(input("Masukan nilai UH 1 : "))
    # nilaiUH2 = int(input("Masukan nilai UH 2 : "))
    # nilaiUTS = int(input("Masukan nilai UTS  : "))
    # nilaiUAS = int(input("Masukan nilai UAS  : "))

    # jmlUH = nilaiUH1+nilaiUH2
    # rata_rata = jmlUH/2

    # akhirUH = 0.3*rata_rata
    # akhirUTS = 0.3*nilaiUTS
    # akhirUAS = 0.4*nilaiUAS
    # total_nilai = akhirUH+akhirUTS+akhirUAS

    # if total_nilai >= 0 and total_nilai < 20 :
    #     nilai_huruf = "E"
    # elif total_nilai >= 20 and total_nilai < 40 :
    #     nilai_huruf = "D"
    # elif total_nilai >= 40 and total_nilai < 60 :
    #     nilai_huruf = "C"
    # elif total_nilai >= 60 and total_nilai < 80 :
    #     nilai_huruf = "B"
    # else: nilai_huruf = "A"


    # nim = input("Masukan NIM     : ")
    # nama = input("Masukan nama    : ")
    # prodi = input("Masukan prodi   : ")
    # matkul = input("Masukan Matkul  : ")
    # print("--- Nilai ke 1 ---")
    # nilaiUH1 = float(input("Nilai Harian 1: "))
    # print(nilaiUH1)
    
    # print("--- Nilai ke 2 ---")
    # nilaiUH2 = float(input("Nilai Harian 2: "))
    # jmlUH = nilaiUH1+nilaiUH2
    # rata_rata = jmlUH/2

    # print(rata_rata)
    # nilaiUTS = float(input("Nilai UTS: "))
    # nilaiUAS = float(input("Nilai UAS: "))
    # print(rata_rata, nilaiUTS, nilaiUAS)
    # print("--- Total Nilai ---")
    
    # akhirUH = 0.3*rata_rata
    # akhirUTS = 0.3*nilaiUTS
    # akhirUAS = 0.4*nilaiUAS
    # total_nilai = akhirUH+akhirUTS+akhirUAS
    
    # print("Total nilai yang didapat ",total_nilai)
    # if total_nilai > 0 and total_nilai < 20:
    #     nilai_huruf - "E"
    # elif total_nilai > 20 and total_nilai < 40:
    #     nilai_huruf = "D"
    # elif total_nilai > 40 and total_nilai < 60:
    #     nilai_huruf = "C"
    # elif total_nilai > 60 and total_nilai < 80 :
    #     nilai_huruf = "B"
    # else: nilai_huruf = "A"