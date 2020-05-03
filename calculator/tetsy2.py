zbior = [x for x in list(input()) if x != " "]
lista=[]

i=0
while i <= len(zbior) or zbior[i] not in "+-*/%":
    lista.append(zbior[i])
    i+=1

"".join(lista)