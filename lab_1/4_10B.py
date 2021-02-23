n=int(input("n= "))
ok=0;
ma=0.00;
#ma,zi1,zi2
x=float(input("curs/zi= "))
for i in range(n-1):
    y=float(input("curs/zi= "))
    if y-x>ma:
        ok=1
        ma=y-x
        zi1=i+1
        zi2=i+2
if ok!=0 :
    print(round(ma,2),zi1,zi2)
else :
    print("nu exista CRESTERE")




