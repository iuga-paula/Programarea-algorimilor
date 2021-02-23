from my_module import *
n = 0
v = []

citeste(n, v)
print(v)

afisare(v)

l = valpoz(v)
afisare(l)

semn(l)
semn(v)

for x in v:
    if x not in l:
        print(-x, end=' ')