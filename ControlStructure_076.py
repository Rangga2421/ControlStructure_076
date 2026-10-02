#1.Evaluasi Performa Mahasiswa
persentase = float(input("Masukkan persentase mahasiswa: "))

if persentase >= 90:
    print("Performa sangat baik")
elif persentase >= 80:
    print("Performa sangat bagus")
elif persentase >= 70:
    print("Performa bagus")
elif persentase >= 60:
    print("Performa cukup")
else:
    print("Performa kurang")

#2.Mencari Bilangan Terbesar Dari 3 Angka
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))
angka3 = float(input("Masukkan angka ketiga: "))

if angka1 >= angka2 and angka1 >= angka3:
    terbesar = angka1
elif angka2 >= angka1 and angka2 >= angka3:
    terbesar = angka2
else:
    terbesar = angka3

print("Bilangan terbesar adalah:", terbesar)

#3.Deret Fibonaci
n = int(input("Masukkan jumlah angka Fibonacci: "))

a = 0
b = 1

print("Deret Fibonacci:")

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c