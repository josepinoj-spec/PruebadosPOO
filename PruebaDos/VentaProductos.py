
class Producto:
    def __init__(self, codigo: str, nombre: str, precio: float, stock: int) -> None:
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        if stock < 0:
            raise ValueError("El stock no puede ser negativo.")
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = float(precio)
        self.__stock = int(stock)

    # Propiedades (encapsulamiento idiomático)
    @property
    def codigo(self) -> str:
        return self.__codigo

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def precio(self) -> float:
        return self.__precio

    @property
    def stock(self) -> int:
        return self.__stock

    def actualizar_stock(self, cantidad: int) -> None:
        if cantidad <= 0:
            raise ValueError("La cantidad a descontar debe ser positiva.")
        if cantidad > self.__stock:
            raise ValueError("No hay suficiente stock disponible.")
        self.__stock -= cantidad

    def restaurar_stock(self, cantidad: int) -> None:
        if cantidad <= 0:
            raise ValueError("La cantidad a restaurar debe ser positiva.")
        self.__stock += cantidad

    # Polimorfismo — redefinido en subclases
    def calcular_total(self, cantidad: int) -> float:
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva.")
        if cantidad > self.__stock:
            raise ValueError("Stock insuficiente.")
        return self.__precio * cantidad

    def tipo_producto(self) -> str:
        return "Genérico"

    def descripcion(self) -> str:
        return f"{self.__nombre} ({self.tipo_producto()}) - ${self.__precio:,.2f} [Stock: {self.__stock}]"

    def __repr__(self) -> str:
        return f"Producto(codigo={self.__codigo!r}, nombre={self.__nombre!r}, precio={self.__precio}, stock={self.__stock})"


class ProductoFisico(Producto):
    def __init__(self, codigo: str, nombre: str, precio: float, stock: int, peso: float, categoria_envio: str) -> None:
        super().__init__(codigo, nombre, precio, stock)
        if peso < 0:
            raise ValueError("El peso no puede ser negativo.")
        self.__peso = float(peso)
        self.__categoria_envio = categoria_envio.lower()

    @property
    def peso(self) -> float:
        return self.__peso

    @property
    def categoria_envio(self) -> str:
        return self.__categoria_envio

    def calcular_total(self, cantidad: int) -> float:
        total = super().calcular_total(cantidad)
        # Costo de envío por pedido (una sola vez). Cambia a "* cantidad" si quieres que sea por unidad.
        costo_envio_por_pedido = {
            "liviano": 5.0,
            "estandar": 10.0,
            "pesado": 20.0
        }.get(self.__categoria_envio, 10.0)
        return total + costo_envio_por_pedido

    def tipo_producto(self) -> str:
        return "Físico"

    def descripcion(self) -> str:
        return (f"[Físico] {self.nombre} - ${self.precio:,.2f} | "
                f"Envío: {self.__categoria_envio.capitalize()} | Peso: {self.__peso}kg | Stock: {self.stock}")


class ProductoDigital(Producto):
    def __init__(self, codigo: str, nombre: str, precio: float, stock: int, tamano_mb: float, tipo_licencia: str) -> None:
        super().__init__(codigo, nombre, precio, stock)
        if tamano_mb < 0:
            raise ValueError("El tamaño no puede ser negativo.")
        self.__tamano_mb = float(tamano_mb)
        self.__tipo_licencia = tipo_licencia.lower()

    @property
    def tamano_mb(self) -> float:
        return self.__tamano_mb

    @property
    def tipo_licencia(self) -> str:
        return self.__tipo_licencia

    def calcular_total(self, cantidad: int) -> float:
        total = super().calcular_total(cantidad)
        # Recargo por licencia comercial sobre el total
        if self.__tipo_licencia == "comercial":
            total *= 1.15  # +15% de recargo
        return total

    def tipo_producto(self) -> str:
        return "Digital"

    def descripcion(self) -> str:
        return (f"[Digital] {self.nombre} - ${self.precio:,.2f} | "
                f"Licencia: {self.__tipo_licencia.capitalize()} | Tamaño: {self.__tamano_mb}MB | Stock: {self.stock}")


class Carrito:
    def __init__(self) -> None:
        # items: codigo -> {"producto": Producto, "cantidad": int}
        self.__items = {}

    def agregar_producto(self, producto: Producto, cantidad: int) -> None:
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva.")
        if cantidad > producto.stock:
            raise ValueError(f"No hay suficiente stock para {producto.nombre}.")

        # Descontamos stock en el producto
        producto.actualizar_stock(cantidad)

        # Agregamos al carrito
        if producto.codigo in self.__items:
            self.__items[producto.codigo]["cantidad"] += cantidad
        else:
            self.__items[producto.codigo] = {"producto": producto, "cantidad": cantidad}

    def eliminar_producto(self, codigo: str) -> None:
        item = self.__items.pop(codigo, None)
        if item is not None:
            producto = item["producto"]
            cantidad = item["cantidad"]
            # Restituimos el stock al producto cuando se elimina del carrito
            producto.restaurar_stock(cantidad)
        else:
            raise KeyError(f"No existe el producto con código {codigo} en el carrito.")

    def mostrar_detalle(self) -> str:
        if not self.__items:
            return "El carrito está vacío."

        lines = ["=== Detalle del Carrito ==="]
        for item in self.__items.values():
            producto = item["producto"]
            cantidad = item["cantidad"]
            total = producto.calcular_total(cantidad)
            lines.append(f"{producto.nombre} | Tipo: {producto.tipo_producto()} | Cantidad: {cantidad} | Total: ${total:,.2f}")
        return "\n".join(lines)

    def total_general(self) -> float:
        return sum(item["producto"].calcular_total(item["cantidad"]) for item in self.__items.values())

    def limpiar(self) -> None:
        # Restituye stock de todos los productos y vacía el carrito
        for codigo, item in list(self.__items.items()):
            producto = item["producto"]
            cantidad = item["cantidad"]
            producto.restaurar_stock(cantidad)
            self.__items.pop(codigo)

