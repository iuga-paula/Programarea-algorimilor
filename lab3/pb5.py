f = open("prop.in")
s = f.readline()
s = s[:-1] # pt a elim caracterul "\n"
d1 = { (key, val) = s.split()
    d[int(key)] = val }
