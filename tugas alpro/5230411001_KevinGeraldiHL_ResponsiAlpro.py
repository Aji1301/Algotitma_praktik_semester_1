def programkasir():
    jalankanprogram = int(input("Apakah akan membeli? (1=Ya/2=Tidak)"))
    tagihan = 0
    while jalankanprogram == 1:
        print("==DAFTAR BARANG==\n"
                "(1.) Pensil : Rp. 5000\n"
                "(2.) Buku : Rp. 15000\n"
                "(3.) Penghapus : Rp. 10000\n"
                "(4.) Bolpoin : Rp. 10000")
        barang = int(input("inputlah barang yang mau dibeli(angka): "))
        if barang == 1:
            namabarang = "Pensil"
            harga = 5000
        elif barang == 2:
            namabarang = "Buku"
            harga = 15000
        elif barang == 3:
            namabarang = "Penghapus"
            harga = 10000
        elif barang == 4:
            namabarang = "Bolpoin"
            harga = 10000
        else:
            print("barang tidak ada")
            harga = 0
        jumlahbarang = int(input("masukkan jumlah barang yang mau dibeli: "))
        belanjaan = harga * jumlahbarang
        tagihan = tagihan + belanjaan
        print("tagihan anda adalah Rp.", tagihan)
        diskon = tagihan * 0.3
        uangbayar = int(input("masukkan uang bayar = Rp."))
        kembalian = uangbayar - (tagihan-diskon)
            
    
        print("==DAFTAR BARANG==\n"
            "(1.) Pensil : Rp. 5000\n"
            "(2.) Buku : Rp. 15000\n"
            "(3.) Penghapus : Rp. 10000\n"
            "(4.) Bolpoin : Rp. 10000\n"
            "============================\n"
            "===========Nota=============\n"
            "Beli       :", jumlahbarang, namabarang, "\n"
            "Tagihan    : Rp.", tagihan, "\n"
            "Diskon     : Rp.", diskon, "\n"
            "Uang       : Rp.", uangbayar, "\n"
            "Kembalian  : Rp.", kembalian, "\n"
            "==========================\n"
            "=========================="
            
            )
        tagihan = 0
        jalankan = int(input("Apakah beli lagi? (1=Ya/2=Tidak)"))
        if jalankan == 1:
            jalankanprogram = 1
        else:
            jalankanprogram = 2
    
    print("terima kasih")

#main
programkasir()
        
    