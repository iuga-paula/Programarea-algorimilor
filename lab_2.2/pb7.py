date = input("dati data completa= ")
v = [0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5] #vector pt preluare cod luna
data = date.split() #o sa avem data[0] data[1] si data[2]
"""print(type(data[0]))
print(type(data[1])) => toate sunt de tip string
print(type(data[2]))"""

day = int(data[0]) #codul pt zi

year = int(data[2]) #codul pt an
year = year % 100
year = (year + year//4) % 7

#codul pt an bisect
year1 = int(data[2])
leapyear = 0
if year1 % 4 ==0  and year1 % 100 !=0 or  year % 400 == 0:
    leapyear = 1

#dictionar pt ziua cautata:
dday = {1: "luni", 2: "marti", 3: "miercuri", 4: "joi", 5: "vineri", 6: "sambata", 7: "duminica"}
dcentury  = {17: 4, 18: 2, 19: 0, 20: 6, 21: 4, 22: 2, 23: 0}
x = year1//100
century = dcentury[x]

#dictionar pt luna cu sting:
dmonth = {"ianuarie": 0, "februarie": 3, "martie": 3, "aprilie": 6, "mai": 1, "iunie": 4, "iulie": 6, "august": 2, "septembrie": 5, "octombrie": 0, "noiembrie": 3, "decembrie": 5}
#dictionar pt luna cu numere:
dmonth1 = {1: 0, 2: 3, 3: 3, 4: 6,5: 1, 6: 4, 7:6, 8: 2, 9: 5, 10: 0, 11:3, 12: 5}

try:
    month = int(data[1])
    month = dmonth1[month]
    #print(month)
except:
    month = dmonth[data[1]]
    #print(month)

f = (year + month + century + day - leapyear) % 7
print(dday[f])








