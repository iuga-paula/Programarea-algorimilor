f = open("date.in")
g = open("date.out", "w")
line = f.readline()
import random

def parola(size=6, chars = "abcdefghijklmnopqrstuvxywz",  digits = "0123456789"):
     a = ''.join(random.choice(chars) for _ in range(3))
     b = ''.join(random.choice(digits) for _ in range(4))
     yield a + b
#parola o lit mare, 3 lit mici si 4 cif

pj = parola() #incarcare generator
p = next(pj) #prima generare

while line != "":
    l = line.split()
    nume = l[0]
    prenume = l[1]
    nume = nume.lower()
    prenume = prenume.lower()
    # prenume.nume@myfmi.unibuc.ro
    g.write(prenume + "." + nume + "nume@myfmi.unibuc.ro,")
    x = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    g.write(x)
    g.write(p)
    try:
        p = next(pj)
    except StopIteration:
        pass
    g.write("\n")
    line = f.readline()

f.close()
g.close()
