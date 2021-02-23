f=open("date3.in")
linie=f.readline()

l=[int(x) for x in linie.split()]
n=l[0]
m=l[1]
a=[]

#Smax[i][j] - suma maxima care se termina in a[i][j]
for i in f:
    p=[int(x) for x in i.split()]
    a.append(p)
print(*a,sep="\n")
Smax=[[0]*m for i in range(n) ]
Smax[0][0]=a[0][0]
for i in range(1,m):
    Smax[0][i]=sum(a[0][:i+1])
for i in range(1,n):
    Smax[i][0]=Smax[i-1][0]+a[i][0]
print("\n")
print(*Smax,sep="\n")
for i in range(1,n):
    for j in range(1,m):
        Smax[i][j]=a[i][j]+max(Smax[i-1][j],Smax[i][j-1])
print("\n")
print(*Smax,sep="\n")

ma=Smax[n-1][m-1]
i=n-1
j=m-1
sol=[a[i][j]]
while i!=0 and j!=0:
    if Smax[i][j-1]>Smax[i-1][j]:
        sol.append(a[i][j-1])
        j=j-1
    else:
        sol.append(a[i-1][j])
        i=i-1
while i!=0:
    sol.append(a[i-1][j])
    i=i-1
while j!=0:
    sol.append(a[i][j-1])
    j=j-1
print("\n")
print(sol[::-1])
