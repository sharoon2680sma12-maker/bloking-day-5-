# Persegi
s = float(input("Masukkan sisi persegi: "))
luas = s * s
keliling = 4 * s
print("Luas:", luas)
print("keliling:", keliling)

# Persegi panjang
p = float(input("Masukkan panjang:"))
l = float(input("Masukkan lebar: "))
luas = p * l
keliling = 2 * (p + l)
print("Luas:", luas)
print("Keliling:", keliling)

# Trapesium
a = float(input("Sisi sejajar a: "))
b = float(input("Sisi sejajar b: "))
t = float(input("Tinggi: "))
c = float(input("Sisi miring c: "))
d = float(input("Sisi miring d: "))

luas = 0.5 * (a + b) * t
keliling = a + b + c + d
print("Luas:", luas)
print("Keliling:", keliling)