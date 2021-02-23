def is_in(a,b):
    count = 0
    while b!=0:
        if b%10==a:
            count = count+1
        b = b//10
    return count

n = int(input("n="))
am_zero = is_in(0, n)
temp_zero = am_zero
nr_min = 0
#construiesc minimul, verificand fiecare cifra de la 1 la 9 si tiannd cont de 0 separat
for i in range(1,10):
    temp_cif = is_in(i, n)
    while temp_cif!=0:
        nr_min = nr_min*10+i
        temp_cif = temp_cif-1
        if nr_min != 0:
            while am_zero != 0:
                nr_min = nr_min * 10
                am_zero = am_zero - 1

nr_max = 0
am_zero = temp_zero
temp_min = nr_min
#construiesc inversul, tinand iar cont de 0
while temp_min!=0:
    if temp_min%10!=0:
        nr_max = nr_max*10+temp_min%10
    temp_min = temp_min//10
while am_zero!=0:
    nr_max = nr_max*10
    am_zero = am_zero-1

print(nr_min, nr_max)

