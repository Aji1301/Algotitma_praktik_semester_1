list_data = input("masukan npm  :")
list_npm = [5,2,3,4,1,1,3,2,1,]

angka_ganjil = 0 
angka_genap = 0

for angka in list_npm:
    if angka % 2 == 0:
        angka_genap += 1
    else:
        angka_ganjil += 1

print("ini adalah angka ganjil ;",angka_ganjil)
print("ini adalah angka genap :",angka_genap)
print("ini adalah true : 4")