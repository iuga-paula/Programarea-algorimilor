import math
L1=int(input("L1= "))
L2=int(input("L2= "))
A=L1*L2
while L2>0:
    X=L1%L2
    L1=L2
    L2=X

#IN L1 e divi
l=L1 #Dimensiunea placa
X=A//(l*l)
print("dimensiunea placa este ", l)
print("numarul de placa este ", X)


