from luas.segitiga import luas as ls
from luas.persegi import luas as lp
from luas.lingkaran import luas as ll
from volume.kubus import volume as vk
from volume.prisma import volume as vp
from volume.bola import volume as vb


# luas segitiga
print("\n--> Menghitung Luas Segitiga :")
print("Alas =  \t", (20))
print("Tinggi =  \t", (5))
print("Luas Segitiga =\t", ls(20,5))

#Luas Persegi
print("\n--> Menghitung Luas Persegi :")
print("Sisi =  \t", (3))
print("Luas Persegi = \t", lp(3))

#Luas LIngkaran 
print("\n--> Menghitung Luas Lingkaran :")
print("Radius =  \t", (7))
print("Luas Lingkaran =\t", ll(7))


#Volume Kubus
print("\n--> Menghitung Volume Kubus:")
print("Sisi =  \t", (21))
print("Volume Kubus = \t",vk(21))

#Volume Prisma
print("\n--> Menghitung Volume Prisma:")
print("als =  \t", (3))
print("ts =  \t", (7))
print("tp =  \t", (11))
print("Volume Prisma =\t",vp(3,7,11))

#Volume Bola
print("\n--> Menghitung Volume Bola:")
print("Radius =  \t", (27))
print("Volume Bola = \t",vb(27))




