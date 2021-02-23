n = 0
l = []

def citire():
    global n
    n = int(input("dati nr de elem al listei= "))
    s = input("dati lista= ")
    global l
    l = [int(x) for x in s.split()]


citire()
#print(n,l)

def poz(x,i,j,lista,nrelem):
    for number in range(i, j+1):
        if lista[number] > x:
            return number
    return -1

#print(poz(2,0,n,l,n))
for x in range(1,n-1,1):
    p = poz(l[x], 0, n-1, l, n)
    if p > x:
        print("Nu")
        break;
else:
    print("Da")