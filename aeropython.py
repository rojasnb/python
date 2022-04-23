# Constantes (grados)

from msilib import datasizemask


novato = str("novato")
experimentado = str("experimentado")
senior = str("senior")

# Ingreso de datos solicitados
piloto = input("Ingrese su nombre: ")

grado = input("Ingrese su grado: ")  
if grado == novato:
    pass
elif grado == experimentado:
    pass
elif grado == senior:
    pass
else: 
    exit("lo siento, no podemos procesar su solicitud en estos momentos")
        
hrs_vuelo = int(input("Ingrese sus horas de vuelo: "))
if hrs_vuelo <= -1:
    exit("lo siento, no podemos procesar su solicitud en estos momentos")

diasentrevuelos = int(input("Ingrese cantidad de días fuera de su casa entre vuelos: "))
if diasentrevuelos <= -1:
    exit("lo siento, no podemos procesar su solicitud en estos momentos")

# Calculo de sueldo

sueldo_base = int(1000)
sueldo = sueldo_base+(100*hrs_vuelo)
sueldo_total = float(1)
 
# Procesado de datos

if grado == novato:
    if diasentrevuelos >= 5:
        sueldo_total = sueldo+(sueldo*0.12)
    elif diasentrevuelos == 4:
        sueldo_total = sueldo+(sueldo*0.1)
    elif diasentrevuelos == 3:
        sueldo_total = sueldo+(sueldo*0.06)
    elif diasentrevuelos <= 2:
        sueldo_total = sueldo+(sueldo*0.04)
    
if grado == experimentado:
    if diasentrevuelos >= 5:
        sueldo_total = sueldo+(sueldo*0.15)
    elif diasentrevuelos == 4:
        sueldo_total = sueldo+(sueldo*0.12)
    elif diasentrevuelos == 3:
        sueldo_total = sueldo+(sueldo*0.08)
    elif diasentrevuelos <= 2:
        sueldo_total = sueldo+(sueldo*0.06)
    
if grado == senior:
    if diasentrevuelos >= 4:
        sueldo_total = sueldo+(sueldo*0.15)
    elif diasentrevuelos <= 3:
        sueldo_total = sueldo+(sueldo*0.1)
    
# Salida
     
print("Señor", piloto,"su sueldo es de: $", int(sueldo_total))