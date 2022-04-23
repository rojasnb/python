from random import randint

entrada_0 = int()
entrada_1 = int()
entrada_2 = int()
entrada_3 = int()
total_2_dias = int()
recargo_estacionamiento = int()
recargo = int()

# Inicio del programa

print("Bienvenido a LolaPYlooza")
print("------- Sistema de cotización de entradas -------")
print()

# Entradas según cantidad de días

cantidad_de_dias = int(input("Cantidad de días: "))
if cantidad_de_dias == 1:
    dia1 = str(input("Día que desea asistir: "))
    if dia1 == "Viernes":
        entrada_0 = int(50000)
    elif dia1 == "Sábado":
        entrada_0 = int(75000)
    elif dia1 == "Domingo":
        entrada_0 = int(60000)
    print ("Día 1:", dia1, "valor: $", entrada_0)

if cantidad_de_dias == 2:
    dia1 = str(input("Día 1 que desea asistir: "))
    dia2 = str(input("Día 2 que desea asistir: "))
    
    if dia1 == "Viernes":
        entrada_1 = int(50000)
    elif dia1 == "Sábado":
        entrada_1 = int(75000)
    elif dia1 == "Domingo":
        entrada_1 = int(60000)    
    
    if dia2 == "Viernes":
        entrada_2 = int(50000)
    elif dia2 == "Sábado":
        entrada_2 = int(75000)
    elif dia2 == "Domingo":
        entrada_2 = int(60000)

    descuento_2d = int((entrada_1+entrada_2)*0.2)
    total_2_dias = (entrada_1+entrada_2)-descuento_2d

    print ("Día 1:", dia1, "valor: $", entrada_1)
    print ("Día 2:", dia2, "valor: $", entrada_2)
    print ("Descuento por días:", descuento_2d)

if cantidad_de_dias == 3:
    entrada_3 = int(150000)
    print("Total a pagar por todos los días: $", entrada_3)

# Entradas VIP

vip = int(input("Ingrese 1 si desea entrada VIP: "))

if vip == 1 and cantidad_de_dias == 1:
    recargo = int(entrada_0*0.4)
    print ("Recargo por entrada VIP: $", recargo)

elif vip == 1 and cantidad_de_dias == 2:
    recargo = int(total_2_dias*0.4)
    print ("Recargo por entrada VIP: $", recargo)

elif vip == 1 and cantidad_de_dias == 3:
    recargo = int(entrada_3*0.4)
    print ("Recargo por entrada VIP: $", recargo)

# Estacionamiento

else:
    estacionamiento = int(input("Ingrese 1 si desea estacionamiento: "))
    if estacionamiento == 1:
        recargo_estacionamiento = int(10000*cantidad_de_dias)
        print("Recargo por estacionamiento: $", recargo_estacionamiento)
    else:
        print("Sin estacionemiento.")

# Esto lo dejo aqui para que python use los valores ingresados por el usuario 

total_sin_descuento = entrada_0+total_2_dias+entrada_3+recargo+recargo_estacionamiento

# Salidas 

banco_py = int(input("Ingrese 1 si tiene tarjeta Banco Pythonia: "))
if banco_py == 1:
    descuento_banco = int(total_sin_descuento*0.3)
    print("Descuento por cliente Bco Pythonia: $", descuento_banco)
    print("Total a pagar: $", total_sin_descuento-descuento_banco)
else:
    random = randint(0,10)
    descuento_random = int(total_sin_descuento*(random/100))
    print("Descuento por sorteo: ", random,"% equivalente a $", descuento_random)
    print("Total a pagar: $", total_sin_descuento-descuento_random)