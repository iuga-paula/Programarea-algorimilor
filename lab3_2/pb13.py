n = int(input("dati nr natural n= "))
# python nu are un tip predefinit pt matrice asa ca cream o lista de liste: 1 lista din lista este prina linie si asmd.
l = [0]*0
x = [0]*0
y = 1
for i in range(n):
    for j in range(n):
        x.insert(len(x), y)
        y += 1
    l.insert(len(l), x)
    del x
    x = [0] * 0
print("rezolvare a): ")
for x in l:
    print(x, end="\n")
#print(l)
lista_poz = [0]*0
if n % 2:
    k = n//2 + 1 #daca n este impar, atunci sunt n/2+! rame de parcurs
else:
    k = n//2 #daca n este par atunci sunt n/2 rame de parcurs

i = 0
while i < k:# pt fiecare rama se parcurg laturile
    j = i
    while j < n-i+1:  #parcurgele latura de sus
        lista_poz.insert(len(lista_poz), tuple((int(i),int(j))))
        j += 1
    j = i + 1
    while j < n -i + 1: #parcurgele latura din dreapta
        lista_poz.insert(len(lista_poz), tuple((i, n-i+1)))
        j += 1

    j = n - i
    while j >= i: #parcurgere latura de jos
        lista_poz.insert(len(lista_poz), tuple((n-i+1, j)))
        j -= 1
    j = n-i
    while j >= i + 1: #parcugere latura din dreapta
        lista_poz.insert(len(lista_poz), tuple((j, i)))
        j -= 1
    i += 1

print("rezolvare b): ")
print(lista_poz)
lista_val = [0]*0
for x in lista_poz:
   try:
       lista_val.insert(len(lista_val), l[x[0]][x[1]])
   except:
       pass
print("rezolvare c): ")
print(lista_val)

