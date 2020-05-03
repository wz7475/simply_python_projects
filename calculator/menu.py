import math
from time import sleep
from os import system
from funkcje_importowane import *
from funkcje_pisane import*
from funkcje_trygonometryczne import *

def start():
    print("""
    Witaj w kalkulatorze by wz7475 3.0!
    Wybierz:
    z - aby wybrać zwykły kalkulator,
    n - aby wybrać naukowy,
    w - aby zakończyć program,
    Następnie naciśnij Enter: """)
    wyb=input()
    wyb=wyb.lower()
    if wyb == "z":
        kalk_zwyk_start()
    elif wyb == "n":
        naukowy()
    elif wyb == "w":
        exit()
    else:
        print("Wybrałeś nieistniejącą opcję. Spróbuj ponownie.")
        system('cls')
        start()


def kalk_zwyk_start():
    system('cls')
    print("""
        Wprowadż pierwszą liczbę,  znak działania matemtycznego i kolejną liczbę.
        Możesz wprowadzać tyle, ile chcesz liczb.
        Każdy wprowadzony element odziel spacją.
        Jeśli chcesz wyjść do menu to wpisz 'm' i naciśnij Enter.
        Dostępne działania to:
        + dodoawnie,
        - odjemowanie,
        * mnożenie
        / dzielenie
        % modulo (reszta z dzielenia)""")
    print()

    while True:
        kalk_zwyk_std()


def kalk_zwyk_std():
    system('cls')
    print()

    zbior = input().split(" ")
    liczby = []
    dzialania = []
    try:
        if zbior[0] == "-" or zbior[0] == "+":
            for i in range(1, len(zbior), 2):
                try:
                    zbior[i] = float(zbior[i])
                except ValueError:
                    print("Pamiętaj o poprawnym wprowadzeniu działania (odzziel liczby spacją), zobacz instrukcję.")
                    kalk_zwyk_start()
        elif zbior[0]=="m":
            start()
        elif zbior[0] == "+" or str(zbior[0])[0] in "0123456789":
            for i in range(0, len(zbior), 2):
                try:
                    zbior[i] = float(zbior[i])
                except ValueError:
                    print("Pamiętaj o poprawnym wprowadzeniu działania (odzziel liczby spacją), zobacz instrukcję.")
                    kalk_zwyk_start()
        else:
            print("Pamiętaj o poprawnym wprowadzeniu działania, zobacz instrukcję.")
            kalk_zwyk_start()
    except IndexError:
        print("Pamiętaj o poprawnym wprowadzeniu działania, zobacz instrukcję.")
        kalk_zwyk_start()

    if zbior[0] == "-" or zbior[0] == "+":
        for znak in zbior:
            if zbior.index(znak) % 2 != 0:
                liczby.append(znak)
            else:
                dzialania.append(znak)
    else:
        for znak in zbior:
            if zbior.index(znak) % 2 == 0:
                liczby.append(znak)
            else:
                dzialania.append(znak)

    ind = 0
    suma = liczby[0]
    while (ind + 1) <= (len(dzialania)):
        if dzialania[ind] == "+":
            suma += liczby[ind+1]
        if dzialania[ind] == "-":
            suma -= liczby[ind + 1]
        if dzialania[ind] == "*":
            suma = suma*liczby[ind+1]
        if dzialania[ind] == "/":
            if liczby[ind+1] == 0:
                print("""Pamiętaj cholero, nie dziel przez zero!!!""")
                system('cls')
                kalk_zwyk_start()
            else:
                suma = suma/liczby[ind + 1]
        if dzialania[ind] == "%":
            if liczby[ind+1] == 0:
                print("""Pamiętaj cholero, nie dziel przez zero!!!""")
                system('cls')
                kalk_zwyk_start()
            else:
                suma = suma % liczby[ind + 1]

        ind += 1

    print(suma)
    system('cls')
    print()


def naukowy():
    print("""Wybierz ktorąs z opcji:
    stop liczba - zamiana stopni na radiany;
    rad liczba - zamiana radianów na stopnie;
    log liczba_logarytmowana podstawa - logarytmowanie;
    wart liczba - wartość bezwzględna;
    zag liczba ilość_cyfr_po_przecinku - zaograglanie;
    poteg liczba wykładnik - potęgowanie;
    pierw liczba stopień_pierwiastka - pierwiastkowanie;
    sil liczba - silnia;
    fib nr_wyrazu - wyznaczanie n-tego wyrazu ciagu fibonacciego;
    proc liczba - procent;
    liczb liczba - sprawdzanie czy dana liczba jest liczbą pierwszą;
    wyzn liczba - wyznaczanie n-tej liczby pierwszej;
    ulam liczba - zamiana ułamka dziesiętnego na zwykły;
    nwd - najmniejszy wspólny dzielnik;
    nww - najmniejsza wspólna wielokrotność;
    wsp - wspólne dzielniki dwóch liczb;
    sin rad/stop liczba - sinus;
    asin rad/stop liczba - arcus sinus;
    cos rad/stop liczba - cosinus;
    acos rad/stop liczba - arcus cosinus;
    tg rad/stop liczba - tangens;
    atg rad/stop liczba - arcus tangens;
    menu/m - wyjście do menu głównego.""")

    wybor = input().split(" ")
    if wybor[0].lower() == "menu" or wybor[0].lower() == "m":
        start()
    elif len(wybor) == 0:
        print("Wybrałeś nie istniejacą opcję.")
        naukowy()
    elif len(wybor) == 1:
        print("Wybrałeś nie istniejacą opcję.")
        naukowy()
    elif len(wybor) == 2:
        try:
            wybor[1] = float(wybor[1])
            if wybor[0].lower() == "stop":
                print(stop_na_rad(wybor[1]))
            elif wybor[0].lower() == "rad":
                print(rad_na_stop(wybor[1]))
            elif wybor[0].lower() == "wart":
                print(wart_bezw(wybor[1]))
            elif wybor[0].lower() == "sil":
                print(silnia(wybor[1]))
            elif wybor[0].lower() == "fib":
                print(fibonacci(wybor[1]))
            elif wybor[0].lower() == "proc":
                print(procenty(wybor[1]))
            elif wybor[0].lower() == "liczb":
                print(pierwsze_spr(wybor[1]))
            elif wybor[0].lower() == "wyzn":
                print(wyznacz_l_pierw(wybor[1]))
            elif wybor[0].lower() == "ulam":
                print(zamiana(wybor[1]))
        except ValueError:
            print("Wybrałeś niepoprawny arument do funkcji, spróbuj ponownie.")
            naukowy()
    elif len(wybor) == 3:
        try:
            wybor[2] = float(wybor[2])
            if wybor[0].lower() == "log":
                wybor[1] = float(wybor[1])
                print(logarytmy(wybor[1], wybor[2]))
            elif wybor[0].lower() == "poteg":
                wybor[1] = float(wybor[1])
                print(potegowanie(wybor[1], wybor[2]))
            elif wybor[0].lower() == "pierw":
                wybor[1] = float(wybor[1])
                print(pierwiastkowanie(wybor[1], wybor[2]))
            elif wybor[0].lower() == "sin":
                print(sinus(wybor[1], wybor[2]))
            elif wybor[0].lower() == "asin":
                print(arcus_sinus(wybor[1], wybor[2]))
            elif wybor[0].lower() == "cos":
                print(cosinus(wybor[1], wybor[2]))
            elif wybor[0].lower() == "acos":
                print(arcus_cosinus(wybor[1], wybor[2]))
            elif wybor[0].lower() == "tg":
                print(tangens(wybor[1], wybor[2]))
            elif wybor[0].lower() == "atg":
                print(arcus_tangens(wybor[1], wybor[2]))
            elif wybor[0].lower() == "zag":
                wybor[1] = float(wybor[1])
                print(zaogralanie(wybor[1], wybor[2]))
            elif wybor[0].lower() == "nwd":
                wybor[2]=int(wybor[2])
                wybor[1] = int(wybor[1])
                print(nwd(wybor[1], wybor[2]))
            elif wybor[0].lower() == "nww":
                wybor[2] = int(wybor[2])
                wybor[1] = int(wybor[1])
                print(nww(wybor[1], wybor[2]))
            elif wybor[0].lower() == "wsp":
                wybor[2] = int(wybor[2])
                wybor[1] = int(wybor[1])
                print(wps_dziel(wybor[1], wybor[2]))
        except ValueError:
            print("Wybrałeś niepoprawny arument do funkcji, spróbuj ponownie.")
            naukowy()

    print()
    system('cls')
    naukowy()


start()
