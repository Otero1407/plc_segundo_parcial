#https://replit.com/@RodrigoOtero1/Conversion-de-Unidades-de-Medida?v=1
tipo=input("inserte el tipo de unidad a convertir(metros, grados, litros: ")
valor=float(input("inserte el valor a convertir"))
if tipo == "metros":
  print(valor,"metros son", valor*3.28084,"pies")

if tipo=="grados":
  print(valor,"grados son", valor+273.15,"kelvin")
  
if tipo=="litros":
  print(valor,"litros son", valor*3.78541,"galones")
