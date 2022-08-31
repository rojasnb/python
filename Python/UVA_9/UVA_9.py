def monto_total_IFE_asignado(sueldo, genero, edad):
    if genero == "F" or edad <= 23 or 55 < edad:
        ife = round((sueldo * 0.45) * 3)
        if ife > 1000000:
            ife = 1000000

        return ife
    
    else:
        ife = round((sueldo * 0.35) * 3)
        if ife > 750000:
            ife = 750000

        return ife

rangos = open("rangos.txt", "r")

resumen = "resumen_{0}_{1}.txt"
edad_inf = 17
for edad in rangos:
    edad = int(edad)
    if edad_inf < edad:
        resumenes = open(resumen.format(edad_inf+1, edad), "w")
        resumenes.close()
        edad_inf = edad
        
resumen_final = open(resumen.format(edad_inf+1, 65), "w")
resumen_final.close()
rangos.close()

postulantes = open("postulantes.txt", "r")
formato = "{0};{1};{2}"

for postulante in postulantes:
    postulantes_strip = postulante.strip()
    postulantes_split = postulantes_strip.split(";")
    edad_postulante = int(postulantes_split[1])
    sueldo_postulante = int(postulantes_split[5])
    nombre_postulante = postulantes_split[3]
    genero_postulante = postulantes_split[2]

    if edad_postulante >= 18 and edad_postulante <= 23:
        resumen_18 = open("resumen_18_23.txt", "w")
        resumen_18.write(formato.format(nombre_postulante, sueldo_postulante, monto_total_IFE_asignado(sueldo_postulante, genero_postulante, edad_postulante)) + "\n")
        resumen_18.close()
        
    elif edad_postulante >= 24 and edad_postulante <= 55:
        resumen_24 = open("resumen_24_55.txt", "w")
        resumen_24.write(formato.format(nombre_postulante,sueldo_postulante, monto_total_IFE_asignado(sueldo_postulante, genero_postulante, edad_postulante)) + "\n")
        resumen_24.close()

    elif edad_postulante >= 56:
        resumen_56 = open ("resumen_56_65.txt", "w")
        resumen_56.write(formato.format(nombre_postulante, sueldo_postulante, monto_total_IFE_asignado(sueldo_postulante, genero_postulante, edad_postulante)) + "\n")
        resumen_56.close()

postulantes.close()