def citeste(n, v):
    n = int(input("dati n= "))
    s = input("dati lista= ")
    for x in s.split():
        v.append(int(x))

def afisare(v):
    for x in v:
        print(x, end=" ")


def valpoz(v):
    poz = [x for x in v if x > 0]
    return poz


def semn(v):
    for x in v:
        v = [-x for x in v]



