#cum fac un fisier fara nume?
numefisier = input("dati numele fisierului: ")
try:
    f = open(numefisier,"r")
    s = f.readline()
    #print(s)
    print("cuvintele care rimeaza sunt:")
    s = s.split()
    D = {} #dictionar in care cheile sunt utlimele 2 litere din fiecare cuv iar valorile sunt liste de cuvinte ce se termina in acele 2 litere,
    # deci rimeaza
    for cuv in s:
        n = len(cuv)
        if cuv[n-2:n] not in D.keys():
            D[cuv[n-2:n]] = []
            D[cuv[n - 2:n]].append(cuv)
        else:
            D[cuv[n - 2:n]].append(cuv)
    for x in D.values():
        x.sort()
        print(x)


    f.close()
except:
    print("Nu exista fisier cu acest nume!")
