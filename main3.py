
from ejercicio3.clases.GestionEmpleados   import Trabajador  
from ejercicio3.clases.GestionEmpleados   import Gerente
from ejercicio3.clases.GestionEmpleados   import Practicante
from ejercicio3.clases.GestionEmpleados   import Empresa
from ejercicio3.clases.GestionEmpleados   import Vendedor
def main():
    empresa = Empresa("INACAP Servicios")

    # Datos de prueba (reales o simulados)
    t1 = Vendedor("Ana Pérez", "VEN-001", 850000, 5800000, 0.03)
    t2 = Gerente("Carlos Ruiz", "GER-900", 2500000, 450000)
    t3 = Practicante("María Gómez", "PRC-123", 4500, 120, activo=False)
    t4 = Vendedor("Pedro Soto", "VEN-002", 900000, 3250000, 0.025)

    for t in (t1, t2, t3, t4):
        empresa.agregar_trabajador(t)

    empresa.resumen_general()


main()