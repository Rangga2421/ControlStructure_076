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