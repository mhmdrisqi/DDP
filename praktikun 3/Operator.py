number1 = 5
number2 = 10

# Operator perbandingan 
if number1 != number2:
    print("Nomor Berbeda!")
else:
    print("Nomor sama!")

# Operator logika
if number2 > 99 and number1 < 1000:
    print("Bilangan ratusan!")
else:
    print("Bukan bilangan ratusan")

# Operatir aritmatika
while True:
    number3 = int(input("Masukan angka:"))

    if number3 == 00:
        break
    
    if number3 % 2 == 0:
        print("Bilangan genap")
    else:
        print("Bilangan ganjil")