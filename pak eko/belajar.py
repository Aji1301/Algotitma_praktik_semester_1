belanja = int(input("total barang"))

if belanja > 50000:
    print("selamat anda mendapt diskon 5%")
else:
    print("tidak ada diskon")
    diskon = belanja * 5/100
    bayar = belanja - diskon

    print(f"selamat nilai, {belanja}")
    print(f"selamat belanja, {diskon}")
    print(f"bayarnya, {bayar}")