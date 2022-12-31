# Membuat modul untuk menghitung luas bangun ruang
def luas_balok(panjang, lebar, tinggi):
  luas = 2 * (panjang * lebar + lebar * tinggi + panjang * tinggi)
  return luas

def luas_kubus(sisi):
  luas = 6 * sisi**2
  return luas

def luas_tabung(jari_jari, tinggi):
  luas = 2 * 3.14 * jari_jari * tinggi + 2 * 3.14 * jari_jari**2
  return luas

def luas_kerucut(jari_jari, tinggi):
  luas = 3.14 * jari_jari * (jari_jari + (jari_jari*2 + tinggi*2)*0.5)
  return luas

def luas_bola(jari_jari):
  luas = 4 * 3.14 * jari_jari**2
  return luas 