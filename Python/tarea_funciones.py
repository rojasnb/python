from random import randint

def es_cara():
    cara_sello = bool(randint(0,1))
    return cara_sello

def lanzamiento(monedas):
    contador = 1
    contador_cara = 0 
    while contador <= monedas:
        lanzamiento = es_cara()
        if lanzamiento == True:
            contador_cara += 1
        contador += 1
    return contador_cara

def maquina(monedas):
    contador_lanzamientos = 0
    while monedas != 0:
        caras = lanzamiento(monedas)
        contador_lanzamientos += 1
        monedas -= caras
    return contador_lanzamientos

m= 10
print (maquina(m))
