import math

# Tabung
r = float(input("Jari-jari tabung:"))
t = float(input("Tinggi tabung: "))
volume_tabung = math.pi * r * r * t
print("Volume tabung:", volume_tabung)

# Balok
p = float(input("Panjang balok: "))
l = float(input("Lebar balok: "))
volume_balok = p * l * t
print("Volume balok:", volume_balok)