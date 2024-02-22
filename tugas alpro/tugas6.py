def Hitung_HurufAngka():
    s = input("input a srting = ")
    d = l = 0
    for c in s:
        if c.isdigit():
            d = d+1
        elif c.isalpha():
            l = l+1
        else:
            pass
    print("letters", 1)
    print("Digits", d)

def utama():
    print("Program Hitung Angka dan Huruf")
    Hitung_HurufAngka()
    print("selesai")
