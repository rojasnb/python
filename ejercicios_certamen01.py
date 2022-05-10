def dia_de_la_semana (dd,mm,aaaa):
    a= (14-mm)//12
    y = aaaa-a
    m = mm + (12*a) - 2
    d = (dd + y + (y//4) - (y//100) + (y//400) + ((31*m)//12)) % 7
    return d

def dia (d):
    if d == 0:
        return "Domingo"
    if d == 1:
        return "Lunes"
    if d == 2:
        return "Martes"
    if d == 3:
        return "Miércoles"
    if d == 4:
        return "Jueves"
    if d == 5:
        return "Viernes"
    if d == 6:
        return "Sábado"

# programa principal
 
invitados = "16052000,Sofia;29022000,Silvia;01082000,Andrea;28042000,Paula;04102000,Eduardo;26062001,Pedro;11072001,Federico;03112001,Claudia;20052001,Lucas;24061999,Gabriel;04101999,Camila;"
i = 0
invitado = ""

while len(invitados) != 0:
    i = 0
    invitado = ""
    while invitados[i] != ";":
        invitado += invitados[i]
        i += 1
    invitados = invitados [i+1:]
    dia_invitado = int(invitado [:2])
    mes_invitado = int(invitado [2:4])
    año_invitado = int(invitado [4:8])
    dias = dia_de_la_semana(dia_invitado,mes_invitado,año_invitado)
    diasemana = dia(dias)

    if dia(dia_de_la_semana(22,6,1999)) == diasemana:
        print ("Invita a", invitado[9:])
    else:
        print ("No invitar a", invitado[9:], "xdxd")