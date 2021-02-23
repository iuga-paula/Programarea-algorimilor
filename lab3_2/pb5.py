f = open("cuv.in")
s = f.readlines() #lista de linii
D1 = {}
for x in s:
   x = x.split()
   n = len(x)
   for i in range(n):
    #print(x[i])
    if x[i] in D1:
        D1[x[i]] = D1[x[i]] + 1
    else:
        D1[str(x[i])] = 1
print()
for x,y in D1.items():
    print(x,y) #am creat dictionarul D1 (functional) in care cheile sunt cuvintele iar valorile sunt frecventele acestora

D2 = {}
for x, y in D1.items():
   if y not in D2.keys():
       D2[y] = []
       D2[y].append(x)
   else:
       D2[y].append(x)
print()
for x, y in D2.items():
    print(x,y) #am creat dictionarul D2( functional), pe baza D1, in care cheile sunt frecventele iar valorile sunt liste de cuvinte ce apar
    # in fisier cu acea frecventa
kmi = min(D2.keys()) #am gasit key-ul minim din dict D2
kma = max(D2.keys()) #am gasit key-ul maxim din dict D2
x = D2[kmi] # sau x = D2.get(kmi)
y = D2[kma] # sau y = D2.get(kma)
x.sort()
y.sort()
print("cuvantul care apare cel mai rar este: ", x)
print("cuvantul care apare cel mai des este: ", y)







f.close()