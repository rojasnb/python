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

nombre = ""
lista_de_curso = []
while nombre != "-1":
    nombre = input("Ingrese el nombre: ")
    lista_de_curso.append(nombre)

del lista_de_curso[-1]
print (lista_de_curso)
n_final = n_en_nombres(lista_de_curso)
print (n_final)
print (len(n_final))
print (inicial(n_final))
