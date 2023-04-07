# ---------------------------------
#       DESARROLLO TAREA 1
# ---------------------------------

texto1 = input("Ingresar primer texto: ")
texto2 = input("Ingresar segundo texto: ")

cant = 0

for i in texto1:
    if i in texto2:
        cant = cant +1
else:
    if cant == len(texto1):
        print("Ambos textos contienen los mismos caracteres ")
    else:
        print("No contienen los mismo caracteres")
        
        

# ---------------------------------
#       DESARROLLO TAREA 2
# ---------------------------------
        
textoIngresado = input("Ingrese texto : ")
textoInverso =  " "

for i in range(len(textoIngresado)):
    a = len(textoIngresado) - (i+1)
    textoInverso += f"{textoIngresado[a]}"
print(textoInverso)



# ---------------------------------
#       DESARROLLO TAREA 3
# ---------------------------------

numeroIngresado = int(input("Ingrese numero: "))
if numeroIngresado < 20:
    operacion = 0
    for i in range(1,numeroIngresado+1):
        denominador = 1
        for j in range(1,i+1):
            denominador *= j
        operacion += (1/denominador)
    print(f"El valor de e = {operacion+1}")
else:
    print("El número tiene que ser menor a 20")
    


# ---------------------------------
#       DESARROLLO TAREA 4
# ---------------------------------

i = 0
numeroBase = 50000

while i < 200:
    if numeroBase <= 0:
        print("El número debe ser mayor que cero")
    else:
        cant_divisores = 0
        k = 1
        while (k <= numeroBase):
            if numeroBase % k == 0:
                cant_divisores += 1
            k += 1
        if cant_divisores == 2:
            print(f"El número {numeroBase} es primo")
            i += 1

    numeroBase += 1