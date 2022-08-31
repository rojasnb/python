from random import randint
import threading 
import socket
import time

host = ''
port = 9000
locaddr = (host,port) 

# preguntas y respuestas

pregunta1 = "Robolx se creo en el año 2009"
pregunta2 = "David Baszucki es el dueño de Roblox"
pregunta3 = "Bloxburg solo se puede encontrar en Roblox"
pregunta4 = "El número de amigos máximo que puedes tener en Roblox es de 300"
pregunta5 = "En Roblox Studio puedes crear tus juegos y mundos"
pregunta6 = "Robux es la moneda virtual en Roblox"
pregunta7 = "Minecraft fue lanzado el año 2013"
pregunta8 = "Al final de minecraft debes pelear contra un dragón"
pregunta9 = "El Creeper está inspirado en un sueño del desarrollador"
pregunta10= "En Minecraft es posible volar en modo supervivencia"
preguntas = [pregunta1, pregunta2, pregunta3, pregunta4, pregunta5, pregunta6, pregunta7, pregunta8, pregunta9, pregunta10]

respuesta1 = "f"
respuesta2 = "v"
respuesta3 = "v"
respuesta4 = "f"
respuesta5 = "v"
respuesta6 = "v"
respuesta7 = "f"
respuesta8 = "v"
respuesta9 = "f"
respuesta10= "v"
respuestas = [respuesta1, respuesta2, respuesta3, respuesta4, respuesta5, respuesta6, respuesta7, respuesta8, respuesta9, respuesta10]

n_de_preguntas = 0
respuestas_correctas = 0
limite = 9

# Creción del socket UDP 

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

tello_address = ('192.168.10.1', 8889)

sock.bind(locaddr)

# Funciones definidas

def recv():
    count = 0
    while True: 
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print ('\nExit . . .\n')
            break

def iniciador():
    msg = "command"
    msg = msg.encode(encoding="utf-8") 
    sent = sock.sendto(msg, tello_address)
    msg = "takeoff"
    msg = msg.encode(encoding="utf-8") 
    sent = sock.sendto(msg, tello_address)    

# Creaciń de recvThread 
recvThread = threading.Thread(target=recv)
recvThread.start()

# Iniciador
print ("Bienvenid@ a la carrera del dron!!")
input("Presiona enter para empezar la carrera!")
iniciador()

while n_de_preguntas < 5:
    random = randint(0,limite)
    pregunta = preguntas.pop(random)
    respuesta_correcta = respuestas.pop(random)
    print (pregunta)
    respuesta = input("El enunciado anterior, ¿es verdadero (v) o falso? (f): ")
    respuesta = respuesta.lower()

    if respuesta == respuesta_correcta:
            print ("Correcto! El dron avanza :D")
            respuestas_correctas += 1
            msg = "forward 30"
            # Enviar mensaje
            msg = msg.encode(encoding="utf-8") 
            sent = sock.sendto(msg, tello_address)
            time.sleep(5)

    elif respuesta == 'x':
        print ('Apagado de emregencia! Apagando motores...')
        msg = "emergency"
        msg = msg.encode(encoding="utf-8") 
        sent = sock.sendto(msg, tello_address)
        print ('Motores apagados')
        sock.close()            
        break
    else:
            print ("Respuesta incorrecta! :(")
     
    n_de_preguntas += 1
    limite -= 1

msg = "land"
msg = msg.encode(encoding="utf-8") 
sent = sock.sendto(msg, tello_address)

if respuestas_correctas == 5:
    print ('Llegaste a la meta!! Felicitaciones!!')
    
else:
    print ('Partida terminada! Lo siento, no cruzaste la linea de meta :(')

sock.close()