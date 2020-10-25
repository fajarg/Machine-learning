#Program main catur

c = []
b = []
h = 0
def convert(list): 
    return tuple(i for i in list)


a = int(input("Masukkan ukuran catur : \n"))


print("Masukkan papan catur : ")
for i in range (a) :
    b = str(input()).split()
    x = len(b)
    c.append(b)
    
    for j in range (x) :
        if x > a :
            print ("Input terlalu banyak, matrik : ",a ,"x", a)
            exit()
        if b[j] == "H" :
            h = h + 1
            #print(h)
            if h > 1 :
                print("kuda tidak boleh lebih dari 1 ")
                exit()


convert(c)
makan = 0

for i in range(a) :
    for j in range(a) :
        if c[i][j] == "H" and a == 1:
             makan = makan + 0
             break
        if c[i][j] == "H" and a == 2:
             makan = makan + 0
             break
        if c[i][j] == "H" and a == 3:
            if c[0][0] == "H" :
                if c[0+1][0+2] == "P" :
                    makan = makan +1
                if c[0+2][0+1] == "P" :
                    makan = makan +1
            if c[0][1] == "H" :
                if c[0+2][1+1] == "P" :
                    makan = makan +1
                if c[0+2][1-1] == "P" :
                    makan = makan +1
            if c[0][2] == "H" :
                if c[0+2][2-1] == "P" :
                    makan = makan +1
                if c[0+1][2-2] == "P" :
                    makan = makan +1
            if c[1][0] == "H" :
                if c[1-1][0+2] == "P" :
                    makan = makan +1
                if c[1+1][0+2] == "P" :
                    makan = makan +1
            if c[1][1] == "H" :
                makan = makan + 0
            if c[1][2] == "H" :
                if c[1-1][2-2] == "P" :
                    makan = makan +1
                if c[1+1][2-2] == "P" :
                    makan = makan +1
            if c[2][0] == "H" :
                if c[2-2][0+1] == "P" :
                    makan = makan +1
                if c[2-1][0+2] == "P" :
                    makan = makan +1
            if c[2][1] == "H" :
                 if c[2-2][1-1] == "P" :
                     makan = makan +1
                 if c[2-2][1+1] == "P" :
                     makan = makan +1
            if c[2][2] == "H" :
                if c[2-2][2-1] == "P" :
                    makan = makan +1
                if c[2-1][2-2] == "P" :
                    makan = makan +1
            break
        if c[i][j] == "H" and a == 4:
            if c[0][0] == "H" :
                if c[0+1][0+2] == "P" :
                    makan = makan +1
                if c[0+2][0+1] == "P" :
                    makan = makan +1
            if c[0][1] == "H" :
                if c[0+1][1+2] == "P" :
                    makan = makan +1
                if c[0+2][1+1] == "P" :
                    makan = makan +1
                if c[0+2][1-1] == "P" :
                    makan = makan +1 
            if c[0][2] == "H" :
                if c[0+1][2-2] == "P" :
                    makan = makan +1
                if c[0+2][2-1] == "P" :
                    makan = makan +1
                if c[0+2][2+1] == "P" :
                    makan = makan +1
            if c[0][3] == "H" :
                if c[0+1][3-2] == "P" :
                    makan = makan +1
                if c[0+2][3-1] == "P" :
                    makan = makan +1
            if c[1][0] == "H" :
                if c[1-1][0+2] == "P" :
                    makan = makan +1
                if c[1+1][0+2] == "P" :
                    makan = makan +1
                if c[1+2][0+1] == "P" :
                    makan = makan +1
            if c[1][1] == "H" :
                if c[1+2][1-1] == "P" :
                    makan = makan +1
                if c[1+2][1+1] == "P" :
                    makan = makan +1
                if c[1+1][1+2] == "P" :
                    makan = makan +1
                if c[1-1][1+2] == "P" :
                    makan = makan +1
            if c[1][2] == "H" :
                if c[1-1][2-2] == "P" :
                    makan = makan +1
                if c[1+1][2-2] == "P" :
                    makan = makan +1
                if c[1+2][2-1] == "P" :
                    makan = makan +1
                if c[1+2][2+1] == "P" :
                    makan = makan +1
            if c[1][3] == "H" :
                if c[1-1][3-2] == "P" :
                    makan = makan +1
                if c[1+1][3-2] == "P" :
                    makan = makan +1
                if c[1+2][3-1] == "P" :
                    makan = makan +1
            if c[2][0] == "H" :
                if c[2-2][0+1] == "P" :
                    makan = makan +1
                if c[2-1][0+2] == "P" :
                    makan = makan +1
                if c[2+1][0+2] == "P" :
                    makan = makan +1
            if c[2][1] == "H" :
                if c[2-2][1+1] == "P" :
                    makan = makan +1
                if c[2-2][1-1] == "P" :
                    makan = makan +1
                if c[2-1][1+2] == "P" :
                    makan = makan +1
                if c[2+1][1+2] == "P" :
                    makan = makan +1
            if c[2][2] == "H" :
                if c[2-2][2+1] == "P" :
                    makan = makan +1
                if c[2-2][2-1] == "P" :
                    makan = makan +1
                if c[2-1][2-2] == "P" :
                    makan = makan +1
                if c[2+1][2-2] == "P" :
                    makan = makan +1
            if c[2][3] == "H" :
                if c[2-2][3-1] == "P" :
                    makan = makan +1
                if c[2-1][3-2] == "P" :
                    makan = makan +1
                if c[2+1][3-2] == "P" :
                    makan = makan +1
            if c[3][0] == "H" :
                if c[3-2][0+1] == "P" :
                    makan = makan +1
                if c[3-1][0+2] == "P" :
                    makan = makan +1
            if c[3][1] == "H" :
                if c[3-2][1-1] == "P" :
                    makan = makan +1
                if c[3-2][1+1] == "P" :
                    makan = makan +1
                if c[3-1][1+2] == "P" :
                    makan = makan +1
            if c[3][2] == "H" :
                if c[3-1][2-2] == "P" :
                    makan = makan +1
                if c[3-2][2-1] == "P" :
                    makan = makan +1
                if c[3-2][2+1] == "P" :
                    makan = makan +1
            if c[3][3] == "H" :
                if c[3-2][3-1] == "P" :
                    makan = makan +1
                if c[3-1][3-2] == "P" :
                    makan = makan +1
            break
        if c[i][j] == "H" and a == 5  :
            if c[0][0] == "H" :
                if c[0+1][0+2] == "P" :
                    makan = makan +1
                if c[0+2][0+1] == "P" :
                    makan = makan +1
            if c[0][1] == "H" :
                if c[0+2][1-1] == "P" :
                    makan = makan +1
                if c[0+2][1+1] == "P" :
                    makan = makan +1
                if c[0+1][1+2] == "P" :
                    makan = makan +1
            if c[0][2] == "H" :
                if c[0+1][2-2] == "P" :
                    makan = makan +1
                if c[0+2][2-1] == "P" :
                    makan = makan +1
                if c[0+2][2+1] == "P" :
                    makan = makan +1
                if c[0+1][2+2] == "P" :
                    makan = makan +1
            
            if c[0][3] == "H" :
                if c[0+1][3-2] == "P" :
                    makan = makan +1
                if c[0+2][3-1] == "P" :
                    makan = makan +1
                if c[0+2][3+1] == "P" :
                    makan = makan +1
            if c[0][4] == "H" :
                if c[0+1][4-2] == "P" :
                    makan = makan +1
                if c[0+2][4-1] == "P" :
                    makan = makan +1
            if c[1][0] == "H" :
                if c[1-1][0+2] == "P" :
                    makan = makan +1
                if c[1+1][0+2] == "P" :
                    makan = makan +1
                if c[1+2][0+1] == "P" :
                    makan = makan +1
            if c[1][1] == "H" :
                if c[1+2][1-1] == "P" :
                    makan = makan +1
                if c[1+2][1+1] == "P" :
                    makan = makan +1
                if c[1+1][1+2] == "P" :
                    makan = makan +1
                if c[1-1][1+2] == "P" :
                    makan = makan +1
            if c[1][2] == "H" :
                if c[1-1][2-2] == "P" :
                    makan = makan +1
                if c[1+1][2-2] == "P" :
                    makan = makan +1
                if c[1+2][2-1] == "P" :
                    makan = makan +1
                if c[1+2][2+1] == "P" :
                    makan = makan +1
                if c[1+1][2+2] == "P" :
                    makan = makan +1
                if c[1-1][2+2] == "P" :
                    makan = makan +1
            if c[1][3] == "H" :
                if c[1-1][3-2] == "P" :
                    makan = makan +1
                if c[1+1][3-2] == "P" :
                    makan = makan +1
                if c[1+2][3-1] == "P" :
                    makan = makan +1
                if c[1+2][3+1] == "P" :
                    makan = makan +1
            if c[1][4] == "H" :
                if c[1-1][4-2] == "P" :
                    makan = makan +1
                if c[1+1][4-2] == "P" :
                    makan = makan +1
                if c[1+2][4-1] == "P" :
                    makan = makan +1
            if c[2][0] == "H" :
                if c[2-2][0+1] == "P" :
                    makan = makan +1
                if c[2-1][0+2] == "P" :
                    makan = makan +1
                if c[2+1][0+2] == "P" :
                    makan = makan +1
                if c[2+2][0+1] == "P" :
                    makan = makan +1
            if c[2][1] == "H" :
                if c[2-2][1-1] == "P" :
                    makan = makan +1
                if c[2-2][1+1] == "P" :
                    makan = makan +1
                if c[2+2][1-1] == "P" :
                    makan = makan +1
                if c[2+2][1+1] == "P" :
                    makan = makan +1
                if c[2+1][1+2] == "P" :
                    makan = makan +1
                if c[2-1][1+2] == "P" :
                    makan = makan +1
            if c[2][2] == "H" :
                if c[2-1][2-2] == "P" :
                    makan = makan +1
                if c[2-2][2-1] == "P" :
                    makan = makan +1
                if c[2-1][2+2] == "P" :
                    makan = makan +1
                if c[2-2][2+1] == "P" :
                    makan = makan +1
                if c[2+1][2-2] == "P" :
                    makan = makan +1
                if c[2+2][2-1] == "P" :
                    makan = makan +1
                if c[2+2][2+1] == "P" :
                    makan = makan +1
                if c[2+1][2+2] == "P" :
                    makan = makan +1
            if c[2][3] == "H" :
                if c[2-2][3-1] == "P" :
                    makan = makan +1
                if c[2-1][3-2] == "P" :
                    makan = makan +1
                if c[2+1][3-2] == "P" :
                    makan = makan +1
                if c[2+2][3-1] == "P" :
                    makan = makan +1
            if c[2][4] == "H" :
                if c[2-2][4-1] == "P" :
                    makan = makan +1
                if c[2-1][4-2] == "P" :
                    makan = makan +1
                if c[2+1][4-2] == "P" :
                    makan = makan +1
                if c[2+2][4-1] == "P" :
                    makan = makan +1
            if c[3][0] == "H" :
                if c[3-2][0+1] == "P" :
                    makan = makan +1
                if c[3-1][0+2] == "P" :
                    makan = makan +1
                if c[3+1][0+2] == "P" :
                    makan = makan +1
            if c[3][1] == "H" :
                if c[3-2][1-1] == "P" :
                    makan = makan +1
                if c[3-2][1+1] == "P" :
                    makan = makan +1
                if c[3-1][1+2] == "P" :
                    makan = makan +1
                if c[3+1][1+2] == "P" :
                    makan = makan +1
            if c[3][2] == "H" :
                if c[3-1][2+2] == "P" :
                    makan = makan +1
                if c[3-2][2+1] == "P" :
                    makan = makan +1
                if c[3-2][2-1] == "P" :
                    makan = makan +1
                if c[3-1][2-2] == "P" :
                    makan = makan +1
                if c[3+1][2-2] == "P" :
                    makan = makan +1
                if c[3+2][2+2] == "P" :
                    makan = makan +1
            if c[3][3] == "H" :
                if c[3-2][3+1] == "P" :
                    makan = makan +1
                if c[3-2][3-1] == "P" :
                    makan = makan +1
                if c[3-1][3-2] == "P" :
                    makan = makan +1
                if c[3+1][3-2] == "P" :
                    makan = makan +1
            if c[3][4] == "H" :
                if c[3-2][4-1] == "P" :
                    makan = makan +1
                if c[3-1][4-2] == "P" :
                    makan = makan +1
                if c[3+1][4-2] == "P" :
                    makan = makan +1
            if c[4][0] == "H" :
                if c[4-2][0+1] == "P" :
                    makan = makan +1
                if c[4-1][0+2] == "P" :
                    makan = makan +1
            if c[4][1] == "H" :
                if c[4-2][1-1] == "P" :
                    makan = makan +1
                if c[4-2][1+1] == "P" :
                    makan = makan +1
                if c[4-1][1+2] == "P" :
                    makan = makan +1
            if c[4][2] == "H" :
                if c[4-1][2-2] == "P" :
                    makan = makan +1
                if c[4-2][2-1] == "P" :
                    makan = makan +1
                if c[4-2][2+1] == "P" :
                    makan = makan +1
                if c[4-2][2+2] == "P" :
                    makan = makan +1
            if c[4][3] == "H" :
                if c[4-2][3+1] == "P" :
                    makan = makan +1
                if c[4-2][3-1] == "P" :
                    makan = makan +1
                if c[4-1][3-2] == "P" :
                    makan = makan +1
            if c[4][4] == "H" :
                if c[4-2][4-1] == "P" :
                    makan = makan +1
                if c[4-1][4-2] == "P" :
                    makan = makan +1
            break  
        if c[i][j] == "H" :
            if c[i-1][j-2] == "P" :
                makan = makan + 1
           
            if c[i-1][j+2] == "P" :
                makan = makan + 1
                
            if c[i-2][j-1] == "P" :
                makan = makan + 1
                
            if c[i-2][j+1] == "P":
               makan = makan + 1
            if c[i+1][j-2] == "P":
                makan = makan + 1
            if c[i+1][j+2] == "P":
                makan = makan + 1
            if c[i+2][j-1] == "P":
                makan = makan + 1
                
            if c[i+2][j+1] == "P":
                makan = makan + 1
print("Banyaknya bidak catur yang dapat dimakan kuda : ")
print(makan)


