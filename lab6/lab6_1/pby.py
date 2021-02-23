"""
se cit n si o loc  = 0 din matricea prt cu lat n
si apoi se compl cu piese de tip L
"""

def afisare(M):
    for l in M:
        print(*l, sep="\t")

def completare(M, lat, lin, col, x, y): #x si y sunt casutele completate
    global nr
    if lat == 2:
        poz = [(lin, col), (lin, col+1), (lin+1, col), (lin+1, col+1)]
        for i,j in poz:
            if M[i][j] == -1:
                M[i][j] == nr
            nr += 1
    else:
        mij = lat//2
        if x < mijl:
            M[mij][mij-1] = nr
            M[mij][mij] = nr

            if y < mij:
                M[mij-1][mij] = nr
            else:
                M[mij][mij] = nr


n = int(input("n = "))
lin = int(input("lin= "))
col = int(input("col= "))
M = [[0 for x in range(2**n)] for y in range(2**n)]
nr = 1
M[lin][col] = 0
#atentie la divide mat apelate recursiv trb sa aibe aceeasi sturctura!!
completare(M, 2**n, 0, 0, lin, col)