rangos = open("rangos.txt", "r")

s = "resumen_{0}_{1}.txt"
edad_min = 18
for edad in rangos:
    edad = int(edad)
    if edad_min < edad:
        open(s.format(edad_min, edad), "w")
        edad_min = edad
open(s.format(edad_min+1, 65), "w") 
rangos.close()