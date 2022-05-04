""""
while contador < len(texto):
    print (texto[contador])
    contador += 1

# No es necesario definir caracter previamente

for caracter in texto:
    print(caracter)
"""


nombre = input("Ingrese su nombre y apellido: ")
contador = 0
nombre_persona = ""
posicion_espacio = nombre.index(" ")
espacio = " "
"""
while nombre[contador] != espacio:
    nombre_persona += nombre[contador]
    contador += 1
print(nombre_persona)
"""
print(nombre[:posicion_espacio])
print(nombre[posicion_espacio+1:])