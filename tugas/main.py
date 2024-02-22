
# lanjutan
'''class Dokter:
    def __init__(self, nama):
        self.nama = nama

    def konsultasi(self, pasien):
        print(f"Selamat datang di konsultasi dengan Dr. {self.nama}")
        print("Silakan jawab pertanyaan-pertanyaan berikut:")
        gejala = input("1. Deskripsikan gejala Anda: ")
        riwayat_medis = input("2. Sebutkan riwayat medis Anda secara singkat: ")
        pemeriksaan_fisik = input("3. Apakah Anda pernah menjalani pemeriksaan fisik? (ya/tidak): ")

        if pemeriksaan_fisik.lower() == "ya":
            diagnosis = input("4. Apa hasil pemeriksaan fisik tersebut? Diagnosis: ")
        else:
            diagnosis = input("4. Berdasarkan deskripsi Anda, apa diagnosis awal Anda: ")

        rencana_pengobatan = input("5. Rencana pengobatan apa yang Anda rekomendasikan: ")

        print(f"Dr. {self.nama} mengatakan: {rencana_pengobatan}")

        tindak_lanjut = input("6. Apakah Anda memiliki pertanyaan atau kekhawatiran? (ya/tidak): ")

        if tindak_lanjut.lower() == "ya":
            pertanyaan = input("7. Silakan ajukan pertanyaan Anda: ")
            print(f"Dr. {self.nama} menjawab: {pertanyaan}")

        print("Terima kasih atas konsultasi ini. Silakan ikuti rencana pengobatan yang telah diberikan.")

        return rencana_pengobatan


class Apoteker:
    def __init__(self):
        self.obat = {}

    def tambah_obat(self, nama_obat, stok):
        self.obat[nama_obat] = stok

    def beli_obat(self, pasien, rencana_pengobatan):
        print(f"Selamat datang di apotek. Silakan pesan obat sesuai rekomendasi dokter.")
        obat_pesanan = input("Daftar obat yang Anda pesan (pisahkan dengan koma jika lebih dari satu): ").split(",")

        total_harga = 0

        for obat in obat_pesanan:
            if obat in self.obat and self.obat[obat] > 0:
                total_harga += 50  # Harga per unit obat
                self.obat[obat] -= 1
            else:
                print(f"Maaf, obat {obat} tidak tersedia saat ini.")

        print(f"Terima kasih, {pasien['nama']}! Obat Anda akan segera diproses. Total biaya: ${total_harga}")
        print("Jangan lupa untuk mengikuti resep pengobatan yang diberikan oleh dokter.")

# Program utama
if __name__ == "__main__":
    nama_dokter = "Smith"  # Nama dokter
    dokter_smith = Dokter(nama_dokter)
    
    nama_pasien = input("Silakan masukkan nama Anda: ")
    pasien = {"nama": nama_pasien}

    rencana_pengobatan = dokter_smith.konsultasi(pasien)

    apoteker = Apoteker()
    apoteker.tambah_obat("Obat A", 10)
    apoteker.tambah_obat("Obat B", 20)
    apoteker.tambah_obat("Obat C", 15)

    apoteker.beli_obat(pasien, rencana_pengobatan)'''


'''
nama_obat1 = "paracetamol"
nama_obat2 = "alpara"
nama_obat3 = "amoxicilin"

def pertanyaan():
    penyakit = input("Apa gejala Anda: ")

    if "pusing" in penyakit.lower():
        print(nama_obat1)
    elif "demam" in penyakit.lower():
        print(nama_obat2)
    elif "infeksi" in penyakit.lower():
        print(nama_obat3)
    else:
        print("Maaf, kami tidak dapat memberikan rekomendasi obat untuk gejala tersebut.")

pertanyaan()
'''