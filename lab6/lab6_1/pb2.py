def citireDATE():
    f = open("copaci.in")
    s = f.readline()
    s += " " + f.readline()
    dreptunghi =[int(x) for x in s.split()]
    s = f.readline()
    l = []
    while s != "":
        x = tuple([int(x) for x in s.split()])
        l.append(x)
        s = f.readline()
    return (*dreptunghi, l)
    f.close()

def dreptunghiArieMaxima(st,jos, dr, sus):
    global C
    gasit = False
    M = 0, None

    for copac in C:
        if st < copac[0] < dr and\
            jos < copac[1]< sus:
            gasit = True
            d1 = dreptunghiArieMaxima(st, jos, copac[0], sus) #taiet pe verticala x -ul copacului
            d2 = dreptunghiArieMaxima(copac[0], jos, dr, sus)
            d3 = dreptunghiArieMaxima(st, copac[1], dr, sus) #taiet pe orizontala y -ul  copacului
            d4 = dreptunghiArieMaxima(st, jos, dr, copac[1])
            l = sorted([d1, d2, d3, d4], reverse=True) #sort cr dupa arie
            if l[0][0] > M[0]:
                M = l[0]
    if gasit == False:
        A = (dr-st)*(sus-jos) #L*l
        return A, [st, jos, dr, sus]
    else: #daca s-a gasit copac
        return M


print(citireDATE())
rez = citireDATE()
C = rez[-1] #lista de copaci
print(dreptunghiArieMaxima(*rez[:-1]))
rezf = dreptunghiArieMaxima(*rez[:-1])
g = open("copaci.out", "w")
g.write("Dreptunghiul:\n")
g.write("{}\t{}\n".format(rezf[1][0], rezf[1][1]))
g.write("{}\t{}\n".format(rezf[1][2], rezf[1][3]))
g.write("Aria Maxima:\n")
g.write(str(rezf[0]))
g.close()

