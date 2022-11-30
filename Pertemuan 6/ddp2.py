#menghitung nilai

#input
nama = input("masukan nama anda =")
kelas = input ("masukan kelas anda =")
nilai = int(input("masukan nilai (max = 100)="))

#output
print("nama anda =",nama)
print("kelas anda =",kelas)
print("nilai anda =",nilai)
if(nilai > 89 and nilai <101 ):
    print("istimewa")
elif(nilai > 69 and nilai <90):
    print("sangat bagus")
elif(nilai >59 and nilai < 70):
    print("cukup")
else:
    print("gagal")