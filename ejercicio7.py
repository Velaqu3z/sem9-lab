numeros = []
n=int(input("ingrese limite: "))
for i in range(n):
    num=int(input("ingrese un valor: "))
    numeros.append(num)
    suma=0
    contador=0
while contador < n:
    suma += numeros[contador]
    contador+=1
    promedio=suma/len(numeros)
print("el numero mayor es " , max(numeros))
print("el numero menor es " , min(numeros))
print("la suma es " , suma)
print("el promedio es " , promedio)