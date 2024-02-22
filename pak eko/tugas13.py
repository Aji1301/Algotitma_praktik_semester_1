def main():
    print("===== Aplikasi Belanja Diskon =====")
    l_nama_barang = []
    l_qty = []
    l_harga_satuan = []

    while True:
        nama_barang = input("nama barang (t untuk berhenti):")
        if nama_barang == 't':
            break
        qty = int(input("qty barang:"))
        harga_satuan = int(input("masukan harga satuan : "))

        l_nama_barang.append(nama_barang)
        l_qty.append(qty)
        l_harga_satuan.append(harga_satuan)

    total_per_prduk = [a*b for a,b in zip(l_qty, l_harga_satuan)]
    total_belanja = sum(total_per_prduk)

    diskon = 0.1 if total_belanja > 150000 else 0

    potongan = total_belanja * diskon
    bayar = total_belanja - potongan

    uang = int(input("Masukan Uang : "))
    kembalian = uang - bayar  
    # print(f"Rp.{kembalian:2f}")



    print("\n===========STRUK KEMBALIAN=============")
    print( f"nama barang\tQTY\tHarga Satuan\tTotal")
    for i in range(len(l_nama_barang)):
        print(f"{l_nama_barang[i]}\t\t{l_qty[i]}\t\t{l_harga_satuan[i]}\t{total_per_prduk[i]}\n")
        
    print(f"Total bayar:\t\t\t\t{bayar}")
    print(f"Bayar:\t\t\t\t\t{uang}")
    print(f"Kemabalian:\t\t\t\t{kembalian}")

if __name__ == "__main__" :
    main()
