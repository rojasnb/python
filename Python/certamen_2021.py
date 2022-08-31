

def votos_partido(votos, partido):
    i = 0
    p = ""
    votos += "$"
    votos_por_partido = 0
    while i < len(votos):
        if votos[i] != "$":
            p += votos[i]
        else:
            if  p == partido:
                votos_por_partido += 1 
            p = ""        
        i += 1
    return votos_por_partido

def votos_coalicion(coaliciones):
    i = 0
    p = ""
    coaliciones += ";"
    coalicion = ""
    partidos = ""
    while i < len(coaliciones):
        if coaliciones[i] != ":":
            coalicion += coaliciones[i]

        elif coaliciones[i] != "-":
            partidos += coaliciones[i]
        i += 1
    return coalicion, partidos


# Programa principal

votos = "p3$p31$p4$p3$p1$p6$p4$p5$p310$p6$p8$p8$p4$p4$p2$p3"
coaliciones = "c1:p1-p2-p31-p3;c2:p4-p5;c3:p6-p310-p7"

votos_coalicion(coaliciones)
