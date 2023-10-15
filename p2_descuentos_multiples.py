#https://replit.com/@RodrigoOtero1/descuentos-multiples?v=1
precio=float(input("inserte el costo total: "))
unidades=float(input("inserte la cantidad de articulos: "))
tipo=input("indique si es tipo A, B o C: ")
if tipo =="A":
  total=precio*.9
elif tipo=="B":
  total=precio*.95
elif tipo=="C":
  total=precio*.98

if unidades >=10:
  print("el precio total es de", total*.95)
else:
  print("el precio total es de", total)
