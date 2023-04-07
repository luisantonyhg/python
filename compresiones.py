
A = set()

A = { i for i in range(1,51) }

print(A)

print("==================================")
B = set()

for i in range(1,51):
    B.add(i)
    
    
print(B)

print("======================================")
D = [ord(i) for i in 'Python 2021']

print(D)

print("=======================================")
mensaje = 'Python 2021'
# --------------------------------------------------
#  ''.join() -> es para juntar    chr()-> para convertir en texto ascci  ord()-> para saber el orden numerico ascii  upper()-> para la mayuscula()
# -------------------------------------------------------
mensajeEncriptado = ''.join([chr(ord(i)+20) for i in mensaje.upper()])

print(mensajeEncriptado)