f = open("bani.txt")
g = open("plata.txt", "w")
s = f.readline()
bancnote = [int(x) for x in s.split()]

s = f.readline()
suma = int(s)
f.close()
bancnote.sort(reverse=True)
print(bancnote)
g.write(str(suma) + " = ")
ok = True
for x in bancnote:
    if x > suma:
        continue
    if suma != 0:
         nr_max = suma//x
         suma = suma % x
         if ok != True:
             g.write(" + ")
             ok = False
         g.write(str(x) + "*" + str(nr_max))
    else:
        break


g.close()