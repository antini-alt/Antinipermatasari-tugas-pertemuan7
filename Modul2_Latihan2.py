# Membuat program_menentukan nilai Akhir

Nama = input("Masukan Nama : ")
Uts = input("Masukan Nilai UTS : ")
UAS = input("Masukan Nilai UAS : ")
Tugas = input("Masukan Nilai Tugas : ")

Akhir =(int(Tugas) * .2 + (int(Uts) * .4) + (int(UAS) * .4)
keterangan = ("TIDAK LULUS", "LULUS")[Akhir > 60.0]
if Akhir > 80:
    huruf = "A"
elif Akhir >70:
    huruf = "B"
elif Akhir > 50:
    huruf = "C"
elif Akhir > 40:
    huruf = "D"
else :
    huruf = "E"

print("\nNama : ", Nama)
print("Nilai Uts : ", uts)
print("Nilai UAS : ", UAS)
print("Nilai Tugas : ", Tugas)
print("Nilai Akhir : ", Akhir)
print("\nNilai Huruf : ", huruf)
print("Keterangan : ", keterangan)