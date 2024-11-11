# Definición de la clase base Prenda
class Prenda:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Precio: ${self.precio}, Stock: {self.cantidad}")

# Definición de la clase RopaHombre que hereda de Prenda
class RopaHombre(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self.talla = talla

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Talla: {self.talla}")

# Definición de la clase RopaMujer que hereda de Prenda
class RopaMujer(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self.talla = talla

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Talla: {self.talla}")

# Definición de la clase Inventario para gestionar las prendas
class Inventario:
    def __init__(self):
        self.prendas = []

    def agregar_prenda(self, prenda):
        self.prendas.append(prenda)

    def mostrar_inventario(self):
        for prenda in self.prendas:
            prenda.mostrar_info()
            print("-" * 20)  # Separador visual entre prendas

# Función principal para probar el sistema
def main():
    # Creación de instancias de ropa de hombre y mujer
    camisa = RopaHombre("Camisa de Hombre", 25.00, 50, "M")
    pantalon = RopaHombre("Pantalón de Hombre", 30.00, 30, "L")
    chaqueta = RopaHombre("Chaqueta de Hombre", 55.00, 20, "XL")
    falda = RopaMujer("Falda de Mujer", 28.00, 15, "S")
    blusa = RopaMujer("Blusa de Mujer", 22.00, 40, "M")
    vestido = RopaMujer("Vestido de Mujer", 45.00, 10, "L")
    zapatos_h = RopaHombre("Zapatos de Hombre", 60.00, 25, "42")
    zapatos_m = RopaMujer("Zapatos de Mujer", 50.00, 20, "38")

    # Creación del inventario y agregación de las prendas
    inventario = Inventario()
    inventario.agregar_prenda(camisa)
    inventario.agregar_prenda(pantalon)
    inventario.agregar_prenda(chaqueta)
    inventario.agregar_prenda(falda)
    inventario.agregar_prenda(blusa)
    inventario.agregar_prenda(vestido)
    inventario.agregar_prenda(zapatos_h)
    inventario.agregar_prenda(zapatos_m)

    # Muestra el inventario actual
    print("Inventario de Ropa Disponible:")
    inventario.mostrar_inventario()

# Ejecución de la función principal
if __name__ == "__main__":
    main()
