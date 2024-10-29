# recursion (memanggil dirinya sendiri)
a = int(input("masukan nilai a: ")) 
b = int(input("masukan nilai b: "))

def hitung(a, b): # fungsi hitung yang berisi dua argumen a dan b
    if b == 0 : #memeriksa apakah nilai b adalah 0
        return 1 # apapun yang di pangkatkan akan menghasilkan nilai 1
    else:
        return a * hitung(a, b-1) # fungsi rekrusi yang memanggil diri sendiri
    
    
hasil = hitung(a, b) # memanggil fungsi hitung dengan arg yang sudah di inputkan
print(hasil)
# proses ini akan terus berjalan sampai semuanya tercukupi
# atau sampai nilai b = 0, 