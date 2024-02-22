import mysql.connector

def insert_data(db):
    with db.cursor() as cursor:
        cursor.execute("INSERT INTO mahasiswa1(NPM, nama, prodi) VALUES(1, 'Naruto', 'IF')")
        db.commit()

        lagi = "y"
        while lagi.lower() == "y":
            npm_baru = input("Tambah no mhs  :")
            nama_baru = input("Tambah nama    :")
            prodi_baru = input("Tambah prodi   :")

            cursor.execute("INSERT INTO mahasiswa1 (NPM, nama, prodi) VALUES (%s, %s, %s)", (npm_baru, nama_baru, prodi_baru))
            db.commit()
            lagi = input("Input lagi (y/t) :")

def isi_table(db):
    with db.cursor() as cursor:
        cursor.execute("SELECT * FROM mahasiswa1")
        for x in cursor.fetchall():
            print(x)

try:
    with mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='db_uty',
    ) as db:
        if db.is_connected():
            print("Connected")

        insert_data(db)
        isi_table(db)

except mysql.connector.Error as err:
    print(f"Error: {err}")
