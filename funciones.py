

def saludar (argumento):
    print("bienvenido a Python", argumento)
    
    

for i in range(10):
    saludar('luis')
    
# si se olvida un parametro por defecto sera una vacio
def escribir(argumento = ''):
    print(argumento)
    
    

def mostrarDatos(dni,apellidos,nombres):
    print('DNI      :', dni)
    print('APELLIDOS :', apellidos)
    print('NOMBRES :',nombres)
    


mostrarDatos(71112652,'huamani gonzales', 'luisantony' )
    
    

    