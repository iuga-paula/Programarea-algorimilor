from math import pi
#rezolvare a):
def lungime_arie_cerc(r):
    return 2* pi * r, r * r * pi

#rezolvare b):
r = float(input("dati nr real r= "))
#print(round(1.23455,3))
x = lungime_arie_cerc(r)
print(round(x[0],3), round(x[1],3))



