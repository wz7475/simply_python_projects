def znajdz_dzielniki():
    dzielniki = []
    if liczba5 >= 0:
        for i in range(1,liczba5+1):
            if liczba5 % i == 0:
                dzielniki.append(i)
                dzielniki.append(i*(-1))
    else:
        for i in range(liczba5-1,0):
            if liczba4 % i == 0:
                dzielniki.append(i)
                dzielniki.append(i*(-1))
                dzielniki.append(i*0.5)
                dzielniki.append(i*(-0.5))
    return dzielniki

while True:
    liczba1, liczba2, liczba3, liczba4, liczba5 = (input().split(" "))
    liczba1=float(liczba1)
    liczba2=float(liczba2)
    liczba3=float(liczba3)
    liczba4=int(liczba4)
    liczba5 = int(liczba5)

    dzielniki=znajdz_dzielniki()
    for i in dzielniki:
        suma = liczba1 * (i**4) + liczba2 * (i**3) + liczba3 * i*i + liczba4 + float(liczba5)
        if suma == 0:
            print(i)
            break
