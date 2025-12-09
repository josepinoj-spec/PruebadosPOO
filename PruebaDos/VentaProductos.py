
class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock

    # Encapsulamiento
    def get_codigo(self):
        return self.__codigo

    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio

    def get_stock(self):
        return self.__stock

    def actualizar_stock(self, cantidad):
        if cantidad <= self.__stock:
            self.__stock -= cantidad
        else:
            raise ValueError("No hay suficiente stock disponible.")

    # Polimorfismo — redefinido en subclases
    def calcular_total(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva.")
        if cantidad > self.__stock:
            raise ValueError("Stock insuficiente.")
        return self.__precio * cantidad

    def tipo_producto(self):
        return "Genérico"

    def descripcion(self):
        return f"{self.__nombre} ({self.tipo_producto()}) - ${self.__precio:,.2f} [Stock: {self.__stock}]"


class ProductoFisico(Producto):
    def __init__(self, codigo, nombre, precio, stock, peso, categoria_envio):
        super().__init__(codigo, nombre, precio, stock)
        self.__peso = peso
        self.__categoria_envio = categoria_envio.lower()

    def calcular_total(self, cantidad):
        total = super().calcular_total(cantidad)
        # Agregar costo de envío según categoría
        costo_envio = {
            "liviano": 5,
            "estandar": 10,
            "pesado": 20
        }.get(self.__categoria_envio, 10)
        return total + costo_envio

    def tipo_producto(self):
        return "Físico"

    def descripcion(self):
        return f"[Físico] {self.get_nombre()} - ${self.get_precio():,.2f} | Envío: {self.__categoria_envio.capitalize()} | Stock: {self.get_stock()}"


class ProductoDigital(Producto):
    def __init__(self, codigo, nombre, precio, stock, tamano_mb, tipo_licencia):
        super().__init__(codigo, nombre, precio, stock)
        self.__tamano_mb = tamano_mb
        self.__tipo_licencia = tipo_licencia.lower()

    def calcular_total(self, cantidad):
        total = super().calcular_total(cantidad)
        # Recargo por licencia comercial
        if self.__tipo_licencia == "comercial":
            total *= 1.15  # +15% de recargo
        return total

    def tipo_producto(self):
        return "Digital"

    def descripcion(self):
        return f"[Digital] {self.get_nombre()} - ${self.get_precio():,.2f} | Licencia: {self.__tipo_licencia.capitalize()} | Stock: {self.get_stock()}"

class Carrito:
    def __init__(self):
        self.__items = {}

    def agregar_producto(self, producto, cantidad):
        try:
            if cantidad <= 0:
                raise ValueError("La cantidad debe ser positiva.")
            if cantidad > producto.get_stock():
                raise ValueError(f"No hay suficiente stock para {producto.get_nombre()}.")

            producto.actualizar_stock(cantidad)
            if producto.get_codigo() in self.__items:
                self.__items[producto.get_codigo()]["cantidad"] += cantidad
            else:
                self.__items[producto.get_codigo()] = {
                    "producto": producto,
                    "cantidad": cantidad
                }
            print(f" {producto.get_nombre()} agregado correctamente ({cantidad} unidad(es)).")

        except ValueError as e:
            print(f" Error al agregar: {e}")

    def eliminar_producto(self, codigo):
        if codigo in self.__items:
            del self.__items[codigo]
            print(f"Producto {codigo} eliminado del carrito.")
        else:
            print(f"No existe el producto con código {codigo} en el carrito.")

    def mostrar_detalle(self):
        if not self.__items:
            print("El carrito está vacío.")
            return

        print("\n=== Detalle del Carrito ===")
        for item in self.__items.values():
            producto = item["producto"]
            cantidad = item["cantidad"]
            total = producto.calcular_total(cantidad)
            print(f"{producto.get_nombre()} | Tipo: {producto.tipo_producto()} | Cantidad: {cantidad} | Total: ${total:,.2f}")

    def total_general(self):
        total = sum(item["producto"].calcular_total(item["cantidad"]) for item in self.__items.values())
        print(f"\n Total general a pagar: ${total:,.2f}")
        return total
    
    
