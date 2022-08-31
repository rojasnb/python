horas = 1
minutos = 0

while horas <= 23:
    while minutos <= 59:
        if minutos < 10 and horas < 10:
            print ("0",horas,":","0",minutos)
        elif horas < 10:
            print ("0",horas, ":",minutos)
        minutos += 1
    horas += 1
    minutos = 0
print ("Hemos terminado.")

# Sin terminar