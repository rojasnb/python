# Tello Python3 Control Demo 
#
# http://www.ryzerobotics.com/
#
# 1/1/2018

import threading 
import socket
import sys
import time
import platform

from click import command  

host = ''
port = 9000
locaddr = (host,port) 


# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

tello_address = ('192.168.10.1', 8889)

sock.bind(locaddr)

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

def verificador (respueta, respuesta_correcta):
        #respuesta = input("Selecciona una opción: ")
        if respuesta == respuesta_correcta:
            print ("Correcto! El dron avanza :D")
            msg = "takeoff"
            return msg
        else:
            print ("Respuesta incorrecta! :(")
            msg = "land"
            return msg
          

# pregnutas
pregunta1 = ""
pregunta2 = ""
pregunta3 = ""
pregunta4 = ""
pregunta5 = ""
pregunta6 = ""
pregunta7 = ""
pregunta8 = ""
pregunta9 = ""
pregunta10= ""
preguntas = [ pregunta1, pregunta2, pregunta3, pregunta4, pregunta5, pregunta6, pregunta7, pregunta8, pregunta9, pregunta10 ]

# Iniciador
print ("Bienvenidos a la carrera del dron USM!")
input("Presiona enter para empezar la carrera!")
iniciador()


#recvThread create
recvThread = threading.Thread(target=recv)
recvThread.start()

while True: 
    try:
        respuesta = input("a o b: ")
        msg = verificador(respuesta,"a")

        if not msg:
            break  

        if 'end' in msg:
            print ('...')
            sock.close()  
            break

        # Send data
        msg = msg.encode(encoding="utf-8") 
        sent = sock.sendto(msg, tello_address)
    except KeyboardInterrupt:
        print ('\n . . .\n')
        sock.close()  
        break


"""
        python_version = str(platform.python_version())
        version_init_num = int(python_version.partition('.')[0]) 
       # print (version_init_num)
        if version_init_num == 3:
            msg = input("")
"""