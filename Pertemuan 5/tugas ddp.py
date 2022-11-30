bb = input ("Barat badanmu (kg) = ")
tb = input ("Tinggi badanmu (cm) = ")

bmi = int(bb) / (int(tb)/100)**2

print("nilai BMI kamu adalah ", bmi)
if (bmi < 18.5):
    status = "kekurangan berat adalah"
if (bmi < 24.9 and bmi > 18.5):
    status = "normal (ideal)"
if (bmi < 29.9 and bmi > 25):
    status = "kelebihan barat"
if (bmi > 30):\
    status = "keguman (Obisitas)"
print("dan status berat badanmu adalah ", status)