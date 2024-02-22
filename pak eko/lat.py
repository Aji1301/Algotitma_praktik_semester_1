import random

nama = ["Anto", "Budi", "Citra", "Devi"]
hari = ["Minggu ke 1", "Minggu ke 2", "Minggu ke 3", "Minggu ke 4"]

random.shuffle(nama)

remaining_names = nama.copy()

print("==========JADWAL MENJAGA IKAN CUPANG===========")
for week in hari:
    name = remaining_names.pop(0)
    print(f"{week}: {name} ({', '.join(remaining_names)})")
    
print("===========SEMANGAT MENJAGA IKAN CUPANG============")


import random

nama = ["Anto","Budi","Citra","Devi"]
hari = ["Minggu ke 1","Minggu ke 2","Minggu ke 3","Minggu ke 4"]

random.shuffle(nama)

nama_tersisa = nama.copy()

print("============== JADWAL MENJAGA IKAN CUPANG ===============")
for i in range(4):
    if i == 0:
        print(f"{hari[i]}: {nama_tersisa[0]} ({','.join(nama_tersisa)})")
    elif i < 3:
        nama = nama_tersisa.pop(0)
        print(f"{hari[i]}: {nama} ({','.join(nama_tersisa)})")
    else:
        print(f"{hari[i]}: {nama_tersisa[0]}")
print("============== SELAMAT MENJAGA IKAN CUPANG ===============")

