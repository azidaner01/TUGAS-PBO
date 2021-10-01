class Sepatu:
    def intro(self):
        print("Sepatu Merupakan salah satu alas kaki yang sering digunakan")

    def deskripsi(self):
        print("Ada beberapa jenis sepatu, ada sepatu olahraga dan ada juga untuk sekolah")

class Sepolahraga(Sepatu):
    def deskripsi(self):
        print("Sepatu olahraga merupakan sepatu yang terbuat dari bahan yang nyaman untuk berolahraga dan style nya lebih beragam")

class Sepsekolah(Sepatu):
    def deskripsi(self):
        print("Sepatu sekolah merupakan sepatu yang memiliki style yang lebih monoton seperti hitam dan putih dan biasanya memiliki bahan yang lebih kaku")

obj_Sepatu = Sepatu()
obj_Sepolahraga = Sepolahraga()
obj_Sepsekolah = Sepsekolah()

obj_Sepatu.intro()
obj_Sepatu.deskripsi()

obj_Sepolahraga.deskripsi()

obj_Sepsekolah.deskripsi()