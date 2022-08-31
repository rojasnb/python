ventas = int()
suma = int()
mayor_venta = int()
venta = int()

while venta != -1:
    venta = int(input("Ingrese 1 para nueva venta o -1 para terminar las ventas del día: "))
    if venta == 1:
        ventas = int(input("Ingrese total de la venta: "))
    suma = suma + ventas
    if mayor_venta < ventas:
        mayor_venta = ventas


print ("La recaudación del día: $", suma , "Y su mayor venta fue de: $", mayor_venta)