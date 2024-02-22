jumlah_mata_kuliah = int(input("msukan jumlah mata kuliah:"))

jumlah_SKS = 0
total_nilai = 0

for i in range(jumlah_mata_kuliah):
    sks = int(input(f"masukan jumlah SKS MK ke-{i + 1}:"))
    nilai = float(input(f"masukan nilai mata kuliah ke-{i + 1}:"))

    bobot = sks * nilai
    total_nilai += bobot
    jumlah_SKS += sks

ipk = total_nilai / jumlah_SKS

print(f"jumlah sks yang di ambil: {jumlah_SKS}")
print(f"IPK mahasiswa: {ipk}")
