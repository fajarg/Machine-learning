print ("kalkulator")

print ("1. jumlah")
print ("2. kurang")
print ("3. kali")
print ("4. bagi")

#input
a = input()

angka1 = int(input("masukan bil pertama : "))
angka2 = int (input("masukan bil kedua : "))

if a == '1' :
    print(angka1+angka2)

elif a == '2' :
    print(angka1-angka2)

elif a == '3' :
    print(angka1*angka2)


else :
    print("Input salah")
