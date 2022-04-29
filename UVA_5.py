from random import randint
from turtle import Screen, Turtle
import turtle

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
    elif n == 2:
        dia = "Martes"
    elif n == 3:
        dia = "Miércoles"
    elif n == 4:
        dia = "Jueves"
    elif n == 5:
        dia = "Viernes"
    elif n == 6:
        dia = "Sábado"
    elif n == 7:
        dia = "Domingo"
    return dia

def grafico(tortuga, x, y, raciones):
    turtle.pendown()
    turtle.forward(30)  
    turtle.left(90)
    turtle.forward(raciones)
    turtle.left(90)
    turtle.forward(30)
    turtle.forward(raciones)
