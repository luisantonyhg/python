"""Tarea 1"""
texto1 = input("Ingresar primer texto: ")
texto2 = input("Ingresar segundo texto: ")

cant = 0
for i in texto1:
    if i in texto2:
        cant += 1
else:
    if cant == len(texto1):
        print("Ambos textos contienen los mismos caracteres")
    else:
        print("NO contienen los mismo caracteres")
        
        

"""Tarea 2"""
texto1 = input("Ingresar texto: ")
text_inverso = ""
for i in range(len(texto1)):
    j = len(texto1) - (i+1)
    text_inverso += f"{texto1[j]}"
print(text_inverso)




"""Tarea3"""
numero = int(input("Ingrese numero: "))
if numero < 20:
    ope = 0
    for i in range(1,numero+1):
        denominador = 1
        for j in range(1,i+1):
            denominador *= j
        ope += (1/denominador)
    print(f"El valor de e = {ope+1}")
else:
    print("El número tiene que ser menor a 20")
    
    

"""Tarea 4"""
i = 0
numero_base = 50000

while i < 200:
    if numero_base <= 0:
        print("El número debe ser mayor que cero")
    else:
        cant_divisores = 0
        k = 1
        while (k <= numero_base):
            if numero_base % k == 0:
                cant_divisores += 1
            k += 1
        if cant_divisores == 2:
            print(f"El número {numero_base} es primo")
            i += 1

    numero_base += 1







