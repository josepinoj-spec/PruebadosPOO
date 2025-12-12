

from clases.flota import Flota
from clases.automovil import Automovil
from clases.motocicleta import Motocicleta
from clases.camion import Camion

def main():
    flota = Flota()

    # Crear vehículos
    auto1 = Automovil("JKL123", "Kia", "Rio", 2020, 4)
    moto1 = Motocicleta("MTR500", "Yamaha", "R6", 2021, 600)
    camion1 = Camion("TRK900", "Mercedes", "Actros", 2019, 15000)

    # Agregar a la flota (evita duplicados según ID)
    for v in (auto1, moto1, camion1):
        flota.agregar(v)

    # Mostrar vehículos registrados
    print("\n=== Vehículos Registrados ===")
    for desc in flota.listar():
        print(desc)

    # Calcular consumo estimado para una distancia
    km = 150
    print(f"\n=== Consumo estimado para {km} km ===")
    consumos = flota.consumo_individual(km)
    for vid, consumo in consumos.items():
        print(f"{vid}: {consumo:.2f} L")

    # Consumo total de la flota
    print(f"\nConsumo total de la flota: {flota.consumo_total(km):.2f} L\n")


main()
