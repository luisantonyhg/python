# ---------------------------------
#       DESARROLLO DE PARTICIPACION
# ---------------------------------

lista=[]
notaSubida=int(input("Ingrese la nota del alumno: "))

while True:
    if notaSubida != 0:
        lista.append(notaSubida)
        notaSubida=int(input("Ingrese la nota del alumno: "))
        if notaSubida > 20:
            print("La nota ingresada es incorrecta")
            nonotaSubidata=int(input("Ingrese la nota del alumno: "))
    elif notaSubida == 0:
        break    
        

for i in lista:
    print (i)
    
aprobados =  0   
desaprobados = 0

for e in lista:
    if e >= 14:
        aprobados += 1
    else:
        desaprobados += 1
        
    
print ("Calificacion maxima     : ", max(lista))
print ("Calificacion minima     : ", min(lista))
print ("Promedio                : ", sum(lista)/len(lista))
print ("Cantidad de aprobados   : ", aprobados)
print ("Cantidad de desaprobados: ", desaprobados)
