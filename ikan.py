from animal12 import *

class ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, ukuran, jenis_ikan):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.ukuran = ukuran
        self.jenis_ikan = jenis_ikan

    def cetak_ikan(self):
        super().cetak()
        print("bentuk \t: ", self.ukuran,"\njenis_ikan \t : ", self.jenis_ikan)


gurame = ikan ("gurame", "pelet", "empang", "Bertelur", "bulat", "air tawar")
gurame.cetak_ikan()
