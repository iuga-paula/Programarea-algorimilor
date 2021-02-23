f = open("angajati.txt")
s = f.readline()
l = []
lmare = []
while s != "":
    s = s.rstrip('\n') #pt a scapa de caracterul linie noua
    l = [x for x in s.split(',')]
    lmare.append(l)
    s = f.readline()
print(lmare)
f.close()
print()
#rezolvare a):
nume = input("dati numele de cautat= ")
def reza(nume):
    ok = 0
    for x in lmare:
        if nume in x:
            print(x[1:])
            ok = 1
    if not ok:
        print("nu exista numele introdus! ")

reza(nume)

#rezolvare b):
import sys
def rezb():
    minim = sys.maxsize
    for x in lmare:
        if int(x[2]) < minim:
            minim = int(x[2]) #calcul slariu minim
    print("salariul minim este: ", minim)
    for x in lmare:
        if x[2] == str(minim):
            print(x[0])

rezb()

#rezolvare c):
def rezc():
    suma = 0
    for x in lmare:
        suma += int(x[2])
    print("salariul mediu este", suma/len(lmare))

rezc()

#rezolvare d):
def rezd():
    g = open("angajati_nume.txt", "w")
    nume = list(x[0] for x in lmare)
    #print(nume)
    g.write(str(sorted(nume)))
    g.close()

rezd()

#rezolvare e): #descr dupa varsta, cr dupa nume
def reze():
    # varsta = list(int(x[1]) for x in lmare)
    # nume = list(x[0] for x in lmare)

    lmare.sort(key=lambda x: x[1], reverse=True) #descr dupa varsta
    lmare.sort(key=lambda x: x[0])    #cr dupa nume
    print(lmare)

reze()

#rezolvare f): descr dupa salariu, cresc dupa varsta
def rezf():
    lmare.sort(key=lambda x: x[2], reverse=True)
    lmare.sort(key=lambda x: x[1])
    print(lmare)
rezf()