

def raiz (n ):
    return n **(1/2)

print(raiz(4))

print("===============")

# LA SITANXIS DE LAMBDA ES : 
#  lamda lista_parametro : expresion_python

raiz = lambda n : n**(1/2)
print(raiz(4))


A = [ raiz(n) for n in range(1,11)]

print(A)


print("=====================================")
# EL MEJOR USO DE LAMBDA O ANONIMA
#  CALCULAMOS LA FUNCION DE LA RAIZ CUADRA CON FUNCION LAMBDA

B = [ (lambda a : a**(1/2)) (n) for n in range(1,11)]

print(B)


print("========================")


#  ASI CALCULAMOS LA RAIZ CUBICA EN LAMBDA

C = [(lambda x : x**(1/3)) (n) for n in range(1,11)]

print(C)




