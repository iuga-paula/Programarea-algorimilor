




def afisare(M):
    for l in M:
        print(*l, sep="\t")

def valid(lista,k):
    for tara in range(k):
        if a[tara][k] and x[k] == x[tara]:
            return 0
    return 1

def bkt(k): #se pot utiliza maxim 4 culori
    global n,x,nr #pt afis cate 3 pe linie
    for i in range(1,5):
        x[k] = i
        if valid(x[:k],k): #if sol_part

            if k == n-1:#if sot_finala
                if nr !=3:
                    print(x[:k+1], sep='')
                else:
                    print()
                    nr = 0
            else:
                bkt(k+1)



f = open("harti.in")
s = f.readline()
s = s.strip()
n = int(s) #nr de tari = nr de linii mat
a = [[0 for x in range(n)] for y in range(n)]
s = f.readline()
while s != "":
    s = s.strip()
    s = s.split()
    x = int(s[0])
    y = int(s[1])
    a[x][y] = a[y][x] = 1
    s = f.readline()
f.close()

afisare(a)
x = [0]*n  #vect pt sol in care avem fiecare tara cu ce e col
bkt(0)
nr = 0