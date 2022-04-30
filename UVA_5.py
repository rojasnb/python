#   Funciones importadas

from random import randint
from turtle import Turtle, Screen

#   Funciones

def estimacion(t,p,estacion):
    if p < 0.5 and estacion == "verano":
        raciones = round(3*t+20*(1-p))
    elif p >= 0.5 and estacion == "verano":
        raciones = round(2*t+20*(1-p))
    elif p < 0.5 and estacion == "otoño":
        raciones = round(2*t+15*(1-p))
    elif p >= 0.5 and estacion == "otoño":
        raciones = round(t+10*(1-p))
    elif p < 0.5 and estacion == "invierno":
        raciones = round(0.5*t+5*(1-p))
    elif p >= 0.5 and estacion == "invierno":
        raciones = round(0.5*t)
    elif p < 0.5 and estacion == "primavera":
        raciones = round(t+15*(1-p))
    elif p >= 0.5 and estacion == "primavera":
        raciones = round(t+10*(1-p))
    return raciones

def promocion(estacion,raciones):
    if estacion == "verano":
        regaladas = randint(1,11)
    elif estacion == "verano":
        regaladas = randint(1,raciones/10)
    elif estacion == "otoño":
        regaladas = randint(1,2)
    elif estacion == "otoño":
        regaladas = randint(1,raciones/8)
    elif estacion == "primavera":
        regaladas = randint(1,2)
    elif estacion == "primavera":
        regaladas = randint(1,raciones/7)
    elif estacion == "invierno":
        regaladas = randint(1,1)
    elif estacion == "invierno":
        regaladas = randint(1,raciones/5)
    return regaladas

def dia(n):
    if n == 1:
        dia = "Lunes"
        return dia
    elif n == 2:
        dia = "Martes"
        return dia
    elif n == 3:
        dia = "Miércoles"
        return dia
    elif n == 4:
        dia = "Jueves"
        return dia
    elif n == 5:
        dia = "Viernes"
        return dia
    elif n == 6:
        dia = "Sábado"
        return dia
    elif n == 7:
        dia = "Domingo"
        return dia

def grafico(t, x, y, raciones):
    t.speed(99999)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.forward(60)
    t.left(90)
    t.forward(raciones*3)
    t.left(90)
    t.forward(40)
    t.write(raciones)
    t.forward(20)
    t.left(90)
    t.forward(raciones*3)
    t.left(90)

def leyenda(t, x, y, texto):
    t.speed(99999)
    t.penup()
    t.goto(x, y-15)
    t.pendown()
    t.write(texto)

#   Programa principal

pantalla = Screen()
tortuga = Turtle()
tortuga.screen.title("*** El Kiwi del Mote con Huesillos ***")
n = 1
x = 0

print()
print("*** El Kiwi del Mote con Huesillos ***")
print()
print()
estacion = input("Estación: ")
print()

while n <= 7:
    n_dia = dia(n)
    y = 0
    print ("Día", n)
    temp = int(input("Pronóstico de temperatura: "))
    lluvia = float(input("Probabilidad de lluvia: "))
    porciones = estimacion(temp, lluvia, estacion)
    promo = promocion(estacion, porciones)
    print()
    print("Se producirán", porciones, "raciones; Se regalarán", promo ,"raciones para promoción.")
    print()
    grafico(tortuga, x, y, porciones)
    grafico(tortuga, x, y, promo)
    leyenda(tortuga, x, y, n_dia)
    x += 60
    n += 1
  
pantalla.exitonclick()