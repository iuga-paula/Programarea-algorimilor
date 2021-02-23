def negative_pozitive(l):
    poz = []
    neg = []
    for x in  l:
        if x > 0:
            poz.append(x)
        else:
            neg.append(x)
    return poz, neg

s = input("dati lista de nr intregi= ")
nume = input("dati numele fisierului= ")

l = [int(x) for x in s.split()]
g = open(nume, "w")
p, n = negative_pozitive(l)
g.write(str(p) + '\n')
g.write(str(n))


