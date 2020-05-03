from time import sleep
import os

def kalk_zwyk_start():
    os.system('cls')
    print("""
        Wprowadz pierwsza liczbe,  znak dzialania matemtycznego,  i kolejna liczbe.
        Mozesz wprowadzac tyle ile chcesz liczb.
        Kazdy wprowadzony element odziel spacja.
        Dostepne dzialania to:
        + dodoawnie,
        - odjemowanie,
        * mnozenie
        / dzielenie
        % modulo (reszta z dzielniea)""")
    print()

    zbior = input().split(" ")
    liczby = []
    dzialania = []

    if zbior[0] == "-" or zbior[0] == "+":
        for i in range(1, len(zbior), 2):
            zbior[i] = float(zbior[i])
    else:
        for i in range(0, len(zbior), 2):
            zbior[i] = float(zbior[i])

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
    while (ind+1) <= (len(dzialania)):

        if dzialania[ind] == "+":
            suma += liczby[ind+1]
        if dzialania[ind] == "-":
            suma -= liczby[ind + 1]
        if dzialania[ind] == "*":
            suma = suma*liczby[ind+1]
        if dzialania[ind] == "/":
            if liczby[ind+1] == 0:
                print("""Pamietaj cholero,nie dziel przez zero!!!
                Program urochomi sie ponownie za 5s...""")
                i = 5
                while i > 0:
                    sleep(1)
                    print(i)
                    os.system('cls')
                    i -= 1
                os.system('cls')
                kalk_zwyk_start()
            else:
                suma = suma/liczby[ind + 1]
        if dzialania[ind] == "%":
            if liczby[ind+1] == 0:
                print("""Pamietaj cholero,nie dziel przez zero!!!
                Program urochomi sie ponownie za 5s...""")
                i = 5
                while i > 0:
                    sleep(1)
                    print(i)
                    os.system('cls')
                    i -= 1
                os.system('cls')
                kalk_zwyk_start()
            else:
                suma = suma % liczby[ind + 1]


        ind += 1

    print(suma)
    os.system('cls')
    print()

def kalk_zwyk_std():
    os.system('cls')
    print()

    zbior = input().split(" ")
    liczby = []
    dzialania = []

    if zbior[0] == "-" or zbior[0] == "+":
        for i in range(1, len(zbior), 2):
            zbior[i] = float(zbior[i])
    else:
        for i in range(0, len(zbior), 2):
            zbior[i] = float(zbior[i])

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
            suma += liczby[ind + 1]
        if dzialania[ind] == "-":
            suma -= liczby[ind + 1]
        if dzialania[ind] == "*":
            suma = suma * liczby[ind + 1]
        if dzialania[ind] == "/":
            if liczby[ind + 1] == 0:
                print("""Pamietaj cholero,nie dziel przez zero!!!
                Program urochomi sie ponownie za 5s...""")
                i = 5
                while i > 0:
                    sleep(1)
                    print(i)
                    os.system('cls')
                    i -= 1
                os.system('cls')
                kalk_zwyk_start()
            else:
                suma = suma / liczby[ind + 1]
        if dzialania[ind] == "%":
            if liczby[ind + 1] == 0:
                print("""Pamietaj cholero,nie dziel przez zero!!!
                Program urochomi sie ponownie za 5s...""")
                i = 5
                while i > 0:
                    sleep(1)
                    print(i)
                    os.system('cls')
                    i -= 1
                os.system('cls')
                kalk_zwyk_start()
            else:
                suma = suma % liczby[ind + 1]

        ind += 1

    print(suma)
    os.system('cls')
    print()

kalk_zwyk_start()
while True:
    kalk_zwyk_std()
