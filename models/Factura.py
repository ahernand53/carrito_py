class Factura():

    def imprimir_total_factura(self, lista_producto):
        total = 0

        for producto in lista_producto:
            total += producto.precio

        print("-------- El total de la factura es: {} --------\n".format(total))
