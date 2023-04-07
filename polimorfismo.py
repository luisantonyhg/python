
class Empleado:
    
    def __init__(self,sueldoBasico,nombre):
        self.sueldoBasico = sueldoBasico
        self.nombre = nombre
        
        
    def generar_boleta(self):
        pass
    


class Operador(Empleado):
    
    def __init__(self,sueldoBasico,nombre):
        # ESTO SE HACE CUANDO ESTAMOS DEFINIENDO DE OTRA CLASE PADRE
        super().__init__(sueldoBasico,nombre)
        
        
        
    
    
    def generar_boleta(self):
        print("Operador : ", self.nombre)
        print("Sueldo : ", 2*self.sueldoBasico)



class Asistente(Empleado):
    pass

    def __init__(self,sueldoBasico,nombre):
        super().__init__(sueldoBasico,nombre)   
         
    def generar_boleta(self):
        print("Asistente : ", self.nombre)
        print("Sueldo: " , 1.5* self.sueldoBasico)


class Planilla:
    
    def __init__(self):
        pass
    
    # def ImprimirPlanilla(self,empleado : Empleado): 
          
    def ImprimirPlanilla(self,empleado : Empleado): 
        empleado.generar_boleta()
        
        
operador1 = Operador(960,"Luis Antony")
operador1.generar_boleta()
asistente1 = Asistente(960,"Briana Diaz Gonzales")
asistente1.generar_boleta()
print("===============================================")
planillaN1 = Planilla()

planillaN1.ImprimirPlanilla(operador1)
print("===============================================")
planillaN1.ImprimirPlanilla(asistente1)