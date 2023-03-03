x=1
username="informatika"
password="12345678"
while x<=3 :
  un=input("Username anda : ")
  pw=input("Password anda : ")

  if un==username and pw==password:
    print("\nBerhasil login!")
    break
  else :
    if x!=3 :
      print("Username atau Password anda salah, coba lagi.")
    else :
      print("Akun anda diblokir karena telah mencapai 3 kali percobaan.")
    x+=1
  print("----------------------------------------------\n")
