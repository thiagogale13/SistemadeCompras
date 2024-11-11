class Prenda:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre  # Atributo público
        self.precio = precio  # Atributo público
        self.cantidad = cantidad  # Atributo público

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Precio: ${self.precio}, Stock: {self.cantidad}")


class RopaHombre(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self.talla = talla  # Atributo específico de RopaHombre

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Talla: {self.talla}")


class RopaMujer(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self.talla = talla  # Atributo específico de RopaMujer

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Talla: {self.talla}")


class Inventario:
    def __init__(self):
        self.prendas = []  # Lista para almacenar las prendas

    def agregar_prenda(self, prenda):
        self.prendas.append(prenda)

    def mostrar_inventario(self):
        print("Inventario de Ropa Disponible:")
        for prenda in self.prendas:
            prenda.mostrar_info()
            print("--------------------")


class Carrito:
    def __init__(self):
        self.items = []  # Lista de artículos en el carrito

    def agregar_al_carrito(self, prenda, cantidad):
        if prenda.cantidad >= cantidad:
            self.items.append((prenda, cantidad))
            prenda.cantidad -= cantidad  # Reducir el stock disponible
            print(f"Se ha agregado {cantidad} {prenda.nombre} al carrito.")
        else:
            print(f"No hay suficiente stock para {prenda.nombre}.")

    def mostrar_carrito(self):
        total = 0
        print("Carrito de Compras:")
        for prenda, cantidad in self.items:
            print(f"{prenda.nombre} - ${prenda.precio} x {cantidad}")
            total += prenda.precio * cantidad
        print(f"Total: ${total}")
        return total

    def procesar_compra(self):
        print("Compra procesada con éxito.")
        self.items.clear()  # Limpiar el carrito


# Crear instancias de Ropa
camisa = RopaHombre("Camisa de Hombre", 25.00, 50, "M")
pantalon = RopaHombre("Pantalón de Hombre", 30.00, 30, "L")
falda = RopaMujer("Falda de Mujer", 28.00, 15, "S")
blusa = RopaMujer("Blusa de Mujer", 22.00, 40, "M")

# Crear el inventario y agregar las prendas
inventario = Inventario()
inventario.agregar_prenda(camisa)
inventario.agregar_prenda(pantalon)
inventario.agregar_prenda(falda)
inventario.agregar_prenda(blusa)

# Mostrar el inventario
inventario.mostrar_inventario()

# Crear un carrito de compras
carrito = Carrito()

# Agregar prendas al carrito
carrito.agregar_al_carrito(camisa, 2)  # 2 Camisas de Hombre
carrito.agregar_al_carrito(falda, 1)   # 1 Falda de Mujer

# Mostrar el carrito y procesar la compra
carrito.mostrar_carrito()
carrito.procesar_compra()

# Mostrar el inventario después de la compra
inventario.mostrar_inventario()
