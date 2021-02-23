f = open("cuburi.txt")
g = open("turn.txt", "w")

s = f.readline()
s =s.strip()
nr_cuburi = int(s)
s = f.readline()

cuburi = []
while s != "":
    s = s.split()
    cuburi.append(tuple((int(s[0]),s[1])))
    s = f.readline()
f.close()
print(cuburi)
cuburi.sort(key= lambda x:x[0], reverse=True) #sortare descr dupa lungime latura
print(cuburi)

h_turn = cuburi[0][0]
culoare = cuburi[0][1]

g.write("{}\t{}\n".format(*cuburi[0]))

for x in cuburi[1:]:
    if x[1] != culoare:
        g.write("{}\t{}\t\n".format(*x))
        h_turn += x[0]
        culoare = x[1]

g.write(str(h_turn))

g.close()