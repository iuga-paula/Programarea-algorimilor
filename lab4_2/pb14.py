def fisier_dict(nume_fisier):
    try:
        f = open(nume_fisier)
        l = []
        s = f.readline()
        while s!= "":
            D = {}
            s = s.replace("->", " ")
            s = s.split() #return lista de caractere
            D["plecare"] = s[0]
            D["sosire"] = s[1]
            D["ora_plecare"] = s[2]
            D["ore sosire"] = s[3]
            l.append(D)
            s = f.readline()
        f.close()
        return l

    except FileNotFoundError as file_not_found:
        print(file_not_found)

def timp_calatorie(ora_plecare, ora_sosire):
    # calculam tot timpul in minute
    timp_maxim = 23 * 60 + 59    #23 de ore și 59 de minute
    #spargem orele dupa":"
    ora_plecare = ora_plecare.split(":")
    ora_sosire = ora_sosire.split(":")
    ora_sosire[0] *= 60 # trans in min
    ora_plecare[0] *= 60
    if ora_sosire[1] > ora_plecare[1]:
        timp = ora_sosire[1] - ora_plecare[1]
    else:
        timp = ora_plecare[1] - ora_sosire[1]
        ora_sosire[0] -= 1
    timp = timp + ora_sosire[0] - ora_plecare[0]
    if timp > timp_maxim:
        print("calatoria depaseste durata maxima!")
        return None
    return timp

def calatorie(lista_program): #returnează o nouă listă de dicționare conținând cursele care o pot ajuta pe
                              #Ana să ajungă la destinație, direct sau indirect.
    l = lista_program
    ld = []
    BF = []  # coada cu elem tupluri (not,tata_nod)
    stop  = "Brasov"
    start = "Bucuresti"
    BF.append(tuple((stop, -1)))
    st = dr = 0
    while st <= dr:
        tata = BF[st][0] #primul nod din coada => ultimul din lista
    try:
        for fiul in l[tata]:
            if fiul not in [nod for (nod, parinte) in BF]:
                BF.append((fiul, tata))
                dr += 1
                if BF[dr][1] == start and len(BF) > 1:
                    for x in BF:
                        l[x[0]]
                        ld.append()

    except:
        pass


    st += 1

def scrie_fisier(lista_dict):
    lista_dict = calatorie(lista_program=fisier_dict(nume_fisier = input("dati nume fisier= ")))
    g = open("traseu.txt", "w")
    for x in lista_dict:
        g.write("Plecare la ora ")
        g. write(str(x["plecare"]))
        if len(x) > 4:
            g.write("schimbare in ")
            g. write(str(x["schimbare"]))
        g.write("sosire la ora ")
        g.write(str(x["sosire"]))
        g.write()

    g.close()


