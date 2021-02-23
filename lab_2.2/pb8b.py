s = input("dati sirul de tradus: ")
i = 0
while i < len(s):
    if s[i] == '-' and i > 0:
        aux = s[i-1]
        s = s[:i+1] + "p" + aux + s[i+1:]
    i+=1
print(s)

for x in s:
    if x != '-':
        print(x, end="")

print()

i = 0
while i < len(s):
    if s[i] == '-' and i+1 < len(s):
        s = s[:i+1] + s[i+3:]
        i+=2
    i+=1
print(s)
