import math
from time import sleep
from os import system
from funkcje_importowane import rad_na_stop
import math

def zamiana_na_stopnie(stop):
    wynik=math.radians(stop)
    return wynik

def sinus(wybor, sin):
    if wybor.lower() == "rad":
        wynik=math.sin(sin)
    elif wybor.lower() == "stop":
        sin=zamiana_na_stopnie(sin)
        wynik = math.sin(sin)
    else:
        print("Wybrales nieistniejaca opcje. Sproboj ponownie za 5s.")
        i = 5
        while i > 0:
            sleep(1)
            print(i)
            system('cls')
            i -= 1
        system('cls')
        sinus()
    return wynik

def arcus_sinus(wybor, sin):
    if wybor.lower() == "rad":
        wynik=math.asin(sin)
    elif wybor.lower() == "stop":
        sin = zamiana_na_stopnie(sin)
        wynik = math.asin(sin)
    else:
        print("Wybrales nieistniejaca opcje. Sproboj ponownie")
        i = 5
        while i > 0:
            sleep(1)
            print(i)
            system('cls')
            i -= 1
        system('cls')
        arcus_sinus()
    return  wynik

def cosinus(wybor, sin):
    if wybor.lower() == "rad":
        wynik=math.cos(sin)
    elif wybor.lower() == "stop":
        sin = zamiana_na_stopnie(sin)
        wynik = math.cos(sin)
    else:
        print("Wybrales nieistniejaca opcje. Sproboj ponownie")
        i = 5
        while i > 0:
            sleep(1)
            print(i)
            system('cls')
            i -= 1
        system('cls')
        cosinus()
    return  wynik

def arcus_cosinus(wybor, sin):
    if wybor.lower() == "rad":
        wynik=math.acos(sin)
    elif wybor.lower() == "stop":
        sin = zamiana_na_stopnie(sin)
        wynik = math.acos(sin)
    else:
        print("Wybrales nieistniejaca opcje. Sproboj ponownie za 5s.")
        i = 5
        while i > 0:
            sleep(1)
            print(i)
            system('cls')
            i -= 1
        system('cls')
        cosinus()
    return  wynik

def tangens(wybor, sin):
    if wybor.lower() == "rad":
        wynik=math.tan(sin)
    elif wybor.lower() == "stop":
        if sin == 90:
            print("Tg z 90 stopni nie istnieje. Sproboj ponownie.")
            i = 5
            while i > 0:
                sleep(1)
                print(i)
                system('cls')
                i -= 1
            system('cls')
            cosinus()
        sin = zamiana_na_stopnie(sin)
        wynik = math.tan((sin))
    else:
        print("Wybrales nieistniejaca opcje. Sproboj ponownie")
        i = 5
        while i > 0:
            sleep(1)
            print(i)
            system('cls')
            i -= 1
        system('cls')
        cosinus()
    return  wynik

def arcus_tangens(wybor, sin):
    if wybor.lower() == "rad":
        wynik=math.atan(sin)
    elif wybor.lower() == "stop":
        if sin == 0:
            print("Ctg z 0 stopni nie istnieje. Sproboj ponownie.")
            i = 5
            while i > 0:
                sleep(1)
                print(i)
                system('cls')
                i -= 1
            system('cls')
            cosinus()
        sin = zamiana_na_stopnie(sin)
        wynik = math.atan((sin))
    else:
        print("Wybrales nieistniejaca opcje. Sproboj ponownie")
        i = 5
        while i > 0:
            sleep(1)
            print(i)
            system('cls')
            i -= 1
        system('cls')
        cosinus()
    return  wynik

