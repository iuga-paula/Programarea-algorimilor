f = open("test.in")
g = open("test.out","w")
nota = 1
line = f.readline()
while line != "":
    l = line.split("=") # lista l va avea 2 elem x*y, rez
    rez = int(l[1])
    s = l[0]
    l1 = s.split("*")
    x = int(l1[0])
    y = int(l1[1])
    g.write(line[:-1] + " ")
    if x * y == rez:
        nota += 1
        g.write("corect")
    else:
        g.write("gresit" + " " + str(x*y))
    g.write("\n")
    line = f.readline()



print(nota)
f.close()
g.write("nota" + " "+ str(nota))
g.close()