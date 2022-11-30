print("Program menghitung luas dan keliling layang-layang")

d1 = int(input("Masukan Diagonal 1 ="))
d2 = int(input("Masukan Diagonal 2 ="))
n1 = int(input("Masukan Sisi 1     ="))
n2 = int(input("Masukan Sisi 2     ="))

luas = 1/2* (d1*d2)
kel = 2* (n1+n2)

print("Luas layang-layang adalah       = ", luas )
print("Keliling layang-layang adalah   = ", kel  )