# Meminta input dari pengguna
tinggi = int(input("Masukkan tinggi segitiga: "))

# Pola segitiga naik dan turun menggunakan satu for loop
for i in range(1, tinggi * 2):
    if i <= tinggi:
        print('*' * i)  # Pola naik
    else:
        print('*' * (tinggi * 2 - i))  # Pola turun 
        #contoh: misal input nya 7 dan nilainya sudah lebih besar dari 7 maka : 7 x 2 = 14 - 8 (nilai i seharusnya) = 6
        #dan seterusnya pun begitu, misal seharusnya bintang sudah angka 9 namun akan di proses : 7x2= 14 - 9 = 5
