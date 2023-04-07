# APELLIDOS: HUAMANI GONZALES
# NOMBRES: LUIS ANTONY
# ÚLTIMO DIGITO DNI: 2
print('SUMATORIA ASCII')
IngresoNombre = input('Ingrese sus nombres : ')
IngresoApellido = input('Ingrese sus apellidos : ')
sumatoriaNombres = 0
sumatoriaApellido = 0

for inicio in IngresoNombre:
    sumatoriaNombres += ord(inicio)
for inicio in IngresoApellido:
    sumatoriaApellido += ord(inicio)

print('Sumatoria ASCII de nombres:',sumatoriaNombres) 
print('Sumatoria ASCII de apellidos:',sumatoriaApellido)

