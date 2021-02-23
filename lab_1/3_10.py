x=int(input("x= "))
n=int(input("n= "))
p=int(input("p= "))
m=int(input("m= "))
d=0
while m>0:

    d=d+x*n
    x=x-(x*p/100)
    m-=n

if m<0:
    a=-m;
    d+=x;


print(d)