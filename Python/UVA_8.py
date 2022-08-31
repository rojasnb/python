def comunas_con_mas_oferta(lista, operacion):
    nueva_lista = []
    operacion = input("Seleccione la operación que desea realizar (A = Arriendo ; V = Venta): ")
    if operacion == "A" or operacion == "a":
        for comunas in lista: # [id, tipo, operación, comuna, dormitorios, baños, estacionamientos, m2, piscina, gimnasio, precio]
            if comunas[3] not in nueva_lista:
                comunas[3] = 0
            comunas[3] += 1
                









oferta = [['B6396', 'C', 'V', 'Providencia', 4, 3, 1, 63, True, False, 140513611],
['B2003', 'C', 'A', 'Ñuñoa', 4, 1, 2, 72, False, False, 122655402], ['B4510', 'D','V','Valparaíso',
3,3,1,53,True,False,137661254],['A6803','D','A','Providencia', 4, 1, 0, 80, False, False, 151368062], ['A9442', 'D', 'A', 'Ñuñoa',3,
1,0,114,True,False, 148007915], ['C4297', 'D', 'V', 'Ñuñoa', 2, 3, 2, 74,True, True, 201075569], ['B1017', 'C', 'V', 'Valparaíso', 3, 3, 2, 60, True, False,
224580934], ['C6171', 'D', 'A', 'Valparaíso', 1, 3, 2, 63, True, False, 192273786],['A1721', 'D', 'V', 'Ñuñoa', 2, 3, 2, 112, False, 
False, 118911622], ['B5197', 'C','A','Ñuñoa',2,2,1,82,True,False,195287817],['B4913','D','V','Concepción',4,2, 2, 73, False, True, 186961907], 
['A5610', 'D', 'A', 'Viña del mar', 1, 2, 2, 115, False, True, 210702365], ['C7718', 'D', 'A', 'Concepción', 1, 1,
2, 112, False, True, 189009541], ['B9228', 'D', 'A', 'San Joaquín', 2, 3, 2, 110, True,False,248914620],['A8676','C','V','Ñuñoa',
2,1,1, 62, False, False,165369148],['A2990','D','A','Viña del Mar', 3,2,1,97,True,False,248708274],['A3150','C','V','San Joaquín', 3,
1,1,79,False,False,202722466],['B4236','C','A','San Joaquín',1,1,1,104,False,False,153363382],['B5625','C','V','Providencia',3,
1,1,109,False,False,86181180],['C8119','D','A','Ñuñoa',1,3,0,60,False,True,235617495],['A7013', 'C', 'V', 'Viña del Mar', 2, 3, 0, 120, 
True, False, 146430526], ['A2983','D', 'V', 'Ñuñoa', 2, 2, 1, 80, True, False, 195192915], ['B2691', 'D', 'V', 'Viña del Mar', 2, 2, 2, 80, False, False, 109713495],
['C2187', 'D', 'V', 'Ñuñoa', 1, 2,2, 77, False, True, 195733294], ['C4132', 'C', 'A', 'Ñuñoa', 1, 2, 1, 119, False,False, 67104298]]        
