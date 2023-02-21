
from models.Producto import Producto


class Carrito():

    def __init__(self, lista_productos):
        self.lista_productos: list(Producto) = lista_productos

    def ver_productos(self):
        if len(self.lista_productos) == 0:
            return print("No hay productos en el carrito.")

        for producto in self.lista_productos:
            print(producto)

    def agregar_producto(self, producto):
        if producto.cantidad_disponible == 0:
            print("Producto agotado.")
            return

        self.lista_productos.append(producto)
        print("Se ha agregado el producto en el carrito correctamente.")

    def eliminar_producto(self, id_producto):
        for producto in self.lista_productos:
            if (producto.id_producto == id_producto):
                self.lista_productos.remove(producto)
                print("Producto eliminado del carrito correctamente.")
                return

        print("Producto no encontrado")
