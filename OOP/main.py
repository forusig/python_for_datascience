from akademik.mahasiswa import Mahasiswa
from akademik.dosen import Dosen
from akademik.program_studi import ProgramStudi
from kampus.universitas import Universitas

def main():
    # Membuat objek Mahasiswa
    mahasiswa1 = Mahasiswa("Bilgis", "123456", 5)
    mahasiswa1.get_info() #contoh implementasi invoke

    # Menggunakan setter untuk memperbarui semester
    # contoh implementasi encapsulation
    mahasiswa1.set_semester(6)
    print(f"Semester diperbarui: {mahasiswa1.get_semester()}")
    
    print("\n--- Program Studi ---")
    # Mahasiswa dengan program studi (multilevel inheritance)
    mahasiswa_prodi = ProgramStudi("Ayu", "654321", 4, "Informatika")
    mahasiswa_prodi.get_info()

    print("\n--- Dosen ---")
    # Membuat objek Dosen
    dosen1 = Dosen("Pak Budi", "987654", "Pemrograman Web")
    dosen1.mengajar()

    print("\n--- Universitas ---")
    # Polymorphism dalam Universitas
    univ = Universitas("Universitas Teknologi")
    univ.tambah_anggota(mahasiswa1)
    univ.tambah_anggota(mahasiswa_prodi)
    # Dosen tidak punya get_info, jadi kita hanya bisa memanggil mengajar() pada dosen di sini
    # Tambahkan anggota kampus
    univ.tampilkan_anggota()

if __name__ == "__main__":
    main()
