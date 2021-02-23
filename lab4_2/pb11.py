#rezolvare a):
#se observa ca pt a forma nr cerut se alipeste cifra maxima din fiecare parametru O SINGURA DATA!
def nr_max(*args): #nr variabil de parametrii
    nou = 0
    cif_max = 0
    for x in args:
        n = x
        print(n)
        while n != 0:
                #print(type(x))
                r = n % 10
                cif_max = max(r, cif_max)
                n = n // 10
        nou = nou * 10 + cif_max
    return nou
s = input("lista = ")
l = [int(x) for x in s.split()]
print(nr_max(*l))

#rezolvare b):
a = int(input("dati a= "))
b = int(input("dati b= "))
c = int(input("dati c= "))

def verif(a = 1, b = 1, c = 1):
    if nr_max(a) <= 1 and nr_max(b) <= 1 and nr_max(c) <= 1:
        return True
    return False

print(verif(a,b,c))