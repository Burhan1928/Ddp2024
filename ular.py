from animal12 import *

class Ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, design, racun):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.design = design
        self.racun = racun

    def cetak_ular(self):
        super().cetak()
        print("Design \t: ", self.design,"\nracun \t : ", self.racun)


anaconda = Ular ("anaconda", "Kambing", "Amazon", "Bertelur", "Batik solo", "Tidak berbisa")
anaconda.cetak_ular()


