def afisare_timp(*tis):
    timp_asteptare = 0
    timp_mediu = 0
    for x in tis:
        timp_asteptare += x[1]
        timp_mediu += timp_asteptare
        print("{}\t{}\t{}".format(*x, timp_asteptare))
    timp_mediu /= len(tis) #timpul mediu de așteptare
    print(timp_mediu)


f = open("tis.txt")
s = f.readline()
f.close()
l = [int(x) for x in s.split()] #timpii de asteptare
n = len(l)
timp = [((x,l[x-1])) for x in range(1,n+1,1)] #lista de tupluri cu nr de ordine + timpul de asteptare
print(timp)

afisare_timp(*timp) # timp de asteptare initial inițial
timp2 = sorted(timp, key = lambda x: x[1])
afisare_timp(*timp2) # timp de asteptare dupa ce s-a modificat lista



