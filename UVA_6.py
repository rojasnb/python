# Funciones importadas

from random import randint

# Funciones definidas

def generador_universo(tamaño):
    vocales = "aeiou"
    consonantes = "bcdfghjklmnñpqrstvwxyz"
    porcentaje_vocales = round(tamaño*0.4)
    porcentaje_consonantes = round(tamaño*0.6)
    universo_vocales = ""
    universo_consonantes = ""
    universo = ""

    if tamaño >= 10 and tamaño <= 35:
        while len(universo) < tamaño:
            while len(universo_consonantes) < porcentaje_consonantes:
                random_consonantes = randint(0,len(consonantes)-1)
                universo_consonantes += consonantes[random_consonantes]
            while len(universo_vocales) < porcentaje_vocales:
                random_vocales = randint(0,len(vocales)-1)
                universo_vocales += vocales[random_vocales]
            universo = universo_consonantes + universo_vocales
        return universo
    else:
        vacio = ""
        return vacio

def validar(palabra):
    contador = 0
    guion = "-"
    primera_palabra = ""
    segunda_palabra = ""
    tercera_palabra = ""
    while palabras[contador] != guion:
        primera_palabra += palabras[contador]
        contador += 1
        while palabras[len(primera_palabra)] != guion:
            segunda_palabra += palabras[len(primera_palabra)]
            tercera_palabra += palabras[len(segunda_palabra)] 

    return primera_palabra


# Programa principal

print("Bienvenido al PysCrable")
print()
tamaño = 0

while tamaño < 10:
    tamaño = int(input("Ingrese el tamaño del universo de letras: "))

universo = generador_universo(tamaño)
print ("Universo:", universo)
palabras = input("Ingrese sus 3 palabras separadas por un guión: ")
valido = validar(palabras)
print(valido)