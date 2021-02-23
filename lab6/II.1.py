def suma(lista):
    s = 0
    for elem in lista:
        s += elem
    return s

def afisare(lista):
    ok = False
    for elem in lista:
        if ok == True:
            print("+", end=" ")
        else:
            ok = True
        print(elem, end=" ")
    print()

def bkt(k):
    global x, nr
    for v in range(1, nr-k+2):
        x[k] = v
        sum = suma(x[:k+1])
        #print(sum)
        if sum <= nr:
            if sum == nr:
                afisare(x[:k+1])
            else:
                bkt(k+1)

#descompunere
f = open("descompunere.in")
s = f.read()
s.strip() #sterge spatiile inutile inaintea+in urma numarului citit
nr = int(s)
print(nr)
x = [0]*100
#print(suma(x[:2]))
f.close()
bkt(0)
