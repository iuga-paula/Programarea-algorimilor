s=input("dati sirul de criptat ")
k=int(input("dati cheia secreta "))

a=list(s)
n=len(a)
for x in range(n):
    a[x] = chr(ord(a[x])+k)
    if (ord(a[x]) >ord('z')):
        a[x]=chr(ord(a[x]-26))
   #print(x)

s = "".join(a)
print(s)
print('\n')

#decpritare pe sirul obtinut:
for x in range(n):
    a[x] = chr(ord(a[x])-k)
    if (ord(a[x]) <ord('a')):
        a[x]=chr(ord(a[x]+26))

s = "".join(a)
print(s)
print('\n')


