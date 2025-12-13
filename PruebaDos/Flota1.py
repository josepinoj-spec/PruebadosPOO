
class Vehiculo:
    def __init__(self, id_vehiculo, marca, modelo, ano_fabricacion):
        self.__id_vehiculo = id_vehiculo
        self.__marca = marca
        self.__modelo = modelo
        self.__ano_fabricacion = ano_fabricacion

    # Encapsulamiento (getters)
    def get_id(self):
        return self.__id_vehiculo

    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    def get_anio(self):
        return self.__ano_fabricacion

    # Métodos polimórficos (a implementar en subclases)
    def calcular_consumo(self, km):
        raise NotImplementedError("Debe implementarse en las subclases.")

    def descripcion(self):
        raise NotImplementedError("Debe implementarse en las subclases.")


class Automovil(Vehiculo):
    def __init__(self, id_vehiculo, marca, modelo, ano_fabricacion, puertas):
        super().__init__(id_vehiculo, marca, modelo, ano_fabricacion)
        self.__puertas = puertas

    def calcular_consumo(self, km):
        # Consumo base ajustado por número de puertas (ejemplo simple)
        return km * (0.1 + self.__puertas * 0.005)

    def descripcion(self):
        return (
            f"[Automóvil] {self.get_id()} - {self.get_marca()} {self.get_modelo()} "
            f"({self.get_anio()}) Puertas: {self.__puertas}"
        )


class Motocicleta(Vehiculo):
    def __init__(self, id_vehiculo, marca, modelo, ano_fabricacion, cilindrada):
        super().__init__(id_vehiculo, marca, modelo, ano_fabricacion)
        self.__cilindrada = cilindrada

    def calcular_consumo(self, km):
        # Motocicletas consumen menos; aumenta con la cilindrada (ejemplo simple)
        return km * (0.04 + self.__cilindrada / 20000)

    def descripcion(self):
        return (
            f"[Motocicleta] {self.get_id()} - {self.get_marca()} {self.get_modelo()} "
            f"({self.get_anio()}) Cilindrada: {self.__cilindrada} cc"
        )


class Camion(Vehiculo):
    def __init__(self, id_vehiculo, marca, modelo, ano_fabricacion, capacidad_carga):
        super().__init__(id_vehiculo, marca, modelo, ano_fabricacion)
        self.__capacidad_carga = capacidad_carga  # en kg

    def calcular_consumo(self, km):
        # Camiones consumen más; depende de la carga (ejemplo simple)
        return km * (0.2 + self.__capacidad_carga / 10000)

    def descripcion(self):
        return (
            f"[Camión] {self.get_id()} - {self.get_marca()} {self.get_modelo()} "
            f"({self.get_anio()}) Carga: {self.__capacidad_carga} kg"
        )


class Flota:
    def __init__(self):
        self.__vehiculos = {}

    def agregar(self, vehiculo):
        vid = vehiculo.get_id()
        if vid in self.__vehiculos:
            print(f"El vehículo {vid} ya existe en la flota.")
        else:
            self.__vehiculos[vid] = vehiculo

    def eliminar(self, id_vehiculo):
        if id_vehiculo in self.__vehiculos:
            del self.__vehiculos[id_vehiculo]
            print(f"Vehículo {id_vehiculo} eliminado correctamente.")
        else:
            print(f"No se encontró el vehículo con ID {id_vehiculo}.")

    def buscar(self, id_vehiculo):
        return self.__vehiculos.get(id_vehiculo)

    def listar(self):
        return [v.descripcion() for v in self.__vehiculos.values()]

    def consumo_individual(self, km):
        return {vid: v.calcular_consumo(km) for vid, v in self.__vehiculos.items()}

    def consumo_total(self, km):
        return sum(v.calcular_consumo(km) for v in self.__vehiculos.values())
    