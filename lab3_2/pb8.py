f = open("fraza.in")
s = f.readline()
f.close()
cuv = input("dati cuvantul= ")

separatori = ",.?!:;"
for x in separatori:
    s = s.replace(x, " ")
s = s.split()
M = set(cuv) #pt a elimina lit care se repeta folosim o multime
#print(M)
for x in s:
    for y in M:
        if y not in x:
            break
    else:
        print(x)

