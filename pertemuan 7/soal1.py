kendaraan = input ('''Nama kendaraan? (mobil motor) jawaban =''')
bensin = input ('''Jenis Bensin? (pertalite/pertamax/turbo) jawabanmu=''')

if bensin.lower() == "pertalite" :
    hargabensin = 10000
    jarakbensin = 12
elif bensin.lower() == "peramax" :
    hargabensin = 14000
    jarakbensin = 13
elif bensin.lower() == "turbo" :
    hargabensin = 17000
    jarakbensin = 13.5
else:
    print('data bensin tidak ada')
    exit()

kota = input('''kota tujuan? (jakarta/bekasi/depok/tanggerang/bogor) jawabanmu:''')

if kota.lower() ==  "jakarta" :
    jarakkota = 20
elif kota.lower() == "bekasi" :
    jarakkota = 35.7
elif kota.lower() == "depok" :
    jarakkota = 5
elif kota.lower() == "tanggerang" :
    jarakkota = 99
elif kota.lower() == "bogor" :
    jarakkota = 120.6
else:
    print('data bensin tidak ada')
    print('data bensin tidak ada')
    exit()

pemakaianbensin = jarakkota/jarakbensin
pemakaianperliter = pemakaianbensin * hargabensin
print("nama kendaraan anda",kendaraan.upper())
print("jenis bensin anda", bensin.upper())
print("kota yng dituju",kota.upper())
print("pemakaianbensin?","{:.2f}".format(pemakaianbensin), "liter")
print("total harga dari bensin yang dikeluarkan? Rp.", int(pemakaianbensin))

