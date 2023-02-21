

class Producto():

    def __init__(self, id_producto, nombre, descripcion, precio, cantidad_disponible):
        self.id_producto = id_producto
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad_disponible = cantidad_disponible

    def __str__(self) -> str:
        return "Codigo: {} [Nombre: {}, Descripcion: {}, Precio: {}, Stock: {}] \n".format(self.id_producto, self.nombre, self.descripcion, self.precio, self.cantidad_disponible)
