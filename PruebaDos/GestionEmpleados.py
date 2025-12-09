
class Trabajador:
    def __init__(self, nombre, identificacion, sueldo_base, activo=True):
        self.__nombre = nombre
        self.__identificacion = identificacion
        self.__sueldo_base = sueldo_base
        self.__activo = activo

    # Encapsulamiento (getters)
    def get_nombre(self):
        return self.__nombre

    def get_identificacion(self):
        return self.__identificacion

    def get_sueldo_base(self):
        return self.__sueldo_base

    def is_activo(self):
        return self.__activo

    def set_activo(self, estado):
        self.__activo = estado

    # Polimorfismo — se redefine en subclases
    def calcular_sueldo_final(self):
        return self.__sueldo_base

    def resumen(self):
        tipo = self.__class__.__name__
        return f"{self.__nombre} ({tipo}) - Sueldo base: ${self.__sueldo_base:,.2f}"
    

class Vendedor(Trabajador):
    def __init__(self, nombre, identificacion, sueldo_base, ventas_mes, porcentaje_comision, activo=True):
        super().__init__(nombre, identificacion, sueldo_base, activo)
        self.__ventas_mes = ventas_mes
        self.__porcentaje_comision = porcentaje_comision  # Ejemplo: 0.05 para 5%

    def calcular_sueldo_final(self):
        comision = self.__ventas_mes * self.__porcentaje_comision
        return self.get_sueldo_base() + comision

    def resumen(self):
        return (
            f"[Vendedor] {self.get_nombre()} | ID: {self.get_identificacion()} | "
            f"Sueldo base: ${self.get_sueldo_base():,.2f} | "
            f"Comisión: {self.__porcentaje_comision*100:.1f}% | "
            f"Sueldo final: ${self.calcular_sueldo_final():,.2f}"
        )


class Gerente(Trabajador):
    def __init__(self, nombre, identificacion, sueldo_base, bono_fijo, activo=True):
        super().__init__(nombre, identificacion, sueldo_base, activo)
        self.__bono_fijo = bono_fijo

    def calcular_sueldo_final(self):
        return self.get_sueldo_base() + self.__bono_fijo

    def resumen(self):
        return (
            f"[Gerente] {self.get_nombre()} | ID: {self.get_identificacion()} | "
            f"Sueldo base: ${self.get_sueldo_base():,.2f} | "
            f"Bono: ${self.__bono_fijo:,.2f} | "
            f"Sueldo final: ${self.calcular_sueldo_final():,.2f}"
        )


class Practicante(Trabajador):
    def __init__(self, nombre, identificacion, valor_hora, horas_trabajadas, activo=True):
        super().__init__(nombre, identificacion, 0, activo)
        self.__valor_hora = valor_hora
        self.__horas_trabajadas = horas_trabajadas

    def calcular_sueldo_final(self):
        return self.__valor_hora * self.__horas_trabajadas

    def resumen(self):
        return (
            f"[Practicante] {self.get_nombre()} | ID: {self.get_identificacion()} | "
            f"Horas: {self.__horas_trabajadas} | Valor hora: ${self.__valor_hora:,.2f} | "
            f"Sueldo final: ${self.calcular_sueldo_final():,.2f}"
        )

class Empresa:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__trabajadores = []

    def agregar_trabajador(self, trabajador):
        self.__trabajadores.append(trabajador)

    def listar_trabajadores(self):
        return self.__trabajadores

    def listar_activos(self):
        return [t for t in self.__trabajadores if t.is_activo()]

    def gasto_total(self):
        return sum(t.calcular_sueldo_final() for t in self.listar_activos())

    def resumen_general(self):
        print(f"\n=== Reporte de Sueldos - {self.__nombre} ===\n")
        for t in self.listar_trabajadores():
            print(t.resumen())
        print(f"\nGasto total mensual (solo activos): ${self.gasto_total():,.2f}")

