s = input("dati dialogul= ")
v1 = 0
v2 = 0
n = len(s)
for i in range(n):
    if i > 1 and s[i].isdigit() and s[i-1] == '$' and v1 == 0:
        j = i
        while s[j].isdigit() and j < len(s):
            v1 = v1 * 10 + int(s[j])
            j += 1
    elif i > 1 and s[i].isdigit() and s[i-1] == '$' and v2 == 0:
        j = i
        while s[j].isdigit() and j < len(s):
            v2 = v2 * 10 + int(s[j])
            if j+1 <len(s):
                j += 1
    if v1 and v2:
        break

print(v1,v2)

x = 0
y = 0

for i in range(n):
    if i > 1 and s[i].isdigit() and s[i-1] == '$':
        j = i
        v1=0
        while s[j].isdigit() and j < len(s):
            v1 = v1 * 10 + int(s[j])
            j += 1
        if x==0:
            x=v1
        elif y==0:
            y=v1
        else:
            x=y
            y=v1
if x == y:
    print("s-au inteles")
else:
    print("NU s-au inteles")




