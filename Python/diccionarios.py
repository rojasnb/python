diccionario = {}
# diccionario = dic()

patas = {"perro":4,"pollo":2}

#para agregar o modificar

patas["araña"] = 8
#patas["araña"] = 10

# Para eliminar 

#del patas["araña"]

print (patas)

for elemento in patas:
    print("El valor asignado a",elemento,"es",patas[elemento])


#palabra: significado

#diccionarios{llave:valor}

from tkinter import N


dic1=dict()
dict2={}

#print(patas["araña"])

#imprimir el valor asociado a la llave "araña"

"""""
patas= {"perro":4,"pollo":2}
#agregar modificar
patas["araña"]=8

patas["araña"]=10
patas={"perro":4,"pollo":2,"araña":10}
print(patas)
del patas["araña"]

print(patas)"""

#para consultar por los datos en un diccioario

#cantidad_patas=patas["perro"]#-->"perro":4-->"perro"-->4
#print(cantidad_patas)
##
####errores en la consulta a valores a diccionarios 
# intentar consultar por el valor 
#nombre_animal=patas[2]
#print(nombre_animal)

#iterar en dicionariorios
#capitales={"argentina":"buenos aires","peru":"lima","bolivia":"la paz","chile":"santiago"}
#capitales["bolivia"]="sucre"
#for sobre un dicionario ¿que valor se imprimiria?
#for elemento in capitales:
  #  print("la capital de",elemento," es" ,capitales[elemento])

#que hacer si queremos 

""""notas={"progra":[55,75,80],"mate":[80,90,75]}

las_notas=notas["progra"]

promedio_progra=sum(notas["progra"])/len(notas["progra"])
print(promedio_progra)
notas_mate=notas["mate"]
promedio_mate1=sum(notas["mate"])/len(notas["mate"])
print(promedio_mate1)
notas_mate=notas["mate"]
promedio_mate2=sum(notas_mate)/len(notas_mate)
print(promedio_mate2)"""

"""encuesta=["talcahuano","talcahuano","arauco","lebu","arauco","concepcion","talcahuano","tome","penco","san pedro de la paz","coronel"]
datos={}
for comuna in encuesta:
    if comuna not in datos:
        datos[comuna]=0
    datos[comuna]+=1

print(datos)"""

encuesta=[["cristian","slayer"],["ailyn","soad"],["cata","metallica"],["edison","slayer"]]
favoritos={}
for nombre_grupo in encuesta:
    if nombre_grupo[1] not in favoritos:
        favoritos[nombre_grupo[1]]=[]
    favoritos[nombre_grupo[1]].append(nombre_grupo[0])

print(favoritos)
