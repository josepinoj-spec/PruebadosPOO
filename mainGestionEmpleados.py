from clases.empresa import Empresa
from clases.vendedor import Vendedor
from clases.gerente import Gerente
from clases.practicante import Practicante
# =================


def main():
    empresa = Empresa("TechNova S.A.")

    # Crear trabajadores de distintos tipos
    v1 = Vendedor("Ana Pérez", "12.345.678-9", 800000, ventas_mes=5000000, porcentaje_comision=0.05)
    v2 = Vendedor("Carlos Díaz", "98.765.432-1", 750000, ventas_mes=2000000, porcentaje_comision=0.03, activo=False)
    g1 = Gerente("Laura Torres", "11.223.344-5", 1500000, bono_fijo=300000)
    p1 = Practicante("Mateo Silva", "22.111.333-4", valor_hora=5000, horas_trabajadas=80)

    # Agregar al registro de la empresa
    empresa.agregar_trabajador(v1)
    empresa.agregar_trabajador(v2)
    empresa.agregar_trabajador(g1)
    empresa.agregar_trabajador(p1)

    # Mostrar reporte completo
    empresa.resumen_general()


if __name__ == "__main__":
    main()
