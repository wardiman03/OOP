#nama : Wardiman
#NIM : D0221345
#Kelas : Informatika F

#Menghitung luas persegi
print("Menghitung Luas Persegi")
p = float(input("Masukkan panjang:"))
l = float(input("Masukkan Lebar:"))
persegi = p*l
print("Luas persegi adalah:" + str(persegi))

print("========================================")

#Menghitung Luas Lingkaran
print("Menghitung Luas Lingkaran")
r = int(input('Masukkan jari-jari lingkaran:'))
phi = 3.14
L = phi*(r*r)
print('Luas lingkaran dengan jari-jari{} adalah{}'.format(r,L))

print("========================================")

#Menghitung Luas Segitiga
print("Menghitung Luas Segitiga")
a = float(input("Masukkan panjang alas:"))
t = float(input("Masukkan tinggi segitiga:"))
luas = 0.5*a*t
print("Luas segitiga adalah::" + str(luas))
