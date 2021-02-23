def bkt(k):
    global x,n
    for v in range(1,n+1):
        x[k] = v
        if v not in x[:k]:
            if k == n-1:
                print(x[:k+1])
            else:
                bkt(k+1)

n = int(input("dati n= "))
x = [0]*n
bkt(0)