
from clases.producto import Producto        
from clases.producto_fisico import ProductoFisico
from clases.producto_digital import ProductoDigital
from clases.carrito import Carrito



def main():
    # Crear productos
    libro = ProductoFisico("LIB123", "Libro Python", 25.0, 10, peso=0.5, categoria_envio="liviano")
    polera = ProductoFisico("POL456", "Polera Negra", 18.0, 5, peso=0.3, categoria_envio="estandar")
    curso = ProductoDigital("CUR789", "Curso IA", 50.0, 100, tamano_mb=5000, tipo_licencia="personal")
    licencia = ProductoDigital("LIC321", "Licencia Software Pro", 120.0, 50, tamano_mb=0, tipo_licencia="comercial")

    # Crear carrito y agregar productos
    carrito = Carrito()
    carrito.agregar_producto(libro, 2)
    carrito.agregar_producto(polera, 1)
    carrito.agregar_producto(curso, 1)
    carrito.agregar_producto(licencia, 3)

    # Mostrar detalles y total
    carrito.mostrar_detalle()
    carrito.total_general()


if __name__ == "__main__":
    main()
