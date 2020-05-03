from time import sleep
import os


print("""Witaj w kalkuklatorze wz7475 2.0!
    Wprowadz pierwsza liczbe,  znak dzialania matemtycznego,  i kolejna liczbe.
    Mozesz wprowadzac tyle ile chcesz liczb, jesli chcesz zakonczyc wprowadz znak '='.
    Po kazdym wprowadzonym elemencie nacisnij Enter.""")
print()

while True:

    def kalk_zwyk():
        os.system('cls')
        print("""Witaj w kalkuklatorze wz7475 3.0!
            Wprowadz pierwsza liczbe,  znak dzialania matemtycznego,  i kolejna liczbe.
            Mozesz wprowadzac tyle ile chcesz liczb, jesli chcesz zakonczyc wprowadz znak '='.
            Po kazdym wprowadzonym elemencie nacisnij Enter.""")
        print()

    liczby = []
    dzialania=[]

    while not("=" in dzialania):
        i = 0
        i = i + 1
        str(i)
        liczba=float(input('liczba: '))
        liczby.append(liczba)
        dzialanie=input()
        dzialania.append(dzialanie)



    ind=0
    suma=liczby[0]
    while (ind+1) <= (len(dzialania)-1):

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
                kalk_zwyk()
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
                kalk_zwyk()
            else:
                suma = suma % liczby[ind + 1]


        ind += 1


    print(suma)
    os.system('cls')
    print()
