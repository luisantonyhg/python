# -----------------------------------------------------------
#                       EXAMEN FINAL
#               APELLIDOS : HUAMANI GONZALES 
#               NOMBRES : LUIS ANTONY
#               ULTIMO DIGITO DE SU DNI : 2
# -----------------------------------------------------------
class Cliente:
    clientes = []

    def __init__(self, dni, apellidos, nombres):
        self.dni = dni
        self.apellidos = apellidos
        self.nombres = nombres
        self.registrar_nuevo_cliente()

    def registrar_nuevo_cliente(self):
        cli = {self.dni: [self.apellidos, self.nombres]}
        Cliente.clientes.append(cli)
        print("Los datos fueron guardados correctamente. \n Presione Enter/Intro para salir al menú")

    @staticmethod
    def consultar_clientes():
        print(f"""CONSULTA DE CLIENTES
        DNI             APELLIDOS           NOMBRES
        -------         ---------           --------""")
        for i in Cliente.clientes:
            for k, j in i.items():
                print(f"""        {k}             {j[0]}          {j[1]}""")


class CuentaAhorros:
    nro_cuenta = 10000
    cuentas = []

    def __init__(self, dni, tipo_cuenta, moneda, saldo_inicial):
        self.tipo_cuenta = tipo_cuenta
        self.moneda = moneda
        self.saldo_inicial = saldo_inicial
        self.dni = dni
        CuentaAhorros.nro_cuenta += 1
        self.registrar_cuenta()

    def registrar_cuenta(self):
        cuenta = {CuentaAhorros.nro_cuenta: [self.dni, self.tipo_cuenta, self.moneda, self.saldo_inicial]}
        CuentaAhorros.cuentas.append(cuenta)
        print(f"Los datos fueron guardados correctamente, se creó la cuenta {CuentaAhorros.nro_cuenta}")
        print("Presione ENTER/INTRO para salir del menú")

    @staticmethod
    def mostrar_movimiento_y_saldo(nro_cuenta):
        movimientos = Movimiento.movimientos

        for mov in movimientos:
            for i,j in mov.items():
                if j[0] == nro_cuenta:
                    print(f"{i}                 {j[2]}{j[1]}")
                    if j[2] == "+":
                        pass           
                    else:
                        pass

        print(CuentaAhorros.cuentas)


class Movimiento:
    nro_movimiento = 202110000
    movimientos = []
    monto = 0

    def __init__(self, monto):
        self.monto = monto
        Movimiento.monto = monto
        Movimiento.nro_movimiento += 1

    @staticmethod
    def depositar(nro_cuenta):
        operacion = "+"
        movi = {Movimiento.nro_movimiento: [nro_cuenta,Movimiento.monto,operacion]}
        Movimiento.movimientos.append(movi)
        print(f"Los Datos fuero guardados correctamente, se creó el moviemiento, {Movimiento.nro_movimiento}\nPresione ENTER/INTRO para salir")

    @staticmethod
    def retirar(nro_cuenta):
        operacion = "-"
        movi = {Movimiento.nro_movimiento: [nro_cuenta, Movimiento.monto, operacion]}
        Movimiento.movimientos.append(movi)
        print(f"Los Datos fuero guardados correctamente, se creó el moviemiento, {Movimiento.nro_movimiento}\nPresione ENTER/INTRO para salir")



# =============================================================================
def pintar_menu():
    print("""===============================
    1. REGISTRAR NUEVO CLIENTE
    2. CONSULTAR LISTA DE CLIENTES
    3. REGISTRAR CUENTA
    4. MOVIMIENTOS EN CUENTA
        a. DEPOSITAR
        b. RETIRAR
        C. MOSTRAR MOVIMIENTOS Y SALDO
    5. SALIR
    """)
def registrar_cliente():
    print("REGISTRAR NUEVO CLIENTE")
    dni = input("DNI: ")
    apellidos = input("APELLIDOS: ")
    nombres = input("NOMBRES: ")

    cli = Cliente(dni,apellidos,nombres)
    salir = input()
def listar_clientes():
    Cliente.consultar_clientes()
def reg_cuenta():
    print("REGISTRAR CUENTA")
    dni = input("DNI: ")
    tipo_cuenta = input("TIPO CUENTA: ")
    moneda = input("MONEDA: ")
    saldo_inicial = float(input("SALDO INICIAL: "))

    cue = CuentaAhorros(dni,tipo_cuenta,moneda,saldo_inicial)
    salir = input()

def pintar_sub_menu():
    print("""a. DEPOSITAR
b. RETIRAR
c. MOSTRAR MOVIMIENTOS Y SALDO""")

def depositar():
    print("""MOVIMIENTOS EN CUENTA
            DEPOSITAR""")

    nro_cuenta = input("NRO CUENTA: ")
    monto = float(input("MONTO: "))
    movi = Movimiento(monto)
    movi.depositar(nro_cuenta)

def retirar():
    nro_cuenta = input("NRO CUENTA: ")
    monto = float(input("MONTO: "))
    movi = Movimiento(monto)
    movi.retirar(nro_cuenta)

def mostrar_movimientos_saldos():
    print("""MOVIMIENTOS EN CUENTA
    MOSTRAR MOVIMIENTOS Y SALDO""")
    nro_cuenta = input("NRO CUENTA: ")

    print("""ID MOVIMIENTO          MONTO""")
    print("---------------          --------")
    CuentaAhorros.mostrar_movimiento_y_saldo(nro_cuenta)


# =============================================================================
print("""BANCO DEL NUEVO MUNDO
        MENU""")

while True:
    pintar_menu()
    opcion = input("ELIJA UNA OPCION Y PRESIONE INTRO: ")

    if opcion == "1":
        registrar_cliente()
    elif opcion == "2":
        listar_clientes()
    elif opcion == "3":
        reg_cuenta()
    elif opcion == "4":
        pintar_sub_menu()
        opcion_sm = input("ELIJA UNA OPCION DEL SUBMENU: ")

        if opcion_sm == "a":
            depositar()
        elif opcion_sm == "b":
            retirar()
        elif opcion_sm == "c":
            mostrar_movimientos_saldos()

    elif opcion == 5:
        break


