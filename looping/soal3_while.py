# Contoh menggunakan while dan if-elif-else
hitung = 1
i = int(input("masukan angka: "))

while hitung <= i:
    if hitung % 3 == 0:
        print(f"{hitung} adalah kelipatan 3")
    elif hitung % 2 == 0:
        print(f"{hitung} adalah bilangan genap")
    else:
        print(f"{hitung} adalah bilangan ganjil")
    hitung += 1
