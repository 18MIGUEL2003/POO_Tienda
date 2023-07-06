class Vendedor:
    """
    Clase que representa a un vendedor.
    """
    def __init__(self, id_vendedor, nombre_vendedor, telefono_vendedor, direccion_vendedor, edad_vendedor):
        """
        Constructor de la clase Vendedor.
        Parámetros:
        - id_vendedor (int): Identificador del vendedor.
        - nombre_vendedor (str): Nombre del vendedor.
        - telefono_vendedor (str): Número de teléfono del vendedor.
        - direccion_vendedor (str): Dirección del vendedor.
        - edad_vendedor (int): Edad del vendedor.
        """
        self.id_vendedor = id_vendedor
        self.nombre_vendedor = nombre_vendedor
        self.telefono_vendedor = telefono_vendedor
        self.direccion_vendedor = direccion_vendedor
        self.edad_vendedor = edad_vendedor

    def mostrar_vendedor(self):
        """
        Muestra la información del vendedor por consola.
        """
        print("Id: ", self.id_vendedor)
        print("Nombre: ", self.nombre_vendedor)
        print("Telefono: ", self.telefono_vendedor)
        print("Direccion: ", self.direccion_vendedor)
        print("Edad: ", self.edad_vendedor)
