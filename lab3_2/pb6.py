f = open("lorem.in")
s = f.readlines() #lista cu liniile
D = {}
#a = ""
for x in s:
    x = x.split()
    #print(x)
    for lit in x :
        for y in lit:
            if y.isalpha():
                if y not in D.keys():
                    D[y] = 1
                else:
                    D[y] = D[y] + 1


    #b = "".join(x)
    #a = a + b
#print()
#print(a)
f.close()
for x,y in D.items():
    print(x,y)
