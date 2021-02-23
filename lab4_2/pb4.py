from math import sqrt
def e_prim(x):
    if x < 2 or x > 2 and x % 2 == 0:
        return 0
    else:
        for d in range(3, int(sqrt(x)), 2):
            if x % d == 0:
                return 0
    return 1
#print(e_prim(23))

def nr_prime(): #generator infinit de numere prime
    x = 1
    while True:
        x += 1
        if e_prim(x):
            yield x

n = int(input("dati n= "))
print("rezolvare  a): ")
y = nr_prime()
x = next(y)
while x < n:
    print(x, end=" ")
    x = next(y)
print()
print("rezolvare b): ")
x = nr_prime()
y = next(x)
i = 1
while i <= n:
    print(y, end=" ")
    y = next(x)
    i += 1
