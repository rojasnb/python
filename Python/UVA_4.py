from math import sqrt
from random import randint

print ()
print ("Bienvenid@s a GimnasIWI!")
print ()
meta = int(input("Ingrese meta en calorias: "))
print()
cal_total = int()
cal_plancha = 0
fact_n = 1
n = 0

while cal_total < meta:

    print ("Seleccione una opción:")
    print ()
    print (" (1)  Sentadilla Sumo")
    print (" (2)  Plancha abdominal")
    print (" (3)  Press Francés")
    print (" (4)  Me cansé")
    print ()
    
    ejercicio = int(input("Ingrese el ejercicio: "))
    print ()

    if ejercicio == 1:
        print ("SENTADILLAS SUMO")
        print ()
        repeticiones = int(input("¿Cuántas repeticioines?: "))
        print ()
        cal_sent = round(randint(3,7)*repeticiones)
        cal_total += cal_sent
        print ("Calorias quemadas con sentadillas: ", cal_sent)
        print ("Calorias hasta el momento: ", cal_total)

    elif ejercicio == 2:
        print ("PLANCHA ABDOMINAL")
        print ()
        segundos = int(input("¿Cuántos segundos?: "))
        while n <= segundos:
            n += 1
            fact_n = fact_n*n
            cal_plancha += 4**n/fact_n
        cal_plancha = round(cal_plancha)
        cal_total += cal_plancha
        print ()
        print ("Calorias quemadas con plancha abdominal: ", cal_plancha)
        print ("Calorias hasta el momento: ", cal_total)

    elif ejercicio == 3:
        print ("PRESS FRANCÉS")
        print ()
        repeticiones = int(input("¿Cuántas repeticiones?: "))
        kg = int(input("¿Cuántos kilos?: "))
        if repeticiones < kg:
            menor = repeticiones
            mayor = kg
        elif kg < repeticiones:
            menor = kg
            mayor = repeticiones
        else:
            mayor = kg
            menor = repeticiones

        cal_press = mayor
        cal_press_t = mayor

        while n < (menor-1):
            n += 1
            cal_press = 1 + sqrt(cal_press)
            cal_press_t += cal_press
        cal_press_t = round(cal_press_t)
        cal_total += cal_press_t
        print ()
        print ("Calorias quemadas con Press Francés: ", cal_press_t)
        print ("Calorias hasta el momento: ", cal_total)

    elif ejercicio == 4:
        print ("A descansar! Quemaste", cal_total, "calorias.")
        print ()
        break

    else:
        print ("Ingrese una opción válida!!!")
        print ()

    print()

if ejercicio != 4:
    print ("Meta cumplida! Quemaste", cal_total, "de un total de", meta, "calorias.")
    print ()