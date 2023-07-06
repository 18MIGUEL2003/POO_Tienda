class Venta:
    """
    Clase que representa una venta de un producto realizada por un vendedor.
    """
    def __init__(self, id_venta, fecha, id_producto, cantidad, id_vendedor, total):
        """
        Constructor de la clase Venta.
        Parámetros:
        - id_venta (int): Identificador de la venta.
        - fecha (str): Fecha de la venta.
        - id_producto (int): Identificador del producto vendido.
        - cantidad (int): Cantidad del producto vendido.
        - id_vendedor (int): Identificador del vendedor.
        - total (float): Monto total de la venta.
        """
        self.id_venta = id_venta
        self.fecha = fecha
        self.id_producto = id_producto
        self.cantidad = cantidad
        self.id_vendedor = id_vendedor
        self.total = total

    def mostrar_venta(self):
        """
        Muestra la información de la venta por consola.
        """
        print("Id: ", self.id_venta)
        print("Fecha: ", self.fecha)
        print("Id producto: ", self.id_producto)
        print("Cantidad: ", self.cantidad)
        print("Id vendedor: ", self.id_vendedor)




