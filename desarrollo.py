class Boleto:
    numeroBoleto = 0
    def __init__(self,nombreBoleto):
        self.nombreBoleto = nombreBoleto
        Boleto.numeroBoleto  += 1
        
        
    def __str__(self):
        return f""" Numero Boleto:  " {Boleto.numeroBoleto}  "nombre : "{self.nombreBoleto}"""
    
    

boleto1 = Boleto("Luis Antony")
print(boleto1)
boleto2 = Boleto("Pepe")
print(boleto2)
boleto3 = Boleto("Huamani Gonzales Luis")
print(boleto3)