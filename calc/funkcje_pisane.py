from time import sleep
from os import system
import math


def potegowanie(pod, wyk):
    wynik = pod ** wyk
    return wynik


def pierwiastkowanie(pod, wyk):
    wynik = pod ** (1/wyk)
    return wynik


def silnia(s):
    suma = 1
    if s <= 100000 and s > 0:
        suma = 1
        while s > 0:
            suma *= s
            s -= 1
    else:
        print("Podales niewlasiwa wartosc. Maks to 100 000, a min to 1. Sprobuj ponownie za 5s.")
        i = 5
        while i > 0:
            sleep(1)
            print(i)
            system('cls')
            i -= 1
        system('cls')
        silnia()
    return suma


def fibonacci(f):
    f = int(f)
    lista = list(range(100000))
    if f <= 100000 and f > 0:
        fib = lista[0:f]
        fib[0] = 1
        fib[1] = 1

        i = 2
        while i < f:
            fib[i] = fib[i-1]+fib[i-2]
            i = i+1

        return fib[f-1]
    else:
        print("Podales niwlaciwa wartosc. Maks to 100 000, a min to 1. Sprobuj ponownie za 5s.")
        i = 5
        while i > 0:
            sleep(1)
            print(i)
            system('cls')
            i -= 1
        system('cls')
        fibonacci()


def procenty(pro):
    wynik = pro / 100
    return wynik


def pierwsze_spr(x):

    licznik = 0
    if x < 2:
        return False
    else:
        for i in range(1, int(x)+1):
            if x % i == 0:
                licznik += 1
    if licznik == 2:
        return True
    else:
        return False


def wyznacz_l_pierw(y):
    if y < 1:
        print("Podales niwlaciwa wartosc. Min to 1. Sprobuj ponownie za 5s.")
        i = 5
        while i > 0:
            sleep(1)
            print(i)
            system('cls')
            i -= 1
        system('cls')
        wyznacz_l_pierw()
    plist = []
    x = 2
    while len(plist) < y:
        if pierwsze_spr(x):
            plist.append(x)
        x += 1
    return plist[-1]


def wps_dziel(a, b):
    dziel_a = []
    dziel_b = []
    dziel_wps = []
    for i in range(1, a+1):
        if a % i == 0:
            dziel_a.append(i)
    for i in range(1, b+1):
        if b % i == 0:
            dziel_b.append(i)
    for i in dziel_a:
        if i in dziel_b:
            dziel_wps.append(i)
    return dziel_wps


def zamiana(x):
    przed = len(str(math.floor(x)))
    dziesiet = str(x)[przed+1:]
    licznik = dziesiet
    licznik = int(licznik)
    mianownik = 10 ** len(str(x)[przed + 1:])
    dzielniki = wps_dziel(licznik, mianownik)
    licznik = str(int(licznik/dzielniki[-1]))
    mianownik = str(int(mianownik/dzielniki[-1]))
    przed_przec = str(x)[0:przed]
    if str(x)[0] == 0:
        wynik = licznik + "/" + mianownik
    else:
        wynik = przed_przec + " " + licznik + "/" + mianownik
    return wynik


def nwd(a, b):
    dziel_a = []
    dziel_b = []
    dziel_wps = []
    for i in range(1, a+1):
        if a % i == 0:
            dziel_a.append(i)
    for i in range(1, b+1):
        if b % i == 0:
            dziel_b.append(i)
    for i in dziel_a:
        if i in dziel_b:
            dziel_wps.append(i)
    return dziel_wps[-1]


def nww(a, b):
    czesc1 = a*b
    czesc2 = nwd(a, b)
    return czesc1 / czesc2
