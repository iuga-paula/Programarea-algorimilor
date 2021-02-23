#student e lista de liste => inf pt fiecare student intr-o lista(nume,gr,nr_credite)
f = open("student.in")
student = []
s = f.readline()
n = 1
while s != "":
    s = s.strip('\n')
    l = [x for x in s.split(',')]
    student.append(l)
    s = f.readline()
    n += 1
f.close()
print(student)
def situatie_scolara(n, t, c): #t nu are credite
    global student
    for x in range(n-1):
        if int(t[x][2]) >= c:
            print("promovat")
            student[x].append("promovat")
        else:
            print("neproovat")
            student[x].append("nepromovat")

situatie_scolara(n,student,10)
print(student)
D = {} #gr sa fie cheie
for x in student:
    if x[1] not in D.keys():
        D[x[1]] = []
        l = []
        l.append(x[0])
        l.append(x[2])
        l.append(x[3])
        D[x[1]].append(l)
    else:
        l = []
        l.append(x[0])
        l.append(x[2])
        l.append(x[3])
        D[x[1]].append(l)

print(D)
for x in sorted(D.keys()):
    print(x)
    l = D[x].copy()
    print(sorted(l, key=lambda l:l[2]))
#print(sorted(D.items()))
