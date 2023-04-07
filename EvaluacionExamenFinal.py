# -----------------------------------------------------------
#                       EXAMEN FINAL
#               APELLIDOS : HUAMANI GONZALES 
#               NOMBRES : LUIS ANTONY
#               ULTIMO DIGITO DE SU DNI : 2
# -----------------------------------------------------------

class CuentaAhorros:
    
    def __init__(self,numeroCuenta,tipoCuenta,moneda,saldo):
        self.numeroCuenta = numeroCuenta
        self.tipoCuenta = tipoCuenta
        self.moneda = moneda
        self.saldo = saldo
        
        
    def registrarCuenta(self):
        pass
    
    
    def mostrarMovimientoYSaldos(self):
        pass
    

class Cliente(CuentaAhorros):
    
    def __init__(self,numeroCuenta,tipoCuenta,moneda,saldo, numeroDni,apellidos,nombres):
        
        super().__init__(numeroCuenta,tipoCuenta,moneda,saldo)
        self.numeroDni = numeroDni
        self.apellidos = apellidos
        self.nombres = nombres
        
    def registrarNuevoCliente(self):
        pass
    
    
    def consultarCliente(self):
        pass
    


class Movimiento(CuentaAhorros):
    
    def __init__(self,numeroCuenta,tipoCuenta,moneda,saldo,idMovimiento,monto):
        
        super().__init__(numeroCuenta,tipoCuenta,moneda,saldo)
        self.idMovimiento = idMovimiento
        self.monto = monto
        
        
    def depositar(self):
        pass
    
    
    def retirar(self):
        pass
    
    

nuevaCuenta = CuentaAhorros()
    
    
    
    
    