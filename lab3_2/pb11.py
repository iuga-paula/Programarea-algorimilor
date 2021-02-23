f = open("dict.in")
s = f.readline() #observam ca, daca cuv este definiend atunci cele  2 pcte sunt lipite de el
# este clar ca prima linie incepe cu primul definiend urmat de definitia acestuia
elem1 = [0]*0
elem2 = [0]*0
linieant = s.split()
liniecurenta = f.readline()
nrcuv = 0
nrtilda = 0
OK = 0
while liniecurenta != "":
    liniecurenta = liniecurenta.split()
    cuv = str(linieant[0])
    if cuv[0] == "\"" and cuv[len(cuv)-1] == ":":
        definit = cuv[1:len(cuv)-1]

        print(definit)
        #if cuv in linieant[1:]:
            #nrcuv = linieant[1:].count(definit)
        #else:
    nrcuv += linieant.count(definit)
    nrtilda += linieant.count("~")

    #nrcuv += liniecurenta.count(cuv)

    #nrtilda += liniecurenta.count("~")
    if "\\n\"" in liniecurenta:

        #facem tuplu din cuv si nr pe care apoi il atasam la rez
        nrcuv += liniecurenta.count(definit)
        nrtilda += liniecurenta.count("~")
        nr = nrcuv + nrtilda
        print(nrcuv,nrtilda)
        elem = tuple((definit, nr))
        print(elem)
        elem1.insert(len(elem1), definit)
        elem2.insert(len(elem2), nr)
        nrcuv = 0
        nrtilda = 0



    linieant = liniecurenta
    liniecurenta = f.readline()

f.close()
rez = list(zip(elem1,elem2)) #concateneaza elem din 2 liste sub forma unei liste de tupluri
print(rez)