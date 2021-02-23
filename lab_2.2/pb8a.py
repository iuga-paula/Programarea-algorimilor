s = input("dati sirul de tradus in pasareasca= ")
i = 0
while i < len(s):
    if s[i] in "aeiouAEIOU":
        x = s[i]
        aux = s[i+1:]
        s = s[:i+1] + "p" + x+  aux
        i+=2
        print(s)
    i+=1

print("sirul in pasareasca este :" , s)

i = 0
while i < len(s):
    if i > 0 and s[i]=='p' and s[i-1] in "aeiouAEIOU":
        s = s[:i] + s[i+2:]
    i+=1

print("sirul normal este :" ,s)

