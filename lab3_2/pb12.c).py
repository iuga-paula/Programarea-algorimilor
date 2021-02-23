#sbpucntul a)
#sirul se termina cu -1
s = input("dati valoarea= ")
nr_ord = 1
rez = [0]*0
while s != "-1":
    s = s.split()
    elem = tuple((int(s[0]), s[1], nr_ord))
    rez.insert(len(rez),elem)
    s = input("dati valoarea= ")
    nr_ord += 1

print("rezolvare a) :", rez)

#subpunctul b)
M = set([x[0] for x in rez])
print("rezolvare b) :", M)

#rezolvare c):
rez = sorted(rez, key=lambda x: (-x[0], x[2]))
print(rez) #rezultatul sortat dupa punctaje si dupa ordinea trimiterii punctajului
import collections
D = collections.OrderedDict()
for x in rez:
    if x[0] not in D.keys():
        D[x[0]] = []
        D[x[0]].append(tuple((x[1], x[2])))
    else:
        D[x[0]].append(tuple((x[1], x[2])))
print("rezolvare c): ", D)

