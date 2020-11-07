# input 3 buah bilangan , menggunakan statement if
print("menentukan bilangan terbesar dari 3 bilangan")

print("Masukkan Bilangan ke-1 : ")
bilangan1=int(input())
print("Masukkan Bilangan ke-2 : ")
bilangan2=int(input())
print("Masukkan Bilangan ke-3 : ")
bilangan3=int(input())


print('\n')


if ( bilangan1 > bilangan2 ) and ( bilangan1 > bilangan3 ) :
    print("Bilangan 1 lebih Besar dari Bilangan 2 dab 3")
elif ( bilangan2 > bilangan1) and ( bilangan2 > bilangan3 ) :
    print ("Bilangan 2 lebih Besar dari Bilangan 1 dan 3")
elif (bilangan3 > bilangan1) and (bilangan3 > bilangan2 ) :
    print ("Bilangan 3 lebih besar dari Bilangan 1 dan 2")
else :
    print ("Semua Bilangan sama Besarnya")