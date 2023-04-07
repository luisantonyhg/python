conjuntos = {'peru','colombia','argentina','peru','alemania'}
print(conjuntos)
print(type(conjuntos)) #ES UN CONJUNTOS Y NO PUEDEN SER REPETIDOS

conjuntosNumero = {9,2,3,4,5,6,7,8,2,2}
print(conjuntosNumero)

conjuntosTipos = {1,'hola',12.12,True}
print(conjuntosTipos)

conjuntosCreadoPorString = set('hola')
print(conjuntosCreadoPorString)


conjuntoTupla = set(('abc','cbv','as','avd'))
print(conjuntoTupla)
print(type(conjuntoTupla))

numeros = [1,2,3,4,1,2,3,4]
print(type(numeros))
conjuntosNumeroGenerado = set(numeros)
print(conjuntosNumeroGenerado)

# VOLVER A TIPO LISTA

numeroUnincos = list(conjuntosNumeroGenerado)
print(type(numeroUnincos))
print(numeroUnincos)

