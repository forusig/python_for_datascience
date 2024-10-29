from .mahasiswa import Mahasiswa

class ProgramStudi(Mahasiswa): #contoh implementasi inhheritance 
    # class program studi mewarisi class mahasiswa
    def __init__(self, nama, nim, semester, prodi):
        super().__init__(nama, nim, semester)
        self.prodi = prodi

    def get_info(self):
        #contoh implementasi super()
        super().get_info()  # Memanggil method dari class Mahasiswa
        print(f"Program Studi: {self.prodi}")
