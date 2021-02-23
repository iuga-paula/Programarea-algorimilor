"""
se cit n sa se creeze o mat cu latura 2^n
3 | 1
2 | 4
"""
def afisare(M):
    for l in M:
        print(*l, sep="\t")

,def completare(M,st,sus,lat):
    global nr
    if lat == 1:
        M[sus][st] = nr
        nr += 1
    else:
        lat = lat//2
        completare(M, st + lat, sus, lat)
        completare(M, st, sus + lat, lat)
        completare(M, st, sus, lat)
        completare(M, st + lat, sus + lat, lat)



n = int(input("dati n= "))
M = [[0 for x in range(2**n)] for y in range(2**n)]
print(M)
print(afisare(M))
nr = 1
completare(M, 0, 0, 2**n)
afisare(M)
