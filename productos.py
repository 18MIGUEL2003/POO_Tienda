class Productos:
    """
    La clase Productos representa un producto con atributos como su ID, nombre, cantidad y valor.
    """
    def __init__(self, id_producto, nombre_producto, cantidad_producto, valor_producto):
        """
        Inicializa una instancia de la clase Productos con los valores proporcionados.
        Parametros:
            id_producto (int): El ID del producto.
            nombre_producto (str): El nombre del producto.
            cantidad_producto (int): La cantidad disponible del producto.
            valor_producto (float): El valor del producto.
        """
        self.id_producto = id_producto
        self.nombre_producto = nombre_producto
        self.cantidad_producto = cantidad_producto
        self.valor_producto = valor_producto

    def mostrar_producto(self):
        """
        Muestra la información del producto en la consola.
        """
        print("Id: ", self.id_producto)
        print("Nombre: ", self.nombre_producto)
        print("Cantidad: ", self.cantidad_producto)
        print("Valor: ", self.valor_producto)

