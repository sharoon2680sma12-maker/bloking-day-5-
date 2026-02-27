# Proram Menghitung Gaji Bersih

# Input data
nama = input("Masukkan nama karyawan:")
gaji_pokok = float(input("Masukan gaji pokok: "))

# Proses perhitungan 
tunjangan = 0.20 * gaji_pokok
pajak = 0.15 + (gaji_pokok + tunjangan)
gaji_bersih = gaji_pokok + tunjangan - pajak

# Output hail
print("\n=== HASIL PERHITUNGAN GAJI===")
print("Nama Karyawan :", nama)
print("Gaji Pokok     :", gaji_pokok)
print ("Gaji Bersih   :", gaji_bersih)