
class EmpleadoBase(Empleado)):
    def __init__(self, nombre, identificacion, sueldo_base, activo=True):
        self._nombre = nombre
        self._identificacion = identificacion
        self._sueldo_base = sueldo_base
        self._activo = activo

    @property
    def nombre(self):
        return self._nombre
    
    @property
    def identificacion(self):
        return self._identificacion
    
    @property
    def sueldo_base(self):
        return self._sueldo_base
    
    @property
    def activo(self):
        return self._activo
    
    @activo.setter
    def activo(self, valor):
        self._activo = valor

    @abstractmethod
    def calcular_remuneracion(self):
        pass

    @abstractmethod
    def tipo(self):
        pass

    def resumen(self):
        return (
            f"{self.nombre} | {self.tipo()} | ID: {self.identificacion} | "
            f"Sueldo base: ${self.sueldo_base} | Pago final: ${self.calcular_remuneracion()}"
        )



# ---------- Vendedor (con comisiones) ----------
class Vendedor(EmpleadoBase):
    def __init__(self, nombre, identificacion, sueldo_base, ventas_mes, porcentaje_comision, activo=True):
        super().__init__(nombre, identificacion, sueldo_base, activo)
        self._ventas_mes = ventas_mes
        self._porcentaje_comision = porcentaje_comision

    def calcular_remuneracion(self):
        comision = self._ventas_mes * (self._porcentaje_comision / 100)
        return self.sueldo_base + comision

    def tipo(self):
        return "Vendedor"


# ---------- Gerente (con bono fijo) ----------
class Gerente(EmpleadoBase):
    def __init__(self, nombre, identificacion, sueldo_base, bono_fijo, activo=True):
        super().__init__(nombre, identificacion, sueldo_base, activo)
        self._bono_fijo = bono_fijo

    def calcular_remuneracion(self):
        return self.sueldo_base + self._bono_fijo

    def tipo(self):
        return "Gerente"


# ---------- Practicante (pago por hora) ----------
class Practicante(EmpleadoBase):
    def __init__(self, nombre, identificacion, horas_trabajadas, valor_hora, activo=True):
        super().__init__(nombre, identificacion, sueldo_base=0, activo=activo)
        self._horas_trabajadas = horas_trabajadas
        self._valor_hora = valor_hora

    def calcular_remuneracion(self):
        return self._horas_trabajadas * self._valor_hora

    def tipo(self):
        return "Practicante"


# ====================================================
# CLASE EMPRESA — ADMINISTRADOR DE EMPLEADOS
# ====================================================
class Empresa:
    def __init__(self):
        self._trabajadores = []

    def agregar(self, trabajador):
        self._trabajadores.append(trabajador)

    def listar_todos(self):
        return self._trabajadores

    def listar_activos(self):
        return [t for t in self._trabajadores if t.activo]

    def gasto_total(self):
        return sum(t.calcular_remuneracion() for t in self.listar_activos())

    def reporte_general(self):
        return [t.resumen() for t in self._trabajadores]



