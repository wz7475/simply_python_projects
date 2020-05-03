def znajdz_dzielniki(a):
    dzielniki = []
    if liczba4 >= 0:
        for i in range(1,liczba4+1):
            if liczba4 % i == 0:
                dzielniki.append(i)
                dzielniki.append(i*(-1))
    else:
        for i in range(liczba4-1,0):
            if liczba4 % i == 0:
                dzielniki.append(i)
                dzielniki.append(i*(-1))
                dzielniki.append(i*0.5)
                dzielniki.append(i*(-0.5))
    return dzielniki

while True:
    liczba1, liczba2, liczba3, liczba4,  =(input().split(" "))
    liczba1=float(liczba1)
    liczba2=float(liczba2)
    liczba3=float(liczba3)
    liczba4=int(liczba4)

    suma=liczba4

    dzielniki=znajdz_dzielniki(liczba4)

    for i in dzielniki:
        suma = liczba1 * (i**3) + liczba2 * (i**2) + liczba3 * i + liczba4
        if suma == 0:
            print(i)
            break


