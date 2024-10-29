# Meminta input angka dari pengguna
angka = int(input("Masukkan angka: "))

# Memeriksa kondisi kelipatan
if angka % 3 == 0 and angka % 5 == 0:
    print("fizzbuzz")
elif angka % 3 == 0:
    print("fizz")
elif angka % 5 == 0:
    print("buzz")
else:
    print("Nayy")
