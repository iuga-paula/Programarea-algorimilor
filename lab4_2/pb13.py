def  cautare_cuvant(cuv, nume_fis_out, *nume_fis_in):
    g  = open(nume_fis_out,"w")
    for x in nume_fis_in:
        try:
            f = open(x)
            nr_linie = 1
            ok = False
            s = f.readline()
            while s != "":
                c = s.split()
                if cuv in c:
                    ok = True
                    g.write(str(nr_linie))
                nr_linie += 1
                s = f.readline()
            if ok == False:
                g.write("nu s-a gasit cuvantul in fisierul " + str(x))
            f.close()
        except FileNotFoundError:
            pass
    g.close()

cuv = input("dati cuvanul de cautat= ")
s = input("dati numele fisierelor de intrare = ")
nume_fis_out = input("dati numele fisierului de iesire = ")
nume_fis_in = [ x for x in s.split()]
cautare_cuvant(cuv,nume_fis_out,*nume_fis_in)

