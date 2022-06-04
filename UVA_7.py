def clasificar(lista_tiempos, clasificados):
    pilotos = 0
    while pilotos < len(lista_tiempos):
        lista_tiempos[pilotos].reverse()
        pilotos += 1

    lista_tiempos.sort()
    pilotos_clasificados = []
    pilotos_no_clasificados = []
    lista = []

    pilotos = 0

    while pilotos < clasificados:
        pilotos_clasificados.append(lista_tiempos[pilotos])
        pilotos += 1
    
    while pilotos < len(lista_tiempos):
        pilotos_no_clasificados.append(lista_tiempos[pilotos])
        pilotos += 1

    lista.append([pilotos_clasificados])
    lista.append([pilotos_no_clasificados])

    return lista


lista_tiempos = [['p5', 93526], ['p5', 91019], ['p8', 90207], ['p5', 94878], ['p6', 92827], ['p3', 93335], ['p4', 92681], ['p4', 90805],
['p10', 90825], ['p3', 90343], ['p5', 91890], ['p6', 90781], ['p3', 93618], ['p3', 91794]]

print (clasificar(lista_tiempos, 2))