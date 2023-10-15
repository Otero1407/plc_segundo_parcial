#https://replit.com/@RodrigoOtero1/Calculadora-de-Calorias-Quemadas?v=1
peso=float(input("ingrese su peso: "))
actividad=(input("ingrese la actividad (correr, bici o nadar): "))
duracion=float(input("inserte la duracion en minutos: "))
if actividad =="correr":
  calorias=(peso*8)*(duracion/60)
elif actividad =="bici":
  calorias=(peso*10)*(duracion/60)
elif actividad =="nadar":
  calorias=(peso*12)*(duracion/60)
print("las kcal quemadas son de:", calorias)
