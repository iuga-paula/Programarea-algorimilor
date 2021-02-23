#geneare nr cu cifre dist si suma s
def suma(lista):
    s = 0
    for elem in lista:
        s += elem
    return s



def bkt(k):
   global x, n
   for v in range(n):
       x[k] = v
       sum = suma(x[:k+1])
       if sum <= n and v not in x[:k] and x[0] !=0 : #if sol partiala
           if sum == n: #if sol finala
               print(x[:k+1])
               if 0 not in x[:k+1]:
                   #x.append(0)
                   #k += 1
                   x[k + 1] = 0
                   print(x[:k+2])

           else:
               bkt(k+1)



f = open("generare.in")
s = f.read()
s = s.strip()
n = int(s)
x = [0]*100
bkt(0)
f.close