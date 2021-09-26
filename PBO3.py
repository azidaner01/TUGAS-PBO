class sepatu:
    def __init__ (self, warna, tipe, merk):
        self.warna = warna
        self.tipe  = tipe
        self.merk  = merk
    
    def printname(self):
        print(self.warna)
        print(self.tipe)
        print(self.merk)

class casual(sepatu):
    def __init__(self, warna, tipe, merk):
        sepatu.__init__(self, warna, tipe,  merk)
        self.penggunaan = "sekolah"

    def sepcasual(self):
        print("penggunaan  : ", self.penggunaan)
        print("Warna       : ", self.warna)
        print("tipe        : ", self.tipe)
        print("Merk        : ", self.merk)

class running(sepatu):
    def __init__(self, warna, tipe, merk):
        sepatu.__init__(self, warna, tipe, merk)
        self.penggunaan = "olahraga"

    def seprunning(self):
        print("penggunaan  : ", self.penggunaan)
        print("Warna       : ", self.warna)
        print("tipe        : ", self.tipe)
        print("Merk        : ", self.merk)

class basket(sepatu):
    def __init__(self, warna, tipe, merk):
        sepatu.__init__(self, warna, tipe, merk)
        self.penggunaan = "Main basket"

    def sepbasket(self):
        print("penggunaan  : ", self.penggunaan)
        print("Warna       : ", self.warna)
        print("tipe        : ", self.tipe)
        print("Merk        : ", self.merk)

a = casual("Hitam", "Suede", "Puma")
b = running("Biru", "Air zoom", "Nike")
c = basket("Merah", "D'Rose", "Adidas")

a.sepcasual()
b.seprunning()
c.sepbasket()