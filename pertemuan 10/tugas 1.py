
data_diri = {
    'nama':'Reza', 
    'nilai':[70, 65, 50, 85]
    }
hasil_akhir = [
{'nama':'Reza', 'nilai':70},
{'nama':'Ciut', 'nilai':63},
{'nama':'Dian', 'nilai':80},
{'nama':'Badu', 'nilai':40}
]

def lulus_nilai(input):
    siswa_lulus = [i for i in input if i['nilai'] > 65]

    return siswa_lulus

siswa_lulus = lulus_nilai(hasil_akhir)

for siswa in siswa_lulus:
    print(f" {siswa['nama']}")

