def kalkulator(x, y, operasi):
    if operasi == "penjumlahan":
        return x + y
    elif operasi == "pengurangan":
        return x - y
    elif operasi == "perkalian":
        return x * y
    elif operasi == "pembagian":
        if y != 0:
            return x // y  # Pembagian bilangan bulat
        else:
            return "Tidak bisa membagi dengan nol"
    else:
        return "Operasi tidak dikenali"

# Input dari pengguna
x = int(input("Masukkan angka pertama: "))
y = int(input("Masukkan angka kedua: "))
operasi = input("Pilih operasi (penjumlahan, pengurangan, perkalian, pembagian): ").lower()

# Menghitung hasil
hasil = kalkulator(x, y, operasi)

# Menampilkan hasil
print(f"Hasil dari {operasi} adalah: {hasil}")
