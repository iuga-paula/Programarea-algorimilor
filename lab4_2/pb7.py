f = open("cuvinte.txt")
s = f.readline()
l = [x for x in s.split()]
#rezolvare a): sort. descr, comparare implicita
l.sort(reverse=True) #modifica si lista initiala
print(l)
#rezolvare b): sort.cresc lung cuv + ord alfabetica
l.sort(key=lambda x: (len(x), x))
print(l)
#rezolvare c): dupa lung, pt acceasi lung pastreaza ordinea din lista initiala
#
# def comp(x,y):
#     if len(x) < len(y):
#         return len(x)
#     elif len(x) > len(y):
#         return len(y)
#     else:
#         return x
#
# l.sort(key=comp())
def poz(x):
    if x in l:
        return l.index(x)

l.sort(key=lambda x: (len(x), poz(x)))
print(l)
f.close()