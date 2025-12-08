from class.flotavehiculos import FlotaVehiculos

from class.vehiculo import Vehiculo

from class.automovil import Automovil 

from class.motocicleta import Motocicleta

from class.camion import Camion

if __name__ == "__main__":
    flota = FlotaVehiculos()

    # Vehículos de prueba
    Auto = Automovil("KJDW10", "Toyota", "Yaris", 2018, 4)
    Moto = Motocicleta ("MOTO88", "Honda", "CBR", 2020, 600)
    Camion = camion("CAM555", "Volvo", "FH", 2019, 12000)

    # Agregar a la flota
    flota.agregar(auto)
    flota.agregar(moto)
    flota.agregar(camion)

    print("\n=== Vehículos Registrados ===")
    for desc in flota.listar():
        print(desc)

    km = 150
    print(f"\n=== Consumos para {km} km ===")
    for v_id, consumo in flota.consumos_individuales(km).items():
        print(f"{v_id}: {consumo:.2f} L")

    print("\n=== Consumo Total ===")
    print(f"{flota.consumo_total(km):.2f} L")