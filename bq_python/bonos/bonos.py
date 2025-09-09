nombre = input("Ingrese su nombre: ")
horas = int(input("Ingrese el número de horas trabajadas en el mes: "))
jornal = float(input("Ingrese el jornal por hora: "))
sueldo = round(horas * jornal, 2)
descto = round(.08 * sueldo, 2)
neto = round(sueldo - descto, 2)

print(f"Empleado: {nombre}")
print(f"Sueldo: S/. {sueldo}")
print(f"Descuento: S/. {descto}")
print(f"Sueldo neto de {nombre}: ${neto}")

print("Bono S/. 200") if horas > 100 else print("No tiene bono")
