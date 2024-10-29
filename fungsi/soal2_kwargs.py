#fungsi kwargs
def data_mahasiswa(**kwargs):
    print("\nData Mahasiswa:")
    for kunci, nilai in kwargs.items():
        print(f"{kunci}: {nilai}")

# Input dari pengguna
nama = input("Masukkan nama: ")
umur = input("Masukkan umur: ")
jurusan = input("Masukkan jurusan: ")
universitas = input("Masukkan universitas: ")

# Memanggil fungsi dengan inputan pengguna
data_mahasiswa(nama=nama, umur=umur, jurusan=jurusan, universitas=universitas)
