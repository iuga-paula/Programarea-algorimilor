import sys
from math import modf
#rezolvare a):
Max = 0
Min = sys.maxsize
def min_max(*args):
    global Max
    global Min
    for x in args:
        if isinstance(x, int):  #type(x) == int:
            Max = x if x > Max else Max
            Min = x if x < Min else Min

        else:
            return None

    #else:
        #return None
    return Max, Min

#rezolvare b):
f = open("numere.txt")
g = open("impartire.txt", "w")
s = f.readline()
l = [float(x) for x in s.split()]
for x in l:
    y = modf(x)
    if y[1] == 0:
        x = int(x)
print(l)
print(min_max(*l))
try:
    if min_max(l):
        M, n = min_max(l)
        g.write(str(int(M/n)))

except FileNotFoundError as e3:
    print(e3)
except ValueError as e2:
    print(e2)
except ZeroDivisionError as e1:
    print(e1)
except Exception as e4:
    print(e4)
else:
    pass

f.close()
g.close()



