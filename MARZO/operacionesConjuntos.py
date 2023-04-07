conjuntoA = {'peru','bolivia','mexico'}
conjuntoB = {'peru','alemania','belgica'}

conjuntoC = conjuntoA.union(conjuntoB)
print(conjuntoC)
print(conjuntoA | conjuntoB)

conjuntoD  = conjuntoA.intersection(conjuntoB)
print(conjuntoD)
print(conjuntoA & conjuntoB)

conjuntoE = conjuntoA - conjuntoC
print(conjuntoE)

conjuntoF = conjuntoA.symmetric_difference(conjuntoB)

print(conjuntoF)