ingreso = float(input("Introduce el ingreso anual: "))

if ingreso < 85528:
	impuesto = ingreso * 0.18 - 556.02
  
else:
    impuesto = 14839.02 + (0.32 * (ingreso - 85528))

if ingreso < 0:
    impuesto = 0.0

impuesto = round(impuesto, 0)
print("El impuesto es:", impuesto, "pesos")
