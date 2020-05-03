from os import  system
zbior = [x for x in input().split() if x != ""]
liczby = []
dzialania = []

if zbior[0] == "-" or zbior[0] == "+":
    for i in range(1, len(zbior), 2):
        try:
            zbior[i] = float(zbior[i])
        except ValueError:
            print("Pamiętaj o poprawnym wprowadzeniu działania (odzziel liczby spacją), zobacz instrukcję.")
            # calls the function which loops back code
elif zbior[0]=="m":
    #calls menu function from differnet file
    print("menu")
elif zbior[0] == "+" or str(zbior[0])[0] in "0123456789":
    for i in range(0, len(zbior), 2):
        try:
            zbior[i] = float(zbior[i])
        except ValueError:
            print("Pamiętaj o poprawnym wprowadzeniu działania (odzziel liczby spacją), zobacz instrukcję.")
            # calls the function which loops back code
else:
    print("Pamiętaj o poprawnym wprowadzeniu działania, zobacz instrukcję.")
    # calls the function which loops back code

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
            print("""Pamiętaj cholero, nie dziel przez zero!!!""")
            system('cls')
            # calls the function which loops back code
        else:
            suma = suma/liczby[ind + 1]
    if dzialania[ind] == "%":
        if liczby[ind+1] == 0:
            print("""Pamiętaj cholero, nie dziel przez zero!!!""")
            system('cls')
            #calls the function which loops back code
        else:
            suma = suma % liczby[ind + 1]

    ind += 1

print(suma)
