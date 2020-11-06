print("Masukkan Pilihan Angka ke-1")
bilangan1 = int(input())
print("Masukkan Pilihan Angka ke-2")
bilangan2 = int(input())
print("Masukkan Pilihan Angka ke-3")
bilangan3 = int(input())

print("\n")


if (bilangan1 > bilangan2) and (bilangan1 > bilangan3):
    print(f"angka pertama lebih besar dari angka ketiga")
elif (bilangan2 > bilangan1) and (bilangan2 > bilangan3):
    print(f"angka dua lebih besar dari angka tiga")
elif (bilangan3 > bilangan2) and (bilangan3 > bilangan1)
    print(f"angka tiga lebih besar dari angka satu")
else:
    print("angka yang dimasukkan sama besar")