s = input("dati numele si prenumele: ")
t = s.split()
ok = 1 # presupunem ca numele este corect numdele de fam este departit de prenume printr-un spatiu
if len(t) > 3:  #daca avem mai mult de un nume de fam si 2 prenume atunci datele de intrare sunt gresite
    ok = 0

for x in t:
    if len(x) < 3: #daca un nume ori prenume are mai putin de 3 caractere atunci datele de intrare sunt gresite
        ok = 0
        break
    if x[0].islower():
        ok = 0
        break


for x in s:
    if x.isalpha() == False and x != ' ' and x != '-': #datele sunt gresite daca nume contine alte caractere in afara de spatiu sau cratima
        ok = 0
        break

nrcratime = s.count("-")
if nrcratime > 1: #daca nr de cratime este mai mare decat 1 atunci datele sunt gresite
    ok = 0
print("numarul de cratime este: ",nrcratime)

if ok:
    print("numele este corect")
else:
    print("numele nu este corect")