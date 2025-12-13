
from ejercicio2.clases.CuentasBancarias import Cuenta
from ejercicio2.clases.CuentasBancarias import CuentaCorriente
from ejercicio2.clases.CuentasBancarias import CuentaAhorro
from ejercicio2.clases.CuentasBancarias import Banco

def main():
    banco = Banco("Banco PulsR")

    # Crear cuentas
    cc1 = CuentaCorriente("CC1001", "Ana Pérez", 500_000, 200_000)
    cc2 = CuentaCorriente("CC1002", "Carlos Ruiz", 1_000_000, 300_000)
    ca1 = CuentaAhorro("CA2001", "María Gómez", 800_000, 0.02)
    ca2 = CuentaAhorro("CA2002", "Pedro Soto", 1_500_000, 0.015)

    # Registrar en el banco (con manejo de duplicados)
    for cuenta in (cc1, cc2, ca1, ca2):
        try:
            banco.agregar_cuenta(cuenta)
        except ValueError as e:
            print(f" {e}")

    # Operaciones de ejemplo con feedback claro
    print("\n=== Operaciones ===")

    print("Depósito CC1001 $250.000:", end=" ")
    cc1.depositar(250_000); print("OK")

    print("Retiro CC1001 $700.000:", end=" ")
    print("OK" if cc1.retirar(700_000) else "Rechazado")

    print("Retiro CA2001 $100.000:", end=" ")
    print("OK" if ca1.retirar(100_000) else "Rechazado")

    print("Aplicar interés CA2001:", end=" ")
    interes = ca1.aplicar_interes()
    print(f"+${interes:,.2f}")

    print("Retiro CC1002 $1.500.000:", end=" ")
    print("OK" if cc2.retirar(1_500_000) else "Rechazado")

    print("Depósito CA2002 $500.000:", end=" ")
    ca2.depositar(500_000); print("OK")

    # Mostrar resumen general
    print("\n=== Resumen de cuentas ===")
    banco.mostrar_cuentas()
    print(f"\nSaldo total administrado por el banco: ${banco.saldo_total():,.2f}\n")

    # Mostrar historial de una cuenta específica
    cuenta = banco.buscar_cuenta("CA2001")
    if cuenta:
        cuenta.mostrar_movimientos()
    else:
        print("Cuenta CA2001 no encontrada.")

if __name__ == "__main__":
    main()