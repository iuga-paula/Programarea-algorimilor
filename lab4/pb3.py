import sys
#rezolvare a):
def min_max(*args):
    Max = None
    Min = sys.maxsize
    if len(args) :
        for x in args:
            if isinstance(x,int):  #type(x) == int:
                Max = x if x > Max else Max
                Min = x if x < Min else Min

            else:
                return  None
        return Max, Min
    else:
        return None

#rezolvare b):
f = open("numere.txt")
g = open("impartire.txt", "w")
s = f.read()
l = [int(float(x))  for x in s.split()]
print(min_max(l))
try:
    if min_max(l):
        M,n = min_max(l)
        g.write(str(int(M/n)))

except FileNotFoundError as e3:
    print(e3)
except ValueError as e2:
    print(e2)
except ZeroDivisionError as e1:
    print(e1)
except Exception as e4:
    print(e4)


f.close()
g.close()



