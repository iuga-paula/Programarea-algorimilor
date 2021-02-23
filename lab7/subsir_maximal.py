
def afisare():
    global lmax, pred
    ma=max(lmax)
    poz=lmax.index(ma)
    print(ma, " ",poz)
    rez=[v[poz]]
    while pred[poz]!=-1:
        poz = pred[poz]
        rez.append(v[poz])

    print(rez[::-1])

#lmax - lungimea maxima a unui subsir care se termina cu pozitia i
#pred
f=open("date2.in")
linie=f.readline()
v=[int(x) for x in linie.split()]
lmax=[1]*len(v)
pred=[-1]*len(v)
lmax[0]=1

for i in range(1,len(v)):
    for j in range(i):
        if v[j]<=v[i] and lmax[j]+1>lmax[i]:
            lmax[i]=lmax[j]+1
            pred[i]=j
print(v)
print(lmax)
print(pred)
afisare()


