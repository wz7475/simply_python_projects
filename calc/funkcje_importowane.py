

import math
from time import sleep
from os import system


def stop_na_rad(stop):
    wynik=math.radians(stop)
    return wynik

def rad_na_stop(rad):
    wynik=math.degrees(rad)
    return wynik

def logarytmy(log, pod):
    wynik=math.log(log, pod)
    return wynik

def wart_bezw(wart):
    wynik=math.fabs(wart)
    return wynik

def zaogralanie(liczba, cyfry_po):
    wynik = round(liczba, cyfry_po)
    return wynik

