amigos=int(input("¿Cuantos amigos se reuniran a comer sushi?: "))
rolls=int(input("¿Cuantos rolls van a ordenar?: "))
piezas=int(input("¿Cuantas piezas de sushi trae cada roll?: "))

#Desarrollo

print("Para", amigos, "amigos, a cada amigo le corresponden", piezas*rolls//amigos, "piezas de sushi.")