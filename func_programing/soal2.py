#  function lambda yang dieksekusi didalam sebuah fungsi def 
def tambah(a, b):
    # Membuat lambda function untuk melakukan operasi penjumlahan
    penjumlahan = lambda x, y: x + y
    # Menjalankan lambda function
    hasil = penjumlahan(a, b)
    return hasil

# Pemanggilan fungsi
print(tambah(10, 5)) 
