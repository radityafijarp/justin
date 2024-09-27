number1=input("Masukan nomor ke-1: ")
number2=input("Masukan nomor ke-2: ")
print("Nomor ke-1: ",number1,". Nomor ke-2:",number2)
number3=number1 #buat variabel dummy yang nilainya sama dengan number 1 lama
number1=number2 #ubah nilai variable number1 jadi number 2 lama
number2=number3 #ubah nilai variable number2 jadi number 1 lama
print("Setelah ditukar: \nNomor ke-1: ",number1,". Nomor ke-2:",number2)