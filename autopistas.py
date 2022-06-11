def mayor_movilidad(lista):
    diccionario = {}
    for patente in lista:
        if patente[0] not in diccionario:
            diccionario[patente[0]] = 0
        diccionario[patente[0]] += 1
 #   diccionario.sort()

    return diccionario

def reportar(lista):
    diccionario = {}
    for patente in lista: #['BBJJ77',2]
        if patente[1] not in diccionario: #patente = [2, 'BBJJ77']
            diccionario[patente[1]] = []
        diccionario[lista[1]].append(patente[0])

    return diccionario    




transitos = [
['BBJJ77',2], ['CCHH19',3], ['AAFF37',3], ['BBJJ77',1],
['AAFF37',1], ['DDKK33',3], ['AAFF37',1], ['AAFF37',2]
]

print (mayor_movilidad(transitos))
print (reportar(transitos))