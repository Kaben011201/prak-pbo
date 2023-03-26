import random

class Robot:
  jumlah_turn=0
  Anta=0
  Alpha=0
  Leca=0
  
  def __init__(self, nama, health, damage):
    self.nama=nama
    self.health=health
    self.damage=damage

  def lakukan_aksi(self, enemy):
    if self.nama == "Antares":
      damage=self.damage
      Robot.Anta+=1
      if Robot.Anta%3 == 0:
        damage*=1.5
      enemy.terima_aksi(damage)

    elif self.nama == "Alphasetia":
      damage=self.damage
      Robot.Alpha+=1
      if Robot.Alpha%2 == 0:
        self.health+=4000
        if self == myrobot:
          print(f"Robotmu ({self.nama}) menambah darah sebanyak 4000 HP")
        else:
          print(f"Robot lawan ({self.nama}) menambah darah sebanyak 4000 HP")
      enemy.terima_aksi(damage)

    elif self.nama == "Lecalicus":
      damage=self.damage
      Robot.Leca+=1
      if Robot.Leca%4 == 0:
        self.health+=7000
        damage*=2
        if self == myrobot:
          print(f"Robotmu ({self.nama}) menambah darah sebanyak 7000 HP")
        else:
          print(f"Robot lawan ({self.nama}) menambah darah sebanyak 7000 HP")
      enemy.terima_aksi(damage)

    if enemy.health <= 0:
      print()
      if self == myrobot:
        print(f"Robotmu ({self.nama}) mengalahkan robot lawan ({enemy.nama})")
      else:
        print(f"Robot lawan ({self.nama}) mengalahkan robotmu ({enemy.nama})")
    
      
  def terima_aksi(self, damage):
    self.health-=damage
    if self == myenemy:
      print(f"Robotmu ({myrobot.nama}) menyerang sebanyak {damage} DMG")
    else:
      print(f"Robot lawan ({myenemy.nama}) menyerang sebanyak {damage} DMG")
    

class Antares(Robot):
  def __init__(self, nama="Antares", health=50000, damage=5000):
    super().__init__(nama, health, damage)

class Alphasetia(Robot):
  def __init__(self, nama="Alphasetia", health=40000, damage=6000):
    super().__init__(nama, health, damage)

class Lecalicus(Robot):
  def __init__(self, nama="Lecalicus", health=45000, damage=5500):
    super().__init__(nama, health, damage)

print("Selamat datang di pertandingan robot Yamako")

robot=int(input("Pilih robotmu (1 = Antares, 2 = Alphasetia, 3 = Lecalicus) :"))
if robot == 1:
  myrobot=Antares()
elif robot == 2:
  myrobot=Alphasetia()
elif robot == 3:
  myrobot=Lecalicus()
else:
  print("Robot tidak terdeteksi")
  
enemy=int(input("Pilih robot lawan (1 = Antares, 2 = Alphasetia, 3 = Lecalicus) :"))
if enemy == 1:
  myenemy=Antares()
elif enemy == 2:
  myenemy=Alphasetia()
elif enemy == 3:
  myenemy=Lecalicus()
else:
  print("Robot tidak terdeteksi")

print("Selanjutnya, pilih 1 untuk batu, 2 untuk kertas, dan 3 untuk gunting")
print()
while myrobot.health>=0 and myenemy.health>=0:
  Robot.jumlah_turn+=1
  print("Turn saat ini :",Robot.jumlah_turn)
  print(f"Robotmu ({myrobot.nama} - {myrobot.health}), robot lawan ({myenemy.nama} - {myenemy.health})")
  robothand=int(input(f"Pilih tangan robotmu ({myrobot.nama}) :"))
  enemyhand=random.randint(1,3)
  print(f"Pilih tangan robot lawan ({myenemy.nama}) : {enemyhand}")
  if robothand<4:
    if robothand == enemyhand:
      print("Seri!!")
    elif (robothand == 1 and enemyhand == 3) or (robothand == 2 and enemyhand == 1) or (robothand == 3 and enemyhand == 2):
      myrobot.lakukan_aksi(myenemy)
    else:
      myenemy.lakukan_aksi(myrobot)
  else:
    print("Terjadi Kesalahan")
    Robot.jumlah_turn-=1
  print()
