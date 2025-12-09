
from clases.flota import Flota
from clases.automovil import Automovil
from clases.motocicleta import Motocicleta
from clases.camion import Camion


def cargar_datos(flota):
    flota.agregar(Automovil("JKL123", "Kia", "Rio", 2020, 4))
    flota.agregar(Motocicleta("MTR500", "Yamaha", "R6", 2021, 600))
    flota.agregar(Camion("TRK900", "Mercedes", "Actros", 2019, 15000))

def main():
    flota = Flota()
    cargar_datos(flota)

    print("\n=== Vehículos Registrados ===")
    for d in flota.listar():
        print(d)

    km = 150
    print(f"\n=== Consumo para {km} km ===")
    consumos = flota.report_consumos(km)

    for vid, consumo in consumos.items():
        print(f"{vid}: {consumo:.2f} L")

    total = flota.consumo_total(km)
    print(f"\nConsumo total de la flota: {total:.2f} L\n")


if __name__ == "__main__":
    main()
