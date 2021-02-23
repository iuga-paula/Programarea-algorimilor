f = open("persoane.in")
#lista de dictonare de dicitonare
s = f.readline()
l = [0]*0
print(type(s))
sep = ".,:}"
while s != "":
    s = s.split("{")
    dictpp = s[0] #cheile principale
    dictsec = s[1] #cheile secundare
    for x in sep:
        dictpp = dictpp.replace(x, " ")
        dictsec = dictsec.replace(x, " ")
    dictpp = dictpp.split()
    dictsec = dictsec.split()

    #print(dictpp,dictsec , end="~")

    # D = {}
    # np = len(dictpp)-1
    # ns = len(dictsec)
    # for i in range(np, 2):
    #     D[dictpp[i]] = dictpp[i+1]
    #
    # if D[dictpp[np]][dictsec[0]] not in D.keys():
    #     D[dictpp[np]][dictsec[0]] = {}
    #     D[dictpp[np]][dictsec[0]] = dictsec[1]
    #
    #
    # if ns % 2 != 0:
    #     s = dictsec[3]  + dictsec[4]
    #     D[dictpp[np]][dictsec[2]] = s
    #     D[dictpp[np]][dictsec[5]] = dictsec[6]
    # else:
    #     D[dictpp[np]][dictsec[2]] = dictsec[3]
    #     D[dictpp[np]][dictsec[4]] = dictsec[5]
    # print(D)
    D1 = {}
    D2 = {}
   # print(dictpp)
    np = len(dictpp) - 1
    for i in range(0, np, 2):
        D1[dictpp[i]] = dictpp[i+1]
   # D1[dictpp[np]] = 0 #am form dict1
    #print(D1)
    ns = len(dictsec)
    D2[dictsec[0]] = dictsec[1]
    if ns % 2:
        D2[dictsec[2]] = dictsec[3] + " " + dictsec[4]
        D2[dictsec[5]] = dictsec[6]
    else:
        D2[dictsec[2]] = dictsec[3]
        D2[dictsec[4]] = dictsec[5]

    #print(D2) #am creat dict2
    D1['adresa'] = D2
    #print(D1)
    l.insert(len(l),D1)
    s = f.readline()

f.close()
print(l)
print()
for x in l:
    print(x)
