54# fungsi penjumlahan
def tambah(x, y):
   return x + y

# fungsi pengurangan
def kurang(x, y):
   return x - y

# fungsi perkalian
def kali(x, y):
   return x * y

# fungsi pembagian
def bagi(x, y):
   return x / y

# menu operasi
print("Pilih Operasi: ")
print("1.Penjumlahan")
print("2.Pengurangan")
print("3.Perkalian")
print("4.Pembagian")

# Meminta input dari user
pilihan = input("Masukkan pilihan|1|2|3|4|: ")

bilangan1 = int(input("Masukkan bilangan pertama: "))
bilangan2 = int(input("Masukkan bilangan kedua: "))

if pilihan == '1':
   print(bilangan1,"+",bilangan2,"=", tambah(bilangan1,bilangan2))
elif pilihan == '2':
   print(bilangan1,"-",bilangan2,"=", kurang(bilangan1,bilangan2))
elif pilihan == '3':
   print(bilangan1,"*",bilangan2,"=", kali(bilangan1,bilangan2))
elif pilihan == '4':
   print(bilangan1,"/",bilangan2,"=", bagi(bilangan1,bilangan2))
else:
   print("Input yang dimasukkan salah")
