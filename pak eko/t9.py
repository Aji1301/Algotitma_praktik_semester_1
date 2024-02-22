import random

min_value = 1
max_value = 10
max_attempts = 3

for attempt in range(1, max_attempts + 1):
    aku = int(input("Masukkan angka tebakan anda = "))
    x = random.randint(min_value, max_value)

    if aku == x:
        print("Anda Menang")
        break
    else:
        print("Angka sebenarnya adalah", x)
        if attempt < max_attempts:
            print(f"Coba lagi, kesempatan {max_attempts - attempt} lagi.")
        else:
            print("Kesempatan habis. Anda kalah.")