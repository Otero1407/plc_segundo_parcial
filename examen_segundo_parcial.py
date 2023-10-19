temp=float(input("inserte la temperatura del ambiente en grados C: "))

if temp<20:
  print("LLevarla dentro de la casa")

elif 25>=temp>=20:
  print("Buenas condiciones")

elif temp>25:
  print("Llevarla dentro de casa y encender ventilador")
  
hum=float(input("inserte el porcentaje de humedad en el aire: "))

riego=(input("inserte que día de la semana es: "))

if riego =="martes" or riego =="jueves" or riego =="sábado" and hum<20:
  print("Regar a Rubí")

elif riego =="martes" or riego =="jueves" or riego =="sábado" and 22>=hum>=20:
  print("humedad adecuada")
  
elif riego=="lunes" or riego=="miércoles" or riego=="viernes" or riego=="domingo" and hum>22:
  print("No es necesario regar a Rubí")
