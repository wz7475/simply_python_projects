def znajdz_dzielniki(a):
    dzielniki = []
    if a >= 0:
        for i in range(1, a+1):
            if a % i == 0:
                dzielniki.append(i)
                dzielniki.append(i*(-1))
    else:
        for i in range(a-1, 0):
            if a % i == 0:
                dzielniki.append(i)
                dzielniki.append(i*(-1))
                dzielniki.append(i*0.5)
                dzielniki.append(i*(-0.5))
    return dzielniki


print("""wpisz wartosci wspolczynnikow (od 3 lub 4 potegi) odzdziel je spacjami, nacisnij Enter,
jesli nie ma zadnej liczby wyswietlonej to oznacza ze nie ma takiej liczby do hornera, wpisz jescze raz inne liczby.""")
while True:
    liczby1 = (input().split(" "))
    liczby = []

    for i in liczby1:
        i = int(i)
        liczby.append(i)

    if len(liczby) == 4:
        dzielniki = znajdz_dzielniki(liczby[-1])

        for i in dzielniki:
            suma = liczby[0] * (i ** 3) + liczby[1] * \
                (i ** 2) + liczby[2] * i + liczby[3]
            if suma == 0:
                print(i)
                break
    elif len(liczby) == 5:
        dzielniki = znajdz_dzielniki(liczby[-1])

        for i in dzielniki:
            suma = liczby[0] * (i ** 4) + liczby[1] * (i ** 3) + \
                liczby[2] * i * i + liczby[3] * i + liczby[4]
            if suma == 0:
                print(i)
                break
