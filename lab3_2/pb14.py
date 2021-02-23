f = open("graf_in.txt")
g = open("graf_out.txt", "w")
s = f.readline()
s = s.split()
l = [0]*0
fel_graf = s[0]
s = f.readline()
s = s.split()
n = int(s[0]) #nr de noduri
s = f.readline()
s = s.split()
m = int(s[0]) #nr de muchii
s = f.readline()
i = 1
while i < m:
    s = s.split()
    x = int(s[0])
    y = int(s[1])
    l.insert((len(l)), tuple((x,y)))
    if fel_graf == "neorientat":
        l.insert(len(l), tuple((y,x)))
    i += 1
    s = f.readline()
l.sort()
print("rezolvarea de la a) este: ")
print(l)
D = {}
for x in l:
    if x[0] not in D.keys():
        D[x[0]] = []
        D[x[0]].append(x[1])
    elif x[1] not in D[x[0]]:
        D[x[0]].append(x[1])
print("rezlvarea de la b) este: ")
print(D)
#viz = [0]*n
def get_key(val):
    for key in D.keys():
        for a in D.items():
            if val in a:
                return key

    return 0

mat = []
for x in range(n):
    linie = []
    for y in range(n):
        #print(get_key(y))
        if get_key(y) == x:
            #viz[get_key(y)] = 1
            linie.append(1)
        else:
            linie.append(0)
    mat.append(linie)
if fel_graf == "neorientat": #avem atucni martice simetrica
    n = len(mat)
    for i in range(n): # ne da linia
        n1 = len(mat[i])
        for j in range(n1):
            if mat[i][j]:
                mat[j][i] = 1

print("rezolvarea de la c) este: ")
print(mat)

#parcurgere latime
print("rezolvarea de la d) este: ")
s = f.readline()
print(s)
s = s.split()
start = int(s[0])
stop = int(s[1])
start = 1
BF = [] #coada cu elem tupluri (not,tata_nod)
BF.append(tuple((start,-1)))
st = dr = 0
while st <=dr :
    tata = BF[st][0] #primul nod din coada => ultimul din lista
    try:
        for fiul in D[tata]:
            if fiul not in [nod for (nod, parinte) in BF]:
                BF.append((fiul, tata))
                dr += 1
    except:
        pass

    st += 1
    for (nod,parinte) in BF:
        print(nod,end=',')
print()
print("rezolvarea de la e) este: ")
DF = [] #stiva
vizitat = []
DF.append(start)
vizitat.append(start)
while  DF !=[]: #cat timp stiva nu este vida
    tata = DF[-1] #fiul din varful stivei
    try:
        for fiul in D[tata]:
            if fiul not in vizitat:
                DF.append(fiul)
                vizitat.append(fiul)

                break
        else:
            DF.pop(-1)
    except:
         DF.pop(-1)
print(vizitat)

print()
print("rezolvarea de la f este: ")
#de la stop la start folosind DF:
drum_minim = n
BF = [] #coada cu elem tupluri (not,tata_nod)
BF.append(tuple((stop, -1)))
st = dr = 0
while st <=dr :
    tata = BF[st][0] #primul nod din coada => ultimul din lista
    try:
        for fiul in D[tata]:
            if fiul not in [nod for (nod, parinte) in BF]:
                BF.append((fiul, tata))
                dr += 1
                if BF[dr][1] == start and len(BF) < drum_minim:
                    drum_minim = len(BF)
    except:
        pass


    st += 1
print(drum_minim)
f.close()
g.close()