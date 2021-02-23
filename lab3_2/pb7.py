D1 = {"ana": 1234,
      "buni": 100,
      "mami": 120,
      "bunicu": 240,
      "tati": 244}
D2 = {"ana": 120,
      "maria": 200,
      "mami": 130,
      "tati": 100}
Dnou = D1
for x,y in D2.items(): #x = cheie, y = valuare
    if x not in Dnou.keys():
        Dnou[x] = y
    else:
        Dnou[x] = Dnou[x] + y
for x, y in Dnou.items():
    print(x, y)

