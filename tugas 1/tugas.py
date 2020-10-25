#Program jalan - jalan dengan PBO
import math

def conver(masukan) :
    n = len(masukan)
    
    for i in range (n) :
        if masukan == "selesai" :
            continue
        b = [ord(c) for c in masukan]
    print (b)


mn = []
masukan = []

i = 1
while  masukan != 'selesai' :
    masukan = str(input("masukan kata barang : "))
    mn.append(masukan)
    i=i+1
    
print(conver(mn))
