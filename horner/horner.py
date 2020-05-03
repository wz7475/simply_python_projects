def znajdz_dzielniki(a):
    dzielniki = []
    if a >= 0:
        for i in range(1,a+1):
            if a % i == 0:
                dzielniki.append(i)
                dzielniki.append(i*(-1))
    else:
        for i in range(a-1,0):
            if a % i == 0:
                dzielniki.append(i)
                dzielniki.append(i*(-1))
                dzielniki.append(i*0.5)
                dzielniki.append(i*(-0.5))
    return dzielniki


liczby1  =(input().split(" "))
liczby=[]

for i in liczby1:
    i=int(i)
    liczby.append(i)

dzielniki=znajdz_dzielniki(liczby[-1])
suma=0

licznik_dzielnikow=0
licznik_wielomianu=0
indeks_liczb=0
print(dzielniki)
while True:
    suma += dzielniki[licznik_dzielnikow] ** (len(liczby)-licznik_wielomianu-1) * liczby[licznik_wielomianu
        print(dzielniki[licznik_dzielnikow])
        break

    licznik_wielomianu += 1
    indeks_liczb+=1
    if licznik_wielomianu >= len(liczby)-1:
        licznik_dzielnikow+=1
        suma=0
        continue


