f = open("cheltuieli.txt")
s = f.readline()
l = s.split() #l e lista de cuvinte
v = []
for cuv in l:
    if cuv.isdecimal():
         v.append(int(cuv))
    else :
        cuv1 = cuv.split(".")
        if len(cuv1) == 2 and cuv1[0].isdecimal() and cuv1[1].isdecimal():
            v.append(float(cuv))
n = len(v)
suma = 0
i = 0
while i < n:
    suma += v[i]*v[i+1]
    i += 2
f.close()
print("suma totala cheltuita este: ", suma)







