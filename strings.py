# Un string es un texto, dentro de su estructura puede contener cualquier elemento.
# Se utiliza el código ASCII para comparar los valores entre los caracteres
palabra = input("Ingrese palabra: ")
# Imprime el número de caracteres
print(len(palabra))
# Imprime en pantalla el último caracter de la palabra
print(palabra[-1])
print(palabra[len(palabra)-1])
# Imprime en pantalla el primer caracter de la palabra
print(palabra[0])
# Imprime rango de caracteres
print (palabra [:4])
print (palabra[5:])
print (palabra[3:6])
# Imprime todos los caracteres desde el primero al último
n = 0
while n < len(palabra):
    print(palabra[n])
    n += 1 
