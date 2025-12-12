

class Cuenta:
    """Clase base para cuentas bancarias.
    Encapsula número, titular, saldo y tipo; registra movimientos.
    """

    def __init__(self, numero, titular, saldo_inicial, tipo):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = float(saldo_inicial)
        self.__tipo = tipo
        self.__movimientos = []

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def tipo(self):
        return self.__tipo

    def _ajustar_saldo(self, delta):
        self.__saldo += float(delta)

    def registrar_movimiento(self, texto):
        self.__movimientos.append(texto)

    def mostrar_movimientos(self):
        print(f"\nHistorial de movimientos — Cuenta {self.numero}")
        for mov in self.__movimientos:
            print("•", mov)

    def depositar(self, monto):
        if monto <= 0:
            print("El monto del depósito debe ser positivo.")
            return
        self._ajustar_saldo(monto)
        self.registrar_movimiento(f"DEPÓSITO ${monto:,.2f}")

    def retirar(self, monto):
        if monto <= 0:
            print("El monto del retiro debe ser positivo.")
            return False
        if monto > self.saldo:
            print("Saldo insuficiente para realizar el retiro.")
            return False
        self._ajustar_saldo(-monto)
        self.registrar_movimiento(f"RETIRO ${monto:,.2f}")
        return True

    def mostrar_resumen(self):
        print(
            f"Cuenta {self.numero}\n"
            f" Titular: {self.titular}\n"
            f" Tipo: {self.tipo}\n"
            f" Saldo: ${self.saldo:,.2f}"
        )


class CuentaCorriente(Cuenta):
    def __init__(self, numero, titular, saldo_inicial, linea_credito):
        super().__init__(numero, titular, saldo_inicial, "Corriente")
        self.__linea_credito = float(linea_credito)

    @property
    def linea_credito(self):
        return self.__linea_credito

    def retirar(self, monto):
        if monto <= 0:
            print("El monto del retiro debe ser positivo.")
            return False
        if monto > (self.saldo + self.__linea_credito):
            print("Límite de crédito excedido.")
            return False
        self._ajustar_saldo(-monto)
        self.registrar_movimiento(f"RETIRO ${monto:,.2f} (Cta. Corriente)")
        return True

    def mostrar_resumen(self):
        print(
            f"Cuenta Corriente {self.numero}\n"
            f" Titular: {self.titular}\n"
            f" Saldo: ${self.saldo:,.2f}\n"
            f" Línea crédito: ${self.__linea_credito:,.2f}"
        )


class CuentaAhorro(Cuenta):
    def __init__(self, numero, titular, saldo_inicial, tasa_interes):
        super().__init__(numero, titular, saldo_inicial, "Ahorro")
        if tasa_interes < 0:
            raise ValueError("La tasa de interés no puede ser negativa.")
        self.__tasa_interes = float(tasa_interes)

    @property
    def tasa_interes(self):
        return self.__tasa_interes

    def aplicar_interes(self):
        interes = self.saldo * self.__tasa_interes
        self._ajustar_saldo(interes)
        self.registrar_movimiento(
            f"INTERÉS ${interes:,.2f} ({self.__tasa_interes*100:.2f}%)"
        )
        print(f"Interés aplicado: ${interes:,.2f}")
        return interes

    def mostrar_resumen(self):
        print(
            f"Cuenta Ahorro {self.numero}\n"
            f" Titular: {self.titular}\n"
            f" Saldo: ${self.saldo:,.2f}\n"
            f" Tasa: {self.__tasa_interes*100:.2f}%"
        )


class Banco:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__cuentas = []

    @property
    def nombre(self):
        return self.__nombre

    def agregar_cuenta(self, cuenta):
        if self.buscar_cuenta(cuenta.numero) is not None:
            raise ValueError(f"Ya existe una cuenta con número {cuenta.numero}.")
        self.__cuentas.append(cuenta)

    def buscar_cuenta(self, numero):
        for c in self.__cuentas:
            if c.numero == numero:
                return c
        return None

    def mostrar_cuentas(self):
        print(f"\n=== {self.__nombre}: Listado de cuentas ===")
        for c in self.__cuentas:
            c.mostrar_resumen()

    def saldo_total(self):
        return sum(c.saldo for c in self.__cuentas)
