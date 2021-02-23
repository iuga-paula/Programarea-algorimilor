def cmpValori(i, j, L):
    if L[i] != L[j]:
        return False
    return True

def cautare(x, L, cmpValori):
    n = len(L)
    if x not in L:
        return None
    else:
        i = L.index(x) #prima ap a valorii x
        for j in range(n-1, 0, -1):
            if i != j and cmpValori(i, j, L) is True:
                return j

def palindrom(L):
    n = len(L)
    for i in range(n//2):
        if (n - 1 - i) != cautare(L[i], L, cmpValori):
            return False
    return True

s = input("dati lista = ")
L = [int(x) for x in s.split()]
#print(cmpValori(0, 4, L))
#print(cautare(10, L, cmpValori))

if palindrom(L) is True:
    print("este palindrom")
else:
    print("Nu e palindrom")