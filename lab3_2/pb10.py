f = open("inventar.txt")
D = {}
s = f.readline()
I = set ()
R = set ()
Dif = set ()
while s != "":
    s = s.split(" ")
    #D[s[0]] = set( [int(x) for x in s[1:] if x.isdigit()] )
    D[s[0]] = set()
    for x in s[1:]:
        if x.isdigit():
            D[s[0]].add(int(x))
            D[s[0]] = set(D[s[0]])
    if len(I) == 0:
        I = D[s[0]]
    else:
        I = I & D[s[0]]
    if len(R) == 0:
        R = D[s[0]]
    else:
        R = R | D[s[0]]
    if len(Dif) == 0:
        Dif = D[s[0]]
    else:
        Dif = Dif - D[s[0]]
    s = f.readline()
f.close()
print("rezolvare subpunctul a: ")
for x, y in D.items():
    print(x, y)
print()

print("rezolvare subpunctul b: ") #inters multimile val
print(I)

print("rezolvare subpunctul c: ") #reuniune multimile val
print(R)

print("rezolvare subpunctul d: ") #dif multimile val
print(Dif)