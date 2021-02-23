from math import sqrt
#rezolvare a):
def ipotenuza(a,b):
    return sqrt(a*a + b*b)
#rezlovare b):
f = open("triplete_pitagoreice.txt","w")
b = int(input("dati cateta b= "))
for a in range(1,b-1,1): # a<b
    c = ipotenuza(a,b)
    if c == int(c):
        f.write("(" + str(b)+ "," + str(a) +"," + str(int(c)) + ")")

f.close()


