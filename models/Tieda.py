
from models.Producto import Producto


class Tienda():

    def __init__(self, lista_productos):
        self.lista_productos: list(Producto) = lista_productos

    def ver_productos_disponibles(self):
        if len(self.lista_productos) == 0:
            return print("No hay productos actualmente.")

        for producto in self.lista_productos:
            print(producto)

    def obtener_producto(self, id_producto) -> Producto:
        for producto in self.lista_productos:
            if (producto.id_producto == id_producto):
                return producto

    def agregar_producto(self, producto):
        self.lista_productos.append(producto)
        print("Se ha agregado el producto correctamente.")

    def eliminar_producto(self, id_producto):
        for producto in self.lista_productos:
            if (producto.id_producto == id_producto):
                self.lista_productos.remove(producto)
                print("Producto eliminado correctamente.")
                return

        print("Producto no encontrado")
