numeros = []
suma=0
for i in range(5):
    a=int(input("ingrese un valor: "))
    numeros.append(a)
for numero in numeros:
    suma += numero
    promedio=suma/len(numeros)
print("el numero mayor es " , max(numeros))
print("el numero menor es " , min(numeros))
print("la suma es " , suma)
print("el promedio es " , promedio)