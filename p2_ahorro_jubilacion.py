#https://replit.com/@RodrigoOtero1/Plan-de-Ahorro-para-la-Jubilacion?v=1
FV=float(input("inserte la cantidad deseada para la jubilación: "))
r=float(input("inserte la tasa de interés mensual: "))
n=float(input("inserte el número de pagos mensuales en la jubilación: "))
t=float(input("inserte el número de años hasta la jubilación: "))
PMT=(FV*r)/(((1+r)**n)-1)*(1+r)**-t
print("el pago mensual necesario es de", PMT)
