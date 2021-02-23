s = input("dati sirul de prelucrat= ")
s1 = s
og = s[::-1]
og1 = og
n = len(s) - 1
l = list(s)
log = list(og)
if l[n] == log[0]:
    c = l[n]
    """i = n
    while l[i] == c: #sterge ultimele caractere
        l = l[-1]
        i -= 1
    j = 0
    while log[j] == c:
        log = log[:1]
        j += 1

l = l + log
rez1 = "".join(l)
"""
for i in range(n,-1):
    if l[i] == c:
        l = l[-1] #sterge ultimele caractere
    else:
        break
for i in range(n):
    if og[i] == c:
        og = og[:1] #sterge primele caractere
    else:
        break





s = "".join(l)
og = "".join(og)
print(s)
print(og)

print("sir1<op>sir1_og", s + og)
