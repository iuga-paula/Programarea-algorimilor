s = input("dati sirul de numere intregi = ") # spațiu între numere și Enter doar la finalul șirului
l = [ int(x) for x in s.split()] #“list comprehensions”
M = sorted(set(l), reverse = True ) #multime pt a elimina duplicatele si cauta cele 2 valori maxime
print(M)
if len(M)>=2:
    print(M[0],M[1])
else:
    print("nu exista 2 valori maxime diferite")
