# ---------------------------------
#       DESARROLLO DE MATRIZ
# ---------------------------------


# DECLARAMOS UNA MATRIZ VACIA

matriz = []

# INGRESAMOS LA DIMENSION DE MATRIZ

dimension = int(input("Ingrese la dimension de la matriz cuadrada: "))

# GENERAMOS LA MTRIZ
for i in range(dimension):
    fila = []
    for o in range(dimension):
         if i == o:
             fila += [1]
         else:
             fila += [0]
    else:
        matriz += [fila]

# IMPRIMIMOS LA MATRIZ GENERADA
for i in matriz:
    print(i)
