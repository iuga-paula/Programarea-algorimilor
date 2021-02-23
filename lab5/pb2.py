f  = open("spectacole.txt")
g = open("program.txt", "w")
l = []
s = f.readline()

while s!="":
    s = s.replace("-", " ")
    x = tuple((x for x in s.split(" ",2)))
    l.append(x)
    s = f.readline()
f.close()

l.sort(key=lambda  x: x[1]) #sortare lista cr dupa ora de sf
ora_sf = l[0][1] #ora de sf a primului spectacol
g.write("{}\t{}\t{}\n".format(*l[0])) #afiseaza primul spectacol

for x in l:
    if x != l[0] and x[0] >= ora_sf:
        #print(ora_sf,x[0])
        ora_sf = x[1]
        g.write("{}\t{}\t{}\n".format(*x))


g.close()