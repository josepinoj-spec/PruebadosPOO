
from abc import ABC, abstractmethod

# ====================================================
class FlotaVehiculo(ABC):
    def __init__(self, id_Vehiculo, marca, modelo, FechaFabricacion):
        self.__id_Vehiculo = id_Vehiculo
        self.__marca = marca
        self.__modelo = modelo
        self.__FechaFabricacion = FechaFabricacion
        
    @property
    def id_Vehiculo(self):
        return self.__id_Vehiculo

    @property
    def marca(self):
        return self.__marca

    @property
    def modelo(self):
        return self.__modelo

    @property
    def FechaFabricacion(self):
        return self.__FechaFabricacion
    
    # MÉTODOS POLIMÓRFICOS OBLIGATORIOS
    @abstractmethod
    def calcular_consumo(self, km):
        pass

    @abstractmethod
    def descripcion(self):
        pass


# ====================================================
# CLASES HIJAS — HERENCIA + POLIMORFISMO
# ====================================================

class Automovil(FlotaVehiculo):
    def __init__(self, id_Vehiculo, marca, modelo, FechaFabricacion, puertas):
        super().__init__(id_Vehiculo, marca, modelo, FechaFabricacion)
        self.__puertas = puertas
        
    def calcular_consumo(self, km):
        return max(0, km * 0.10 - (self.__puertas * 0.005))

    def descripcion(self):
        return (
            f"[AUTO] {self.id_Vehiculo} - {self.marca} {self.modelo} "
            f"({self.FechaFabricacion}), Puertas: {self.__puertas}"
        )


class Motocicleta(FlotaVehiculo):
    def __init__(self, id_Vehiculo, marca, modelo, FechaFabricacion, cilindrada):
        super().__init__(id_Vehiculo, marca, modelo, FechaFabricacion)
        self.__cilindrada = cilindrada

    def calcular_consumo(self, km):
        return km * (0.04 + self.__cilindrada / 20000)

    def descripcion(self):
        return (
            f"[MOTO] {self.id_Vehiculo} - {self.marca} {self.modelo} "
            f"({self.FechaFabricacion}), CC: {self.__cilindrada}"
        )


class Camion(FlotaVehiculo):
    def __init__(self, id_Vehiculo, marca, modelo, FechaFabricacion, capacidad_carga):
        super().__init__(id_Vehiculo, marca, modelo, FechaFabricacion)
        self.__capacidad_carga = capacidad_carga

    def calcular_consumo(self, km):
        return km * (0.20 + self.__capacidad_carga / 10000)

    def descripcion(self):
        return (
            f"[CAMIÓN] {self.id_Vehiculo} - {self.marca} {self.modelo} "
            f"({self.FechaFabricacion}), Carga: {self.__capacidad_carga} kg"
        )


# ====================================================
# CLASE FLOTA — ADMINISTRA LOS VEHÍCULOS
# ====================================================

class Flota:
    def __init__(self):
        self.__vehiculos = {}

    def agregar(self, vehiculo):
        if vehiculo.id_Vehiculo in self.__vehiculos:
            raise ValueError("Error: La identificación ya existe en la flota.")
        
        self.__vehiculos[vehiculo.id_Vehiculo] = vehiculo

    def eliminar(self, identificacion):
        if identificacion not in self.__vehiculos:
            raise ValueError("Error: Vehículo no encontrado.")
        del self.__vehiculos[identificacion]

    def buscar(self, identificacion):
        return self.__vehiculos.get(identificacion)

    def listar(self):
        return [v.descripcion() for v in self.__vehiculos.values()]

    def consumo_total(self, km):
        return sum(v.calcular_consumo(km) for v in self.__vehiculos.values())

    def report_consumos(self, km):
        return {v.id_Vehiculo: v.calcular_consumo(km) for v in self.__vehiculos.values()}


