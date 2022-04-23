cantidad_de_notas = int(input("Indique la cantidad de notas que desea ingresar: "))
contador = int (1)
notas = int()

# Mientras la condición dentro del while es verdadera se ejectuan las instrucciones indentadas.
while contador <= cantidad_de_notas:
    nota = int(input("Ingrese las notas a promediar: "))

    #Instrucciones de acumulación
    notas = notas + nota
    contador = contador + 1  

# Cuando la condición del while es falsa se ejecutan las instrucciones que no están indentadas.

promedio = round(notas/cantidad_de_notas, 0)
print("Su promedio es: ", promedio)
    


