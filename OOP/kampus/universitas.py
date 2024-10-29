class Universitas:
    def __init__(self, nama_univ):
        self.nama_univ = nama_univ
        self.anggota = []  # List untuk menyimpan mahasiswa dan dosen

    def tambah_anggota(self, orang):
        self.anggota.append(orang)

    def tampilkan_anggota(self):
        print(f"Anggota di {self.nama_univ}:")
        for orang in self.anggota:
            orang.get_info()  # Polymorphism, bisa memanggil get_info() dari Mahasiswa atau ProgramStudi
