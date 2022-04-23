from math import sqrt

mvp = str()
mejor_distancia = 10000
rondas = int(input("Cantidad de rondas: "))
rondas_jugadas = 0

while rondas_jugadas < rondas:
    rondas_jugadas += 1
    print ("Ronda", rondas_jugadas)
    jugador_1 = input("Nombre: ")
    x_jugador1 = int(input("Coordenada x: "))
    y_jugador1 = int(input("Coordenada y: "))
    if x_jugador1 >= -20 and x_jugador1 <= 20 and y_jugador1 >= -20 and y_jugador1 <= 20:
        hipo=x_jugador1**2+y_jugador1**2
        distancia1= sqrt(hipo)
        print (round(distancia1, 4))
    else:
        distancia1 = 1000
        print("Disparo inválido.", jugador_1, "pierde el turno.")
    
    jugador_2 = input("Nombre: ")
    x_jugador2 = int(input("Coordenada x: "))
    y_jugador2 = int(input("Coordenada y: "))
    if x_jugador2 >= -20 and x_jugador2 <= 20 and y_jugador2 >= -20 and y_jugador2 <= 20:
        hipo=x_jugador2**2+y_jugador2**2
        distancia2= sqrt(hipo)
        print (round(distancia2, 4))
    else:
        distancia2 = 1000
        print("Disparo inválido.", jugador_2, "pierde el turno.")
        
    jugador_3 = input("Nombre: ")
    x_jugador3 = int(input("Coordenada x: "))
    y_jugador3 = int(input("Coordenada y: "))
    if x_jugador3 >= -20 and x_jugador3 <= 20 and y_jugador3 >= -20 and y_jugador3 <= 20:
        hipo=x_jugador3**2+y_jugador3**2
        distancia3= sqrt(hipo)
        print (round(distancia3, 4))
    else:
        distancia3 = 1000
        print("Disparo inválido.", jugador_2, "pierde el turno.")

    if distancia1 < distancia2 and distancia1 < distancia3:
        mejor_distronda = distancia1
        mvp_ronda = jugador_1
    elif distancia2 < distancia1 and distancia2 < distancia3:
        mejor_distronda = distancia2
        mvp_ronda = jugador_2
    elif distancia3 < distancia1 and distancia3 < distancia2:
        mejor_distronda = distancia3
        mvp_ronda = jugador_3 
    
    print ("Mejor de la ronda: ",mvp_ronda,"- Distancia: ", round(mejor_distronda, 4))
   
    if mejor_distronda < mejor_distancia:
        mejor_distancia = mejor_distronda
        mvp = mvp_ronda
print ()        
print ("Ganador(a): ", mvp,"- Distancia: ", round(mejor_distancia, 4))