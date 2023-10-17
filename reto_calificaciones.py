#https://replit.com/@RodrigoOtero1/reto-parcial-2?v=1
puntos=float(input("calificacion en el examen: "))
materias=float(input("inserte las asignaciones completadas: "))
participacion=input("Ingrese si participó (Sí/No) ")
if 0<=puntos<=100  and 5<=materias<=10 and participacion =="Sí":
  print("su calificación es de", puntos,"y está aprobado")
elif 0<=materias<=4 or participacion =="No":
  print("su calificación es de",puntos,"y está reprobado")
else:
  print("algun valor no es valido")
