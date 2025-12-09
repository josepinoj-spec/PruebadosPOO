
class Cuenta:
    def __init__(self, numero, titular, saldo_inicial, tipo):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo_inicial
        self.__tipo = tipo
        self.__movimientos = []

    # ----- Encapsulamiento -----
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
        self.__saldo += monto
        self.registrar_movimiento(f"DEPÓSITO ${monto:,.2f}")

    def retirar(self, monto):
        if monto <= 0:
            print("El monto del retiro debe ser positivo.")
            return False
        if monto > self.__saldo:
            print("Saldo insuficiente para realizar el retiro.")
            return False
        self.__saldo -= monto
        self.registrar_movimiento(f"RETIRO ${monto:,.2f}")
        return True

    def mostrar_resumen(self):
        print(f"Cuenta {self.numero} | Titular: {self.titular} | Tipo: {self.tipo} | Saldo: ${self.saldo:,.2f}")


class CuentaCorriente(Cuenta):
    def __init__(self, numero, titular, saldo_inicial, linea_credito):
        super().__init__(numero, titular, saldo_inicial, "Corriente")
        self.__linea_credito = linea_credito

    def retirar(self, monto):
        if monto <= 0:
            print("El monto del retiro debe ser positivo.")
            return False
        if monto > (self.saldo + self.__linea_credito):
            print("Límite de crédito excedido.")
            return False

        # Permite sobregiro
        self._Cuenta__saldo -= monto  
        self.registrar_movimiento(f"RETIRO ${monto:,.2f} (Cta. Corriente)")
        return True

    def mostrar_resumen(self):
        print(f"Cuenta Corriente {self.numero} | Titular: {self.titular} | Saldo: ${self.saldo:,.2f} | Línea crédito: ${self.__linea_credito:,.2f}")


class CuentaAhorro(Cuenta):
    def __init__(self, numero, titular, saldo_inicial, tasa_interes):
        super().__init__(numero, titular, saldo_inicial, "Ahorro")
        self.__tasa_interes = tasa_interes

    def aplicar_interes(self):
        interes = self.saldo * self.__tasa_interes
        self._Cuenta__saldo += interes
        self.registrar_movimiento(f"INTERÉS ${interes:,.2f} ({self.__tasa_interes*100:.2f}%)")
        print(f"Interés aplicado: ${interes:,.2f}")

    def mostrar_resumen(self):
        print(f"Cuenta Ahorro {self.numero} | Titular: {self.titular} | Saldo: ${self.saldo:,.2f} | Tasa: {self.__tasa_interes*100:.2f}%")
