# jumlah_ganjil = 0 
# for i in range(1, 100):
#     if i % 2 == 0:
#         jumlah_ganjil += 1
# print( 'jumlah bilangan ganjil', jumlah_ganjil)

jumlah_huruf = 0 
kalimat = input('masukan kalimat =')
for i in kalimat :
    if i =="":
        continue
    jumlah_huruf += 1

print(kalimat, jumlah_huruf)