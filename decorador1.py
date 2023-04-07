
def habla(text):
    return text.upper()

print(habla('Hola Mundo'))


escucha = habla

print(escucha("Otro mensaje"))



def susurrar(text):
    return text.lower()

def hablar2(text):
    return text.upper()

def grita(funcion):
    gritando = funcion('Este se ha creado en la funcion grita, o parametro funcion')
    print(gritando)

grita(hablar2)
print("=============")
grita(susurrar)


# def sumar( x):
#     def otronumero(y):
#         return 


def decoradorSaludos(funcion):
    
    def inner1():
        print("Esto es antes de ejecucion de funcion")
        
        funcion()
        print("Esto es despues de la ejecucion de funcion")
        
    return inner1

def funcionHacerUsada():
    
    print("ESto esta dentro de la funcion")
    
    
otraFuncion = decoradorSaludos( funcionHacerUsada)
otraFuncion()


def PresentacionUnica():
    print("Hola mi gente")
    
print("======================") 
otraFuncion2 = decoradorSaludos(PresentacionUnica)
otraFuncion2()
    
    