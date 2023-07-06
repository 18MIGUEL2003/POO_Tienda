from os import system
from tienda import Tienda

class Menu:
    """
    La clase Menu representa un menú interactivo para interactuar con una Tienda.
    Atributos:
        tienda (Tienda): La instancia de la clase Tienda utilizada para realizar las operaciones.
    Métodos:
        mostrar_menu_principal(): Muestra el menú principal y maneja las opciones seleccionadas por el usuario.
    """
    def __init__(self):
        """
        Inicializa una instancia de la clase Menu.
        """
        self.tienda = Tienda()

    def mostrar_menu_principal(self):
        """
        Muestra el menú principal y maneja las opciones seleccionadas por el usuario.
        """
        while True:
            system("cls")
            print("************************************")
            print("************** TIENDA **************")
            print("************ ************************")
            print("1: Registrar vendedor.")
            print("2: Listar vendedores.")
            print("3: Modificar vendedor.")
            print("4: Eliminar vendedor.")
            print("5: Registrar producto.")
            print("6: Listar productos.")
            print("7: Modificar productos.")
            print("8: Eliminar productos.")
            print("9: Registrar venta.")
            print("10: Modificar venta.")
            print("11: Mostrar ventas por producto.")
            print("12: Mostrar ventas por fecha.")
            print("13: Mostrar ventas por vendedor.")
            print("0: Salir")
            print("************************************")

            try:
                opcion = int(input("Digite la opción: "))
                print("************************************")

                if opcion == 1:
                    self.tienda.crear_vendedor()

                elif opcion == 2:
                    self.tienda.listar_vendedores()

                elif opcion == 3:
                    self.tienda.modificar_vendedor()

                elif opcion == 4:
                    self.tienda.eliminar_vendedor()

                elif opcion == 5:
                    self.tienda.crear_producto()

                elif opcion == 6:
                    self.tienda.listar_productos()

                elif opcion == 7:
                    self.tienda.modificar_producto()

                elif opcion == 8:
                    self.tienda.eliminar_producto()

                elif opcion == 9:
                    self.tienda.registrar_venta()

                elif opcion == 10:
                    self.tienda.modificar_venta()

                elif opcion == 11:
                    self.tienda.mostrar_ventas()

                elif opcion == 12:
                    self.tienda.mostrar_ventas_fecha()

                elif opcion == 13:
                    self.tienda.mostrar_ventas_vendedor()
                    
                elif opcion == 0:
                    break

                else:
                    print("************************************")
                    print("Error - Opción no válida")
                    print("************************************")
                    input()

            except ValueError:
                print("************************************")
                print("Error - El dato debe ser entero")
                print("************************************")
                input()

if __name__ == '__main__':
    tienda = Tienda()
    menu = Menu()
    menu.mostrar_menu_principal()
