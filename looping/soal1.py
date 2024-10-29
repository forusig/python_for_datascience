#Buatlah script yang dapat memberikan output berupa pola segitiga siku-siku berdasarkan jumlah bintang yang diinput.
# fungsi input
tinggi = int(input("Masukkan tinggi segitiga: "))

# Loop untuk membuat pola segitiga (menggunakan fungsi for range)
for i in range(1, tinggi + 1):
    print('*' * i)
