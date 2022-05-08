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

def verificador(palabra, universo):
    contador = 0
    palabra_valida = ""
    while contador < len(palabra):
        if palabra[contador] in universo:
            palabra_valida += palabra[contador]
        contador += 1
    if palabra_valida == palabra:
        return True
    else:
        return False          


def puntaje(palabra):
    consonantes = "bcdfghjklmnñpqrstvwxyz"
    vocales = "aeiou"
    n = 0
    vocales_totales = 0
    consonantes_totales = 0
    varios_totales = 0
    while n < len(palabra):
        if palabra[n] in vocales:
            vocales_totales += 1
        elif palabra[n] in consonantes:
            consonantes_totales += 1
        else:
            varios_totales += 1
        n += 1  
    puntaje = len(palabra)*10 + vocales_totales*5 + consonantes_totales*3
    return puntaje

# Programa principal

print("Bienvenido al PysCrable")
print()
tamaño = 0

while tamaño < 10 and tamaño <= 35:
    tamaño = int(input("Ingrese el tamaño del universo de letras: "))

universo = generador_universo(tamaño)
print ("Universo:", universo)
palabras = input("Ingrese sus 3 palabras separadas por un guión: ")

contador = 0
primera_palabra = ""
segunda_palabra = ""
tercera_palabra = ""

while palabras[contador] != "-":
    primera_palabra += palabras[contador]
    contador += 1

contador = len(primera_palabra)+1
while palabras[contador] != "-":
    segunda_palabra += palabras[contador]
    contador += 1

contador = len(primera_palabra) + len(segunda_palabra) + 2
while contador < len(palabras):
    tercera_palabra += palabras[contador]
    contador += 1

verificacion1 = verificador(primera_palabra, universo)
verificacion2 = verificador(segunda_palabra, universo)
verificacion3 = verificador(tercera_palabra, universo)
puntaje_p1 = puntaje(primera_palabra)
puntaje_p2 = puntaje(segunda_palabra)
puntaje_p3 = puntaje(tercera_palabra)

if len(primera_palabra) < 3 or len(segunda_palabra) < 3 or len(tercera_palabra) < 3:
    print("Error, las palabras deben tener al menos 3 letras, perdió su intento")

else:
    if verificacion1 == True:
        print (primera_palabra,"se puede generar con",universo)
        print (puntaje_p1)

    if verificacion1 == False:
        puntaje_p1 = 0
        print (primera_palabra,"no se puede generar con",universo)

    if verificacion2 == True:
        print (segunda_palabra,"se puede generar con",universo)
        print (puntaje_p2)

    if verificacion2 == False:
        puntaje_p2 = 0
        print (segunda_palabra,"no se puede generar con",universo)

    if verificacion3 == True:
        print (tercera_palabra,"se puede generar con",universo)
        print (puntaje_p3)

    if verificacion3 == False:
        puntaje_p3 = 0
        print (tercera_palabra," no se puede generar con",universo)

    puntaje_total = puntaje_p1 + puntaje_p2 + puntaje_p3
    print ("Fin del intento, obtuviste un total de",puntaje_total,"puntos.")