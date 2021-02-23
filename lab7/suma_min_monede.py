

def afisare(suma):
    global nrmin,pred
    print(nrmin[suma]," monede folosite")
    poz=suma
    while pred[poz]!=-1:
        print(pred[poz],end=" ")
        poz=poz-pred[poz]


f=open("date.in")
s=int(f.readline())
linie=f.readline()
monede=[int(x) for x in linie.split()]
nrmin=[float('inf')]*(s+1)
pred=[-1]*(s+1)

nrmin[0]=0
pred[0]=-1

for i in range(1,s+1):
    for m in monede:
        if m<=i and 1+nrmin[i-m] < nrmin[i]:
            nrmin[i]=1+nrmin[i-m]
            pred[i]=m

print(nrmin)
print(pred)
afisare(s)

