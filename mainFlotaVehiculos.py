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

    # Agregar a la flota
    flota.agregar(auto1)
    flota.agregar(moto1)
    flota.agregar(camion1)

    # Mostrar vehículos
    print("\n=== Vehículos Registrados ===")
    for desc in flota.listar():
        print(desc)

    # Calcular consumo
    km = 150
    print(f"\n=== Consumo estimado para {km} km ===")
    consumos = flota.consumo_individual(km)
    for vid, consumo in consumos.items():
        print(f"{vid}: {consumo:.2f} L")

    print(f"\nConsumo total de la flota: {flota.consumo_total(km):.2f} L\n")


if __name__ == "__main__":
    main()

    