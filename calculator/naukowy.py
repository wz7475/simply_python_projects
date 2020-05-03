from funkcje_importowane import *
from funkcje_pisane import*
from funkcje_trygonometryczne import *
import math
from os import system
from time import sleep
while True:
    def naukowy():
        print("""Wybierz ktoras z opcji:
        stop - zamiana stopni na radiany;
        rad - zamiana radianow na stopnie;
        log - logarytmowanie;
        wart - wartosc bezwzgledna;
        zag - zaograglanie;
        poteg - potegowamie;
        pierw - pierwiastkowanie;
        sil - silnia;
        fib - wyznaczanie n-tego wyrazu ciagu fibonacciego;
        proc - procent;
        sin - sinus
        asin - arcus sinus;
        tg - tangens;
        atg - arcus tangens;
        nwd - najmniejszy wspolny dzielnik;
        nww - najmniejsza wspolna wielokrotnosc;
        menu - wyjscie do menu glowniego.""")

        wybor = input("Wybierz dzialanie: ")

        if wybor.lower() == "stop":
            print(stop_na_rad())
        elif wybor.lower() == "rad":
            print(rad_na_stop())
        elif wybor.lower() == "log":
            print(logarytmy())
        elif wybor.lower() == "wart":
            print(wart_bezw())
        elif wybor.lower() == "zag":
            print(zaogralanie())
        elif wybor.lower() == "poteg":
            print(potegowanie())
        elif wybor.lower() == "pierw":
            print(pierwiastkowanie())
        elif wybor.lower() == "sil":
            print(silnia())
        elif wybor.lower() == "fib":
            print(fibonacci())
        elif wybor.lower() == "proc":
            print(procenty())
        elif wybor.lower() == "sin":
            print(silnia())
        elif wybor.lower() == "asin":
            print(arcus_sinus())
        elif wybor.lower() == "cos":
            print(cosinus())
        elif wybor.lower() == "acos":
            print(arcus_cosinus())
        elif wybor.lower() == "tg":
            print(tangens())
        elif wybor.lower() == "atg":
            print(arcus_tangens())
        elif wybor.lower() == "menu":
            print("menu so far")
        else:
            print("Wybrales nie istniejaca opcje.")
            system('cls')
            naukowy()
    print()
    system('cls')
    naukowy()