#Program jalan - jalan dengan PBO

import math

def encode(masukan) :
    if masukan == "selesai":
        b = 15
    else :
        b = [math.floor(ord(c)*math.pi) for c in masukan]
        b = (sum([int(i) for i in b]))%15
    return b 
   

mn = []
mb = []
masukan = []

print ("==============Selamat datang !================")
i = 1
while  masukan != 'selesai' :
    masukan = str(input("Silahkan masukan nama barang : "))
    mb.append(masukan)
    mn.append((encode(masukan)))
    i=i+1

print ("===============================================")
n = len(mn)
i = 0
for i in range (n):
    if mn [i] == 15 :
       continue 
    if mn[i] >= 0 and mn[i] <= 4 :
       print(mb[i] , "adalah barang Lucu")
    elif mn[i] >= 5 and mn[i] <= 10 :
       print(mb[i] , "adalah barang Unik")
    elif mn[i] >= 11 and mn[i] <= 14 :
       print(mb[i] , "adalah barang Langka")
print ("Terimakasih sudah belanja di QuantaMart !")

