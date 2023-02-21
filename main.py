from models.Carrito import Carrito
from models.Factura import Factura
from models.Producto import Producto
from models.Tieda import Tienda


salir = False

lista_productos = [
    Producto("A1", "Galleta", "Paquete de galletas x4", 600, 10),
    Producto("A2", "Galleta Oreo", "Paquete x6", 1200, 2),
    Producto("A3", "Panela", "Paquete de panela x2", 2500, 0)
]

tienda = Tienda(lista_productos)

while (salir != True):
    print("Bienvenido!!")

    tienda.ver_productos_disponibles()
    menu = 0

    carrito = Carrito([])
    factura = Factura()
    while (menu != 4):
        menu = int(
            input("\n0. Listar Productos carrito \n1. Agregar Producto \n2. Eliminar Producto \n3.Ver Factura \n4 Nueva Persona. \n5. Salir \n"))

        if (menu == 0):

            carrito.ver_productos()

        if (menu == 1):

            tienda.ver_productos_disponibles()
            id_producto = input("Digite el codigo del producto \n")
            producto = tienda.obtener_producto(id_producto)

            if isinstance(producto, Producto):
                carrito.agregar_producto(producto)
                continue

            print("Producto no existente cv")
        if (menu == 2):

            tienda.ver_productos_disponibles()
            id_producto = input("Digite el codigo del producto \n")
            carrito.eliminar_producto(id_producto)
        if (menu == 3):

            carrito.ver_productos()
            factura.imprimir_total_factura(carrito.lista_productos)

        if (menu == 4):
            break
        if (menu == 5):
            salir = True
            break
