from math import cos, sin, pi, sqrt

#Inicio programa.
print("*** Kiwi ayuda al Coyote ***")
print()
print("Ingrese los datos solicitados:")
print()

#Variables solicitadas.
x_correcaminos=int(input("Coordenada x del Correcaminos: "))
velocidad_inicial=int(input("Velocidad inicial de lanzamiento [kms/h]: "))
angulo_lanzamiento=int(input("Ángulo de lanzamiento, expresado [grados]: "))
x_coyote=int(input("Coordenada x del lanzamiento [Coyote]: "))
y_coyote=int(input("Coordenada y del lanzamiento [Coyote]: "))

#Transformación de unidades de medida.
velocidad_ms= round(velocidad_inicial*10/36, 5)
radianes= round(angulo_lanzamiento*pi/180, 5)
vx= round(velocidad_ms*cos(radianes), 5)
vy= round(velocidad_ms*sin(radianes), 5)

#Calculo de discriminante y tiempo de impacto.
discrim= round(vy**2-(-(4*4.9*y_coyote)), 5)
t_imp=round((-vy-(sqrt(discrim)))/(4.9*2), 5)*-1
t1= round(t_imp-0.1, 5)
t2= round(t_imp-0.2, 5)
t3= round(t_imp-0.3, 5)

#Calculo de coordenadas.
coordenada_x0=round(x_coyote+vx*0, 5)
coordenada_x1=round(x_coyote+vx*0.1, 5)
coordenada_x2=round(x_coyote+vx*0.2, 5)
coordenada_x3=round(x_coyote+vx*0.3, 5)
coordenada_x4=round(x_coyote+vx*t3, 5)
coordenada_x5=round(x_coyote+vx*t2, 5)
coordenada_x6=round(x_coyote+vx*t1, 5)
coordenada_y0=round(y_coyote+vy*0-4.9*0**2, 5)
coordenada_y1=round(y_coyote+vy*0.1-4.9*0.1**2, 5)
coordenada_y2=round(y_coyote+vy*0.2-4.9*0.2**2, 5)
coordenada_y3=round(y_coyote+vy*0.3-4.9*0.3**2, 5)
coordenada_y4=round(y_coyote+vy*t3-4.9*t3**2, 5)
coordenada_y5=round(y_coyote+vy*t2-4.9*t2**2, 5)
coordenada_y6=round(y_coyote+vy*t1-4.9*t1**2, 5)
coordenada_ximp=round(x_coyote+vx*t_imp, 5)

#Salida en pantalla.
print()
print("Valores ajustados")
print()
print("Velocidad: ", velocidad_ms,"[m/s]")
print("Ángulo de lanzamiento: ", radianes,"[radianes]")
print("vx: ", vx,"[m/s]" )
print("vy: ", vy,"[m/s]")
print()
print("Evaluación del lanzamiento:")
print()
print("Tiempo de impacto estimado: ", t_imp)
print("En el tiempo 0 el proyectil se encuentra en: ", coordenada_x0, coordenada_y0)
print("En el tiempo 0.1 el proyectil se encuentra en: ", coordenada_x1, coordenada_y1)
print("En el tiempo 0.2 el proyectil se encuentra en: ", coordenada_x2, coordenada_y2)
print("En el tiempo 0.3 el proyectil se encuentra en: ", coordenada_x3, coordenada_y3)
print("En el tiempo", t3, "el proyectil se encuentra en: ", coordenada_x4, coordenada_y4)
print("En el tiempo", t2, "el proyectil se encuentra en: ", coordenada_x5, coordenada_y5)
print("En el tiempo", t1, "el proyectil se encuentra en: ", coordenada_x6, coordenada_y6)
print("Proyectil impacta en coordenada x: ", coordenada_ximp)
print("Se falló al Correcaminos por: ", round(coordenada_ximp-x_correcaminos, 5) ,"[m]")