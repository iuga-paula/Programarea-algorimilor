import  re
def determina_ip(nume_fis):
    f = open(nume_fis)
    s = f.readline()
    while s != "":
        x = re.findall("^PING", s)
        if (x):
            x = re.sub("PING", " ", s)
            x = x.split(" ", 2)
            IP = x[0]
            x[1] = re.sub('[^0-9a-zA-Z]+', '.', x[1])
            x[1] = x[1].rstrip('.')
            x[1] = x[1].lstrip('.')
            DNS = x[1]
        s = f.readline()
    f.close()
    return IP, DNS

def nr_pachete(nume_fis):
    f = open(nume_fis)
    s = f.readline()
    cuv = s
    while s != "":
        x = re.search("packets transmitted", s)
        if (x):
            nr_pct = s[:x.start()]
            nr_pct = nr_pct.rstrip()
            nr_pct = nr_pct.lstrip()
        s = f.readline()
        if s != "":
            cuv += s
    x = re.findall("\A64 bytes..from..icmp_seq..time", cuv)
    nr_int = len(x)
    return  nr_pct,nr_int

    f.close()

def verificare_timp(nume_fis):
    f = open(nume_fis)
    s = f.readlines()
    ultima_linie = s[len(s) - 1]
    removelist = "."
    x = re.sub(r'[^\w' + removelist + ']', ' ', ultima_linie)
    x = x.split()
    tmin = min(x)
    tmax = max(x)
    for elem in x:
        if elem != tmin and elem != tmax:
            tmed = elem

    for elem in x:
        if elem not in s:
            return 0
    return tmin, tmed, tmin
    f.close()


nume_fis = input("dati numele fisierului in care cautam= ")
t = determina_ip(nume_fis) #tuplu
g = open("ping.out", "w")
numere = nr_pachete(nume_fis)
if verificare_timp(nume_fis) != 0:
    g.write("timp minim:\t{}\ntimp mediu:\t{}\ntimp maxim: \t{}\n".format(*verificare_timp(nume_fis)))
else:
    g.write("eroare")
g.write("IP:\t{}\tDNS:\t{}\n".format(*t))
g.close()