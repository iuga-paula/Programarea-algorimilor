import math
a=int(input("dati primul coef= "))
b=int(input("dati al doilea coef= "))
c=int(input("dati al treilea coef= "))
d=b*b-4*a
x=math.sqrt(d)
if d<0 :
    print("ecuatia nu are nicio radacina")
elif d==0 :
    print(-b/(2*a))
else :
    print ((-b+x)/(2*a),(-b-x)/(2*a))


