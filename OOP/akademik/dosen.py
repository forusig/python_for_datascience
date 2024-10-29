class Dosen:
    def __init__(self, nama, nip, mata_kuliah):
        self.nama = nama
        self.nip = nip
        self.mata_kuliah = mata_kuliah

    def mengajar(self):
        print(f"Dosen {self.nama} mengajar mata kuliah {self.mata_kuliah}")
