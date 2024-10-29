def daftar_nilai(*args):
    total_nilai = 0
    for nilai in args:
        total_nilai += nilai
    rata_rata = total_nilai / len(args)
    return f"Total Nilai: {total_nilai}, Rata-rata: {rata_rata}"

# Contoh penggunaan dengan inputan
jumlah_nilai = int(input("Berapa jumlah nilai yang ingin dimasukkan? "))
nilai_mahasiswa = []

for i in range(jumlah_nilai):
    nilai = float(input(f"Masukkan nilai ke-{i+1}: "))
    nilai_mahasiswa.append(int(nilai))  # Mengonversi float menjadi int

# Memanggil fungsi dengan args
hasil = daftar_nilai(*nilai_mahasiswa)

# Menampilkan hasil
print(hasil)
