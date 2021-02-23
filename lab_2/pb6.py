s = input("dati fraza= ")
n = len(s)
suma = 0

sep = ";?!:.,/ "
for x in sep:
    s = s.replace(x, " ")
s = s.split()
for x in s:
    if s.isdecimal() == True:
        suma += int(s)


print(suma)



