def pares_e_impares(numeros):
    contador = 0
    pares = 0
    impares = 0
    lista = []
    while contador < len(numeros):
        if numeros[contador]%2 == 0:
            pares += 1
            contador += 1
        else:
            impares += 1
            contador += 1
    lista.append(pares)
    lista.append(impares)
    return lista
    

'''
def par_o_impar(lista):
    pares = 0
    impares = 0
    for numero in lista:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
'''

cantidad = int (input("Ingrese cantidad de números: "))
numeros = []
# numeros = list() / otra forma de crear una lista vacia
contador = 0
while contador < cantidad:
    numero = int(input("Ingrese número: "))
    numeros.append(numero)
    contador += 1

numeros.sort()
numeros.reverse()
pares = pares_e_impares(numeros)
print (pares)


