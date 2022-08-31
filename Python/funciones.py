# Desarrollar sus propias funciones

def prom(n1,n2,n3):
    prom = round((n1+n2+n3)/3)
    return prom

# Variables del programa principal

nota1 = int(input("Ingrese nota 1: ")) 
nota2 = int(input("Ingrese nota 2: "))
nota3 = int(input("Ingrese nota 3: "))

promedio = prom(nota1,nota2,nota3)

print ("Su promedio es:", promedio)