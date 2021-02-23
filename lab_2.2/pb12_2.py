s1 = input("dati sirul 1= ")
s2 = input("dati sirul 2= ")
#if len(list)==0 or if not a => avem lista vida

aux1 = s1
aux2 = s2  #copii pt a realiza op2
a = s1
b = s1[::-1] #oginditul lui s1
print("oglinditul lui s1 este: ", b)
n1 = len(s1) - 1
n2 = len(s2) - 1
if s1[n1] == s2[0]:  #pt op1 daca ultima litera din s1 este egala cu prima litera din s2 at. stergere
    x = s1[n1]
    s1 = s1.rstrip(x) #elim caracterle x de la sfarsitul lui s1
    s2 = s2.lstrip(x) #elim caracterele x de la inceputul lui s2 pt aplica op1

print("sir_1 <op> sir_2", s1 + s2)
"""print(aux1)
print(aux2)
"""
if aux1[0] == aux2[n2]:  #pt op2 daca ultima litera din s2 este egala cu prima litera din s1 at. stergere
    x = aux1[0]
    aux1 = aux1.lstrip(x) #elim caracterle x de la sfarsitul lui s2
    aux2 = aux2.rstrip(x) #elim caracterele x de la inceputul lui s1 pt aplica op1
print("sir_2 <op> sir_1", aux2 + aux1)

#pt og sirului 1
a1 = a
b1 = b
if a[n1] == b[0]:  #pt op1 sir + oglindit
    x = a[n1]
    a = a.rstrip(x)
    b = b.lstrip(x)

if a1[0] == b1[n2]:  #pt op2 daca ultima litera din s2 este egala cu prima litera din s1 at. stergere
    x = a1[0]
    a1 = a1.lstrip(x) #elim caracterle x de la sfarsitul lui s2
    b1 = b1.rstrip(x) #elim caracterele x de la inceputul lui s1 pt aplica op1
print("sir_1 <op>sir_1_oglindit", a + b)
print("sau sir_1_oglindit<op> sir_1", b1 + a1)
if len(a + b)> len(b1 + a1):
    print("op1")
else:
    print("op2")

