
from Vehiculo import Automovil, Motocicleta, Camion

class FlotaVehiculo:
    def __init__(self, id_Vehiculo, marca, modelo, Fecha_Fabricacion):
        self.__id_Vehiculo = id_Vehiculo
        self.__marca = marca
        self.__modelo = modelo
        self.__Fecha_Fabricacion = Fecha_Fabricacion
        
    @property
    def identificacion(self):
        return self.__id_Vehiculo

    @property
    def marca(self):
        return self.__marca

    @property
    def modelo(self):
        return self.__modelo

    @property
    def anio(self):
        return self.__Fecha_Fabricacion
    
    
class Automovil(Vehiculo):
    def __init__(self, id_Vehiculo, marca, modelo, Fecha_Fabricacion, puertas):
        super().__init__(id_Vehiculo, marca, modelo, Fecha_Fabricacion)
        self.puertas = puertas
        
    def calcular_consumo(self, km):
        return max(0, km * 0.10 - (self.puertas * 0.005))

    def descripcion(self):
        return f"[AUTO] {self.id_Vehiculo} - {self.marca} {self.modelo} ({self.Fecha_Fabricacion}), Puertas: {self.puertas}"


class Motocicleta(Vehiculo):
    def __init__(self, id_Vehiculo, marca, modelo, Fecha_Fabricacion, cilindrada):
        super().__init__(id_Vehiculo, marca, modelo, Fecha_Fabricacion)
        self.cilindrada = cilindrada

    def calcular_consumo(self, km):
        return km * (0.04 + self.cilindrada / 20000)

    def descripcion(self):
        return f"[MOTO] {self.id_Vehiculo} - {self.marca} {self.modelo} ({self.Fecha_Fabricacion}), CC: {self.cilindrada}"


class Camion(Vehiculo):
    def __init__(self, id_Vehiculo, marca, modelo, FechaFabricacion, capacidad_carga):
        super().__init__(id_Vehiculo, marca, modelo, FechaFabricacion)
        self.capacidad_carga = capacidad_carga

    def calcular_consumo(self, km):
        return km * (0.20 + self.capacidad_carga / 10000)

    def descripcion(self):
        return f"[CAMIÓN] {self.id_Vehiculo} - {self.marca} {self.modelo} ({self.Fecha_fabricacion}), Carga: {self.capacidad_carga} kg"


# ==============================
# CLASE FLOTA
# ==============================

class Flota:
    def __init__(self):
        self.vehiculos = {}

    def agregar(self, vehiculo):
        if vehiculo.identificacion in self.vehiculos:
            raise ValueError("Error: La identificación ya existe en la flota.")
        self.vehiculos[vehiculo.identificacion] = vehiculo

    def eliminar(self, identificacion):
        if identificacion in self.vehiculos:
            del self.vehiculos[identificacion]
        else:
            raise ValueError("Error: Vehículo no encontrado.")

    def buscar(self, identificacion):
        return self.vehiculos.get(identificacion, None)

    def listar(self):
        return [v.descripcion() for v in self.vehiculos.values()]

    def consumo_total(self, km):
        return sum(v.calcular_consumo(km) for v in self.vehiculos.values())

    def report_consumos(self, km):
        return {v.identificacion: v.calcular_consumo(km) for v in self.vehiculos.values()}
