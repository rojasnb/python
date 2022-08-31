# Leer y recorrer un archivo
#archivo = open("nombre_archivo.csv/txt", "r") #read
#for linea in archivo:
#    linea.strip().replace("buscamos", "el que reemplazará al que buscamos")
#    lista_split = linea.strip(split)(",") #linea - factura,123,$345 --> linea - 
#    print (lista_split[0])
#archivo.close() # Esta linea es re importante ctm, asique que no se te olvide uwu

'''
semis_copa_america = ["Brasil", "Argentina", "Perú", "Colombia"]

archivo = open ("semis.txt", "w")
archivo.write("Semifinales Copa América\n")
archivo.write("\n")

for pais in semis_copa_america:
    archivo.write(pais+"\n")
archivo.close()
'''

semis_copa_america2 = [
    ["Brasil", 20],
    ["Perú", 3],
    ["Colombia", 1],
    ["Argentina", 15],
]

archivo = open ("campeones.txt", "w")
archivo.write("No sé que poner pero xD\n")
archivo.write("\n")

#Brasil ha salido campeón 20 veces
s = "{0} ha salido campeón {1} veces\n"
for pais in semis_copa_america2:
    archivo.write(s.format(pais[0],pais[1]))
archivo.close()