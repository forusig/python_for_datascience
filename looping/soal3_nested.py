# Contoh nested loop dengan if-else
baris = int(input("masukan angka: "))

for i in range(1, baris + 1):
    for j in range(1, i + 1):
        if j % 2 == 0:
            print('A', end=' ')  # Jika bisa di bagi 2 maka akan cetak "A"
        else:
            print('B', end=' ')  # Jika tidak bisa di bagi 2 maka akan setak "B"
    print() 