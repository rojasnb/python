'''
def n_en_nombres(lista):
    nombres_n_final = []
    for nombre in lista:
        if nombre[-1] == "n":
            nombres_n_final.append(nombre)
    return nombres_n_final

def inicial(lista):
    iniciales = []
    for nombre in lista:
        iniciales.append(nombre[0])
    return iniciales
'''
# Programa principal

nombre = ""
lista_de_curso = []
nombre_n_lista = []
iniciales = []
while nombre != "-1":
    nombre = input("Ingrese el nombre: ")
    lista_de_curso.append(nombre)
    if nombre[-1] == "n":
        nombre_n_lista.append(nombre)
        for nombre in nombre_n_lista:
            iniciales.append(nombre[0])

del lista_de_curso[-1]
print (lista_de_curso)
print (nombre_n_lista)
print ("Cantidad:",len(nombre_n_lista))
print (iniciales)