class Beta:
  def __init__(self, nama, nim, siakad, jumlah_sks):
    self.nama=nama
    self.nim=nim
    self.siakad=siakad
    self.jumlah_sks=jumlah_sks

  def ganti(self, ganti):
    del(self.siakad)
    self.siakad=ganti

  def show(self):
    print(f'Nama       : {self.nama}\nNIM        : {self.nim} \nKelas      : {self.siakad}\nJumlah sks : {self.jumlah_sks}')
    
mahasiswa=Beta("Bendry","121140111","RB",66)
mahasiswa.show()

x=input("\nApakah ingin ganti kelas? ")
if x=="ya":
  mahasiswa.siakad=input("Masukkan kelas : ")
  print("")
mahasiswa.show()
