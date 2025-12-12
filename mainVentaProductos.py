

from clases.producto_fisico import ProductoFisico
from clases.producto_digital import ProductoDigital
from clases.carrito import Carrito

def main():
    # Crear productos
    p1 = ProductoFisico(
        codigo="A100",
        nombre="Mouse",
        precio=15000,
        stock=20,
        peso=0.2,
        categoria_envio="liviano"
    )

    p2 = ProductoDigital(
        codigo="D200",
        nombre="Curso Excel",
        precio=25000,
        stock=100,
        tamano_mb=500,
        tipo_licencia="comercial"
    )

    # Crear carrito
    carrito = Carrito()

    # Agregar productos
    carrito.agregar_producto(p1, 2)   # descuenta stock en p1
    carrito.agregar_producto(p2, 3)   # descuenta stock en p2

    # Mostrar detalle y total
    print(carrito.mostrar_detalle())
    print(f"Total general a pagar: ${carrito.total_general():,.2f}")

    # Eliminar un producto y restaurar stock
    carrito.eliminar_producto("A100")
    print("\nTras eliminar A100:")
    print(carrito.mostrar_detalle())
    print(f"Stock de Mouse luego de eliminar del carrito: {p1.stock}")

    # Limpiar carrito (restituye todos los stocks)
    carrito.limpiar()
    print("\nTras limpiar carrito:")
    print(carrito.mostrar_detalle())
    print(f"Stock de Curso Excel: {p2.stock}")

if __name__ == "__main__":
    main()
