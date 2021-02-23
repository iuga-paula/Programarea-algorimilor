s = input("dati textul de modificat: ")
'''s1 = s
t = s.split('.')
print(t)
print(s1)'''
i = 0
poz1 = 0
poz2 = len(s)-1
f = poz2
while poz2 > 0:
    if poz2>0 and s[poz2].isupper() and s[poz2-1] =='.' :
        poz1 = poz2
        for i in range(poz1,f+1,1):
            print(s[i], end="")
        f = poz1-1
        print()
    poz2 -= 1

for i in range(0,f+1,1):
    print(s[i],end="")