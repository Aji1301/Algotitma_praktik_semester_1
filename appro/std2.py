import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='db_uty',
)

if db.is_connected():
    print("Connected")

# def nilaimahasiswa():
    
#     print("--- Nilai ke 1 ---")
#     nilaiUH1 = float(input("Nilai Harian 1: "))
#     print(nilaiUH1)
    
#     print("--- Nilai ke 2 ---")
#     nilaiUH2 = float(input("Nilai Harian 2: "))
#     jmlUH = nilaiUH1+nilaiUH2
#     rata_rata = jmlUH/2

#     print(rata_rata)
#     nilaiUTS = float(input("Nilai UTS: "))
#     nilaiUAS = float(input("Nilai UAS: "))
#     print(rata_rata, nilaiUTS, nilaiUAS)
#     print("--- Total Nilai ---")
    
#     akhirUH = 0.3*rata_rata
#     akhirUTS = 0.3*nilaiUTS
#     akhirUAS = 0.4*nilaiUAS
#     total_nilai = akhirUH+akhirUTS+akhirUAS
    
#     print("Total nilai yang didapat ",total_nilai)
#     if total_nilai > 0 and total_nilai < 20:
#         nilai_huruf - "E"
#     elif total_nilai > 20 and total_nilai < 40:
#         nilai_huruf = "D"
#     elif total_nilai > 40 and total_nilai < 60:
#         nilai_huruf = "C"
#     elif total_nilai > 60 and total_nilai < 80 :
#         nilai_huruf = "B"
#     else: nilai_huruf = "A"
#     print("Total nilai dalam huruf : ",nilai_huruf)

# nilaimahasiswa()

def insert_data(db):
    cursor = db.cursor()

    nim = input("Masukan NIM       : ")
    nama = input("Masukan nama     : ")
    prodi = input("Masukan prodi   : ")
    matkul = input("Masukan nilai  : ")
    nilaiUH1 = int(input("Masukan nilai UH 1 : "))
    nilaiUH2 = int(input("Masukan nilai UH 2 : "))
    nilaiUTS = int(input("Masukan nilai UTS  : "))
    nilaiUAS = int(input("Masukan nilai UAS  : "))

    jmlUH = nilaiUH1+nilaiUH2
    rata_rata = jmlUH/2

    akhirUH = 0.3*rata_rata
    akhirUTS = 0.3*nilaiUTS
    akhirUAS = 0.4*nilaiUAS
    total_nilai = akhirUH+akhirUTS+akhirUAS

    if total_nilai >= 0 and total_nilai < 20 :
        nilai_huruf = "E"
    elif total_nilai >= 20 and total_nilai < 40 :
        nilai_huruf = "D"
    elif total_nilai >= 40 and total_nilai < 60 :
        nilai_huruf = "C"
    elif total_nilai >= 60 and total_nilai < 80 :
        nilai_huruf = "B"
    else: 
        nilai_huruf = "A"


    sql = "INSERT INTO mahasiswa (NPM, nama, prodi, matkul, nilai_UH1, nilai_UH2, nilai_UTS,nilai_UAS,total_nilai, nilai_huruf) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,)"
    val = (nim, nama, prodi, matkul, nilaiUH1, nilaiUH2, nilaiUTS, nilaiUAS, total_nilai, nilai_huruf)
    cursor.execute(sql, val)
    db.commit()

    print("{} data berhasil ditambahkan".format(cursor.rowcount))

insert_data()