
from clases.trabajador import Trabajador  
from clases.gerente import Gerente
from clases.practicante import Practicante
from clases.empresa import Empresa

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
