numeros=[]
cont=0
while cont < 5:
    num=int(input("ingrese valor: "))
    numeros.append(num)
    cont += 1
invertir = numeros[: :-1]    
print(numeros)
print(invertir)
