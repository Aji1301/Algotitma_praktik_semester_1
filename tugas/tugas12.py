# import mysql.connector

# db = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='db_uty',
# )

# if db.is_connected():
#     print("Connected")




def nilai_uas():

    print("----Nilai ke 1----")
    nilaiUH1 = float(input("Nilai harian : "))
    print(nilaiUH1)
    print("----NILAI KE 2----")
    nilaiUH2 = float(input("Nilai harian : "))
    jumlahUH = nilaiUH1 + nilaiUH2
    rata_rata = jumlahUH/2
    print(rata_rata)

    nilaiUTS = float(input("Nilai UTS : "))
    nilaiUAS = float(input("Nilai UAS : "))
    print(rata_rata,nilaiUTS,nilaiUAS)

    print("----Total Nilai----")
    akhirUH = 0.3*rata_rata
    akhirUTS = 0.3*nilaiUTS
    akhirUAS = 0.4*nilaiUAS
    total_nilai = akhirUH+akhirUTS+akhirUAS
    print("Total nilai yang didapat :",total_nilai)

    if total_nilai >= 0 and total_nilai < 20:
        nilai_huruf = "E"
    elif total_nilai >= 20 and total_nilai < 40:
        nilai_huruf = "D"
    elif total_nilai >= 40 and total_nilai < 60:
        nilai_huruf = "C"
    elif total_nilai >= 60 and total_nilai < 70:
        nilai_huruf = "B"
    else: nilai_huruf = "A"
    print("Total nilai dalam huruf",nilai_huruf)

nilai_uas() 

