#Solicitar 20 valores enteros y almacenarlos en la lista y calcular y mostrar:
#la cantidad de números pares, la cantidad de numero impares, la cantidad de ceros,
#el promedio de números positivos, el promedio de números negativos, y el promedio
#de los 20 numeros

lista=[]

i=1

for i in range(1,21):

    num=int(input("introduce el numero en la posicion " + str(i) + ", debe ser entero:"))

    lista=[num]
    i+=1

print("que posicion de numero quieres que te muestre: ")
