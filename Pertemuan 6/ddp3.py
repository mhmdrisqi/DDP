#praktikum

#input
kondisi = input("masukan kondisi lab (tersedian/penuh/tidak ada)=")

#output dan ketentuan
if(kondisi == "tersedia"):
    print("maka praktikum")
elif(kondisi == "penuh"):
    print("maka pindah jadwal")
elif(kondisi == "tidak ada"):
    print("maka tidak jadi praktikum")
else:
    print("error")