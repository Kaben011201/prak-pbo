class Capil:
    __daftar=[] #__daftar adalah atribut privat yang dimiliki oleh Capil dan tidak dapat diakses pada kelas lain dan main program
    def __init__(self, nama, no_akte, alamat, no_hp):
        self.nama=nama
        self.__no_akte=no_akte
        self.alamat=alamat
        self._no_hp=no_hp
        Capil.__daftar.append(self.__no_akte)  #Contohnya adalah bagian ini yang dapat diakses pada method walaupun termasuk atribut privat

    def _ubahnohp(self, change):
        self._no_hp=change
    
    def caridata(self, cari):
        if cari in Capil.__daftar:
            print("Data ditemukan")
        else:
            print("Data tidak ada")

    def biodata(self):
        #fungsi public, proctect dan privat hanya dapat diakses pada kelas, dan method yang ada dalam kelas tersebut
        #namun fungsi privat tidak dapat diakses pada kelas lain dan main program
        print(f"Nama : {self.nama}\nNo Akte : {self.__no_akte}\nAlamat : {self.alamat}\nNo HP : {self._no_hp}\n")

Person1=Capil("Bendry", 101201, "Sukarame", "082233445566")
Person2=Capil("Arya", 211002, "Cikarang", "082131415161")
Person3=Capil("Septo", 101201, "Jakarta", "082567891011")

#fungsi biodata() adalah fungsi yang bersifat public
Person1.biodata()

Person1._ubahnohp("082344445555") #fungsi proctect dapat diakses pada main sama seperti fungsi public

print("Nama : ", Person1.nama) #bagian ini dapat dieksekusi karena memanggil atribut public
#print("No Akte :", Person1.__no_akte) -->Bagian ini akan membuat error pada main program karena memanggil atribut private
print()
Person1.biodata()

cari=int(input("Masukkan No Akte dari data yang ingin dicari : "))
Person1.caridata(cari)
