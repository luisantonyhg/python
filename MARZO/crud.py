
conjuntosPaises = {'peru','argentina','bolivia'}

tamañosConjuntos = len(conjuntosPaises)

print("HAY UN TOTAL DE ELEMENTOS EN EL CONJUNTO " + str(tamañosConjuntos))

print('peru' in conjuntosPaises)
print('chile' in conjuntosPaises)

# AGREGAR ELEMENTOS AL CONJUNTO

conjuntosPaises.add('chile')

print(conjuntosPaises)

conjuntosPaises.add('chile')
print(conjuntosPaises)

#  ACTUALIZAR

conjuntosPaises.update({'mexico','alemania'})
print(conjuntosPaises)

# ELIMINAR

conjuntosPaises.remove('chile')
print(conjuntosPaises)

#conjuntosPaises.remove('mexicos') #CUANDO NO LO ENCUENTRA DA ERROR
conjuntosPaises.discard('mexicos')
print(conjuntosPaises)

#limpieza general de conjuntos
conjuntosPaises.clear()
print(conjuntosPaises)
print(len(conjuntosPaises))


countries = {"MX", "COL", "ARG", "USA"}
northAm = {"USA", "CANADA"}
centralAm = {"MX", "GT", "BZ"}
southAm = {"COL", "BZ", "ARG"}

new_set = set()
# OTRA MANERA DE UNIR Y ELIMINAR LOS REPETIDOS
new_set = countries | northAm | centralAm | southAm
print(new_set)

#  AL UNIRSE SE ELIMINA LOS REPETIDOS Y SE PONE UNICO
new_set = countries.union(northAm,centralAm,southAm)
print(new_set)


