

class Boleto:
    
    def __init__(self, nombreComprador):
        self.nombreComprador = nombreComprador
           
        numeroBoleto= []
       
        for i in range(1,100):
            numeroBoleto.insert(i)
            print ("N° Boleto : ", numeroBoleto[1] , "Nombre es : ", self.nombreComprador)
        

boleto1 = Boleto('Luis')