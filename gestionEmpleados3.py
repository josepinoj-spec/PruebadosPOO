
class Trabajador:
    def __init__(self, nombre, identificacion, sueldo_base, activo=True):
        # Validaciones básicas
        if not nombre:
            raise ValueError("El nombre no puede estar vacío.")
        if not identificacion:
            raise ValueError("La identificación no puede estar vacía.")
        if sueldo_base < 0:
            raise ValueError("El sueldo base no puede ser negativo.")

        self.__nombre = nombre
        self.__identificacion = identificacion
        self.__sueldo_base = float(sueldo_base)
        self.__activo = bool(activo)

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
        self.__activo = bool(estado)

    # Polimorfismo — se redefine en subclases
    def calcular_sueldo_final(self):
        return self.__sueldo_base

    def resumen(self):
        tipo = self.__class__.__name__
        return f"{self.__nombre} ({tipo}) - Sueldo base: ${self.__sueldo_base:,.2f}"


class Vendedor(Trabajador):
    def __init__(self, nombre, identificacion, sueldo_base, ventas_mes, porcentaje_comision, activo=True):
        super().__init__(nombre, identificacion, sueldo_base, activo)

        if ventas_mes < 0:
            raise ValueError("Las ventas del mes no pueden ser negativas.")
        if porcentaje_comision < 0 or porcentaje_comision > 1:
            raise ValueError("El porcentaje de comisión debe estar entre 0 y 1.")

        self.__ventas_mes = float(ventas_mes)
        self.__porcentaje_comision = float(porcentaje_comision)  # Ejemplo: 0.05 para 5%

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
        if bono_fijo < 0:
            raise ValueError("El bono fijo no puede ser negativo.")
        self.__bono_fijo = float(bono_fijo)

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
        # El practicante tiene sueldo base 0 por definición
        super().__init__(nombre, identificacion, 0, activo)

        if valor_hora < 0:
            raise ValueError("El valor hora no puede ser negativo.")
        if horas_trabajadas < 0:
            raise ValueError("Las horas trabajadas no pueden ser negativas.")

        self.__valor_hora = float(valor_hora)
        self.__horas_trabajadas = float(horas_trabajadas)

    def calcular_sueldo_final(self):
        return self.__valor_hora * self.__horas_trabajadas

    def resumen(self):
        return (
            f"[Practicante] {self.get_nombre()} | ID: {self.get_identificacion()} | "
            f"Horas: {self.__horas_trabajadas:.0f} | Valor hora: ${self.__valor_hora:,.2f} | "
            f"Sueldo final: ${self.calcular_sueldo_final():,.2f}"
        )


class Empresa:
    def __init__(self, nombre):
        if not nombre:
            raise ValueError("El nombre de la empresa no puede estar vacío.")
        self.__nombre = nombre
        self.__trabajadores = []

    def agregar_trabajador(self, trabajador):
        # Evitar duplicados de identificación
        for t in self.__trabajadores:
            if t.get_identificacion() == trabajador.get_identificacion():
                print(f" Ya existe un trabajador con ID {trabajador.get_identificacion()}. No se agrega.")
                return
        self.__trabajadores.append(trabajador)

    def listar_trabajadores(self):
        return self.__trabajadores

    def listar_activos(self):
        return [t for t in self.__trabajadores if t.is_activo()]

    def gasto_total(self):
        # Solo activos, como lo definiste
        return sum(t.calcular_sueldo_final() for t in self.listar_activos())

    def resumen_general(self):
        print(f"\n=== Reporte de Sueldos - {self.__nombre} ===\n")
        for t in self.listar_trabajadores():
            print(t.resumen())
        print(f"\nGasto total mensual (solo activos): ${self.gasto_total():,.2f}")