n=int(input("n="))
ma1=0
ma2=0 #ma1>ma2
for i in range(n):
    x=int(input("x="))
    if x>ma2 and x<ma1:
        ma2=x
    elif x>ma1:
        ma2,ma1=ma1,x
if ma2!=ma1 and  ma1!=0 and ma2!=0:
    print(ma2,ma1)
else :
    print("Imposibil")


