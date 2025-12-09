from clases.empleado_base import EmpleadoBase   

from clases.vendedor import Vendedor
from clases.gerente import Gerente
from clases.practicante import Practicante
from clases.empresa import Empresa
def cargar_datos(empresa):
    empresa.agregar(Vendedor("Ana Gomez", "V001", 800000, 5000000, 5))
    empresa.agregar(Gerente("Luis Perez", "G001", 1500000, 300000))
    empresa.agregar(Practicante("Maria Ruiz", "P001", 80, 5000))        
    
def main():

    empresa = Empresa()
    cargar_datos(empresa)

    print("\n=== Empleados Registrados ===")
    for resumen in empresa.listar_todos():
        print(resumen)

    print("\n=== Empleados Activos ===")
    for activo in empresa.listar_activos():        
        print(f"{activo.tipo()}: {activo._nombre} - Remuneración: {activo.calcular_remuneracion():.2f}")            
    total_gasto = empresa.gasto_total()
    print(f"\nGasto total en remuneraciones: {total_gasto:.2f}\n")
if __name__ == "__main__":
    main()
