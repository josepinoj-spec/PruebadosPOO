from clases.cuenta_corriente import CuentaCorriente
from clases.cuenta_ahorro import CuentaAhorro
from clases.banco import Banco
# =================


def main():
    banco = Banco("Banco PulsR")

    # Crear cuentas
    cc1 = CuentaCorriente("CC1001", "Ana Pérez", 500000, 200000)
    cc2 = CuentaCorriente("CC1002", "Carlos Ruiz", 1000000, 300000)
    ca1 = CuentaAhorro("CA2001", "María Gómez", 800000, 0.02)
    ca2 = CuentaAhorro("CA2002", "Pedro Soto", 1500000, 0.015)

    # Registrar en el banco
    banco.agregar_cuenta(cc1)
    banco.agregar_cuenta(cc2)
    banco.agregar_cuenta(ca1)
    banco.agregar_cuenta(ca2)

    # Operaciones de ejemplo
    cc1.depositar(250000)
    cc1.retirar(700000)  # Permitido (usa línea de crédito)
    ca1.retirar(100000)
    ca1.aplicar_interes()
    cc2.retirar(1500000)  # Excede línea de crédito → rechazado
    ca2.depositar(500000)

    # Mostrar resumen general
    banco.mostrar_cuentas()
    print(f"\nSaldo total administrado por el banco: ${banco.saldo_total():,.2f}\n")

    # Mostrar historial de una cuenta específica
    cuenta = banco.buscar_cuenta("CA2001")
    if cuenta:
        cuenta.mostrar_movimientos()


if __name__ == "__main__":
    main()
