from animal12 import *

class burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, aktivitas, keistimewaan):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.aktivitas = aktivitas
        self.keistimewaan = keistimewaan

    def cetak_burung(self):
        super().cetak()
        print("aktivitas \t: ", self.aktivitas,"\nkeistimewaan \t : ", self.keistimewaan)


merpati = burung ("merpati", "jagung", "pohon", "Bertelur", "makan_minum_menikah", "terbang_tinggi")
merpati.cetak_burung()
