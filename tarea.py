
# ------------------------------------------------
#                   TAREA N° 1
# ------------------------------------------------

edad = int(input("Ingrese su edad actual : "))

añoActual = 2021

jubilacion = 65

añoNacimiento = añoActual - edad

añoJubilacion = añoNacimiento + jubilacion

# --------------------------------------------
#               MI CAUSAL CHENCHO 
# --------------------------------------------

print ("====== SISTEMA DE JUBILACION ===== ")
print("Año de Nacimiento : ",añoNacimiento )
print("Año de Jubilacion : ", añoJubilacion)





# ------------------------------------------------
#                   TAREA N° 2
# ------------------------------------------------
ventaTotal = int(input("Ingrese el consumo total : "))

igv = 0.18
operacionIgv = ventaTotal * igv
precioVenta = ventaTotal - operacionIgv

print("===== RESTAURANTE EL GORDITO =======")
print("Precio de venta : ", precioVenta)
print("Impuesto (18%) : ", operacionIgv)
print("Valor Total : ", ventaTotal)


