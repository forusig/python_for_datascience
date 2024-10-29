class Mahasiswa:
    def __init__(self, nama, nim, semester):
        self.__nama = nama           # contoh implementasi encapsulation (menyembunyikan atribut menggunakan __)
        self.__nim = nim             
        self.__semester = semester   

    def get_info(self):
        print(f"Nama: {self.__nama}, NIM: {self.__nim}, Semester: {self.__semester}")

    def set_semester(self, semester_baru):
        if semester_baru > 0:
            self.__semester = semester_baru
        else:
            print("Semester harus lebih dari 0")

    def get_semester(self):
        return self.__semester
