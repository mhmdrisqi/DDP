nM=input("Masukan Nama: ")
hp=input("Masukan No HP: ")
menu=str(input("Mau pesan apa? (makanan/minuman): "))
menu=str(input("Mau pesan apa? (makanan/minuman): "))
if menu == "makanan":
    print("""
=============================
List Menu makanan
=============================
A. Nasi goreng : Rp. 15.000
B. Mie Goreng : Rp. !2.000
C. Ayam geprek : Rp. 18.000
""")

elif menu == "minuman":
    print("""
=============================
List Menu Minuman Kopi
=============================
D. Aneka Jus: Rp. 11.000
E. Soft Drink: Rp. 12>000
F. Sweet Ice Tea: Rp> 11.000
=============================
""")
pesan=input(" Mau pesan apa? (masukan list abjad sesuai menu): ")
Jp=int(input("Masukan jumlah Pesanan: "))
if pesan == "A":
    listmenu="Nasui Goreng"
    Th=(15000*Jp)
elif pesan == "B":
    listmenu="Mie goreng"
    Th=(12000*Jp)
elif pesan == "C":
    listmenu= "Ayam Geprek"
    Th=(18000*Jp)
elif pesan == "D":
    listmenu= "Aneka Jus"
    Th=(11000*Jp)
elif pesan == "E":
    listmenu= "Soft Drink"
    Th=(12000*Jp)
elif pesan == "F":
    listmenu= "Sweet Ice Tea"
    Th=(11000*Jp)

print("Nama :",nM)
print("No HP :",hp)
print("Menu :",listmenu)
print("Jumlah pesan :",Jp)
print("--------------------------")
print("Jumlah Bayar :",Th)



