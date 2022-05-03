"""
frase = input("Ingrese una frase: ")
frase = frase.lower()
if "uwu" in frase or "pana" in frase:
    print ("Generación Z")
elif "bacan" in frase or "brigido" in frase:
    print ("Millenial")
elif "grosso" in frase:
    print("Generación X")
else:
    print("No lo podemos calificar")
"""

consonantes = "bcdfghjklmnñpqrstvwxyz"
vocales = "aeiou"
print()
palabra = input("Ingrese una palabra: ")
palabra = palabra.lower()

n = 0
vocales_totales = 0
consonantes_totales = 0
varios_totales = 0

while n < len(palabra):
    # print(palabra(n))
    if palabra[n] in vocales:
        vocales_totales += 1
    elif palabra[n] in consonantes:
        consonantes_totales += 1
    else:
        varios_totales += 1
    n += 1

print()
print("El total de vocales en su frase es:", vocales_totales, "; El total de consonantes es:", consonantes_totales, "Y el total de caracteres especiales es:", varios_totales)


