from os import system  # Importa la función system del módulo os
from vendedor import Vendedor  # Importa la clase Vendedor desde el archivo vendedor.py
from venta import Venta  # Importa la clase Venta desde el archivo venta.py
from productos import Productos  # Importa la clase Productos desde el archivo productos.py
from datetime import datetime  # Importa la clase datetime del módulo datetime

class Tienda():
    def __init__(self):
        # Inicializa las listas vacías
        self.vendedores = []  # Lista de vendedores
        self.productos = []  # Lista de productos
        self.ventas = []  # Lista de ventas
        self.id_ingresado_vendedor = []  # Lista de IDs ingresados de vendedores
        self.id_ingresado_producto = []  # Lista de IDs ingresados de productos
        self.id_ingresado_venta = []  # Lista de IDs ingresados de ventas
    
    def buscar_producto(self, producto):
        # Busca un producto por su ID en la lista de productos
        for i in range(len(self.productos)):
            if self.productos[i].id_producto == producto:
                return i  # Retorna la posición del producto si se encuentra
        return -1  # Retorna -1 si no se encuentra el producto

    def adicionar_vendedor(self, vendedor):
        # Añade un vendedor a la lista de vendedores
        if self.buscar_vendedor(vendedor.id_vendedor) == -1:
            self.vendedores.append(vendedor)
            return True  # Retorna True si el vendedor se agregó exitosamente
        return False  # Retorna False si el vendedor ya existe en la lista

    def adicionar_producto(self, producto):
        # Añade un producto a la lista de productos
        if self.buscar_producto(producto.id_producto) == -1:
            self.productos.append(producto)
            return True  # Retorna True si el producto se agregó exitosamente
        return False  # Retorna False si el producto ya existe en la lista
    
    def buscar_venta(self, id):
        # Busca una venta por su ID en la lista de ventas
        for i in range(len(self.ventas)):
            if self.ventas[i].id_venta == id:
                return i  # Retorna la posición de la venta si se encuentra
        return -1  # Retorna -1 si no se encuentra la venta
    
    def buscar_vendedor(self, vendedor):
        # Busca un vendedor por su ID en la lista de vendedores
        for i in range(len(self.vendedores)):
            if self.vendedores[i].id_vendedor == vendedor:
                return i  # Retorna la posición del vendedor si se encuentra
        return -1  # Retorna -1 si no se encuentra el vendedor

    def crear_vendedor(self):
        system("cls")
        print("***************************")
        print("****** CREAR VENDEDOR *****")
        print("***************************")
        id_vendedor = int(input("Ingrese el Id del vendedor: "))

        if id_vendedor in self.id_ingresado_vendedor:
            print("************************************")
            print("Error - El id ingresado ya se encuentra asignado a otro vendedor")
            print("************************************")
            input()
            return False
        
        self.id_ingresado_vendedor.append(id_vendedor)

        nombre_vendedor = input("Ingrese el nombre del vendedor: ")
        telefono_vendedor = input("Ingrese el telefono del vendedor: ")
        direccion_vendedor = input("Ingrese la direccion del vendedor: ")
        edad_vendedor = input("Ingrese la edad del vendedor: ")

        vendedor = Vendedor(id_vendedor, nombre_vendedor, telefono_vendedor, direccion_vendedor, edad_vendedor)

        if self.adicionar_vendedor(vendedor):
            print("***************************")
            print("Info - El vendedor fue adicinado correctamente")
            print("***************************")
            input()

        else:
            print("***************************")
            print("Error - El vendedor no fue adicionado")
            print("***************************")
            input()
    
    def listar_vendedores(self):
        system("cls")
        print("***************************")
        print("**** LISTAR VENDEDORES ****")
        print("***************************")
        self.mostrar_lista_vendedores()
        input() 

    def mostrar_lista_vendedores(self):
        for vendedor in self.vendedores:
            print("***************************")
            vendedor.mostrar_vendedor()

    def modificar_vendedor(self):
        system("cls")
        print("***************************")
        print("**** MODIFICAR VENDEDOR ***")
        print("***************************")
        id = int(input("Ingrese el documento del vendedor que desea modificar: "))

        if self.modificar_vendedores_2(id):
            print("***************************")
            print("Info - El vendedor fue modificado correctamente")
            print("***************************")
            input()
        
        else:
            print("***************************")
            print("Error - El vendedor no fue modificado correctamente")
            print("***************************")
            input()

    def modificar_vendedores_2(self, id):
        pos_ven = self.buscar_vendedor(id)

        if pos_ven != -1:
            if self.vendedores[pos_ven].id_vendedor == id:
                print("***************************")
                print("*** OPCIONES A MODIFICAR ***")
                print("***************************")

                try:
                    print("1: Modificar el nombre del vendedor")
                    print("2: Modificar el telefono del vendedor")
                    print("3: Modificar la direccion del vendedor")
                    print("4: Modificar la edad del vendedor")
                    print("************************************")

                    opcion = int(input("Seleccione la opcion: "))

                    if opcion == 1:
                        nombre = input("Digite el nuevo nombre del vendedor: ")
                        self.vendedores[pos_ven].nombre_vendedor = nombre
                        return True

                    elif opcion == 2:
                        telefono = input("Digite el nuevo telefono del vendedor: ")
                        self.vendedores[pos_ven].telefono_vendedor = telefono
                        return True
                    
                    elif opcion == 3:
                        direccion = input("Digite la nueva direccion del vendedor: ")
                        self.vendedores[pos_ven].direccion_vendedor = direccion
                        return True
                    
                    elif opcion == 4:
                        edad = input("Digite la nueva edad del vendedor: ")
                        self.vendedores[pos_ven].edad_vendedor = edad
                        return True
                    
                    else: 
                        return False
                    
                except ValueError:
                    print("************************************")
                    print("Error - El dato ingresado debe ser entero")
                    print("************************************")
                    input()

            else:
                return False
    
        return False

    def eliminar_vendedor_2(self, id):
        pos_ven = self.buscar_vendedor(id)
        if pos_ven != -1:
            del(self.vendedores[pos_ven])
            return True
        return False

    def eliminar_vendedor(self):
        system("cls")
        print("***************************")
        print("**** ELIMINAR VENDEDOR ****")
        print("***************************")
        id = int(input("Ingrese el id del vendedor que desea eliminar: "))

        if self.eliminar_vendedor_2(id):
            print("***************************")
            print("Info - El vendedor fue eliminado")
            print("***************************")
            input()
        
        else:
            print("***************************")
            print("Error - El vendedor no se puede eliminar")
            print("***************************")
            input()

    def crear_producto(self):
        system("cls")
        print("**** REGISTRAR PRODUCTO ***")
        print("***************************")
        id_producto = int(input("Ingrese el Id del producto: "))

        if id_producto in self.id_ingresado_producto:
            print("************************************")
            print("Error - El id ingresado ya se encuentra asignado a otro producto")
            print("************************************")
            input()
            return False
        
        self.id_ingresado_producto.append(id_producto)

        nombre_producto = input("Ingrese el nombre del producto: ")
        cantidad_producto = int(input("Ingrese la cantidad del producto: "))
        valor_producto = int(input("Ingrese el valor unitario del producto: "))
        
        productos = Productos(id_producto, nombre_producto, cantidad_producto, valor_producto)

        if self.adicionar_producto(productos):
            print("***************************")
            print("Info - El producto fue adicinado correctamente")
            print("***************************")
            input()

        else:
            print("***************************")
            print("Error - El producto no fue adicionado")
            print("***************************")
            input()

    def listar_productos(self):
        system("cls")
        print("***************************")
        print("**** LISTAR PRODUCTOS *****")
        print("***************************")
        self.mostrar_lista_productos()
        input() 

    def mostrar_lista_productos(self):
        for producto in self.productos:
            print("***************************")
            producto.mostrar_producto()
    
    def modificar_producto(self):
        system("cls")
        print("***************************")
        print("**** MODIFICAR PRODUCTO ***")
        print("***************************")
        id = int(input("Ingrese el id del producto que desea modificar: "))

        if self.modificar_productos_2(id):
            print("***************************")
            print("Info - El producto fue modificado correctamente")
            print("***************************")
            input()
        
        else:
            print("***************************")
            print("Error - El producto no fue modificado correctamente")
            print("***************************")
            input()

    def modificar_productos_2(self, id):
        pos_pro = self.buscar_producto(id)

        if pos_pro != -1:
            if self.productos[pos_pro].id_producto == id:
                print("***************************")
                print("*** OPCIONES A MODIFICAR ***")
                print("***************************")

                try:
                    print("1: Modificar el nombre del producto")
                    print("2: Modificar la cantidad del producto")
                    print("3: Modificar valor unitario del producto")
                    print("************************************")

                    opcion = int(input("Seleccione la opcion: "))

                    if opcion == 1:
                        nombre = input("Digite el nuevo nombre del producto: ")
                        self.productos[pos_pro].nombre_producto = nombre
                        return True

                    elif opcion == 2:
                        cantidad = input("Digite la nueva cantidad del producto: ")
                        self.productos[pos_pro].cantidad_producto = cantidad
                        return True
                    
                    elif opcion == 3:
                        valor = input("Digite el nuevo valor del producto: ")
                        self.productos[pos_pro].valor_producto = valor
                        return True               
                    
                    else: 
                        return False
                    
                except ValueError:
                    print("************************************")
                    print("Error - El dato ingresado debe ser entero")
                    print("************************************")
                    input()

            else:
                return False
    
        return False
    
    def eliminar_producto_2(self, id):
        pos_pro = self.buscar_producto(id)
        if pos_pro != -1:
            del(self.productos[pos_pro])
            return True
        return False

    def eliminar_producto(self):
        system("cls")
        print("***************************")
        print("**** ELIMINAR PRODUCTO ****")
        print("***************************")
        id = int(input("Ingrese el id del producto que desea eliminar: "))

        if self.eliminar_producto_2(id):
            print("***************************")
            print("Info - El producto fue eliminado")
            print("***************************")
            input()
        
        else:
            print("***************************")
            print("Error - El producto no se puede eliminar")
            print("***************************")
            input()

    def registrar_venta(self):
        system("cls")
        print("***************************")
        print("***** ADICIONAR VENTA ****")
        print("***************************")
        id = int(input("Ingrese el id de la venta: "))

        if self.buscar_venta(id) != -1:
            print("***************************")
            print("Error - la venta no se pudo agregar")
            print("***************************")
            input()
            return False
        
        if id in self.id_ingresado_venta:
            print("************************************")
            print("Error - El id ingresado ya se encuentra asignado a otra venta")
            print("************************************")
            input()
            return False
        
        self.id_ingresado_venta.append(id)
        
        dia = int(input("Ingrese el dia: "))
        mes = int(input("Ingrese el mes: "))
        año = int(input("Ingrese el año: "))

        fecha = "{}/{}/{}".format(dia, mes, año)

        try:

            fecha_completa = datetime.strptime(fecha, "%d/%m/%Y")

            id_producto = int(input("Ingrese el id del producto: "))
            id_vendedor = int(input("Ingrese el id del vendedor: "))

            if (self.buscar_producto(id_producto) == -1 and self.buscar_vendedor(id_vendedor) == -1):
                print("***************************")
                print("Error - la venta no se pudo agregar")
                print("***************************")
                input()
                return False
            
            cantidad = int(input("Ingrese la cantidad: "))

            pos_produ = self.buscar_producto(id_producto)

            if (cantidad > self.productos[pos_produ].cantidad_producto):
                print("***************************")
                print("Error - No hay suficiente cantidad de productos")
                print("***************************")
                input()
                return False
            
            total = cantidad*self.productos[pos_produ].valor_producto

            self.productos[pos_produ].cantidad_producto =  self.productos[pos_produ].cantidad_producto - cantidad

            venta = Venta (id, fecha, id_producto, cantidad, id_vendedor, total)
            self.ventas.append(venta)
            
            print("***************************")
            print("Info - La venta se agrego")
            print("***************************")
            input()

        except:
            print("***************************")
            print("Error - No se pudo agregar la venta ")
            print("***************************")
            input()

    def modificar_venta(self):
        system("cls")
        print("***************************")
        print("***** MODIFICAR VENTA *****")
        print("***************************")
        id = int(input("Ingrese el id de la venta que desea modificar: "))

        if (self.modificar_venta_2(id)):
            print("***************************")
            print("Info - La venta fue modificado correctamente")
            print("***************************")
            input()

    def modificar_venta_2(self, id):
        pos_ven = self.buscar_venta(id)

        if pos_ven != -1:
            if self.ventas[pos_ven].id_venta == id:
                print("***************************")
                print("*** OPCIONES A MODIFICAR ***")
                print("***************************")
                print("1: Fecha")
                print("2: Id producto")
                print("3: Cantidad")
                print("4: Id vendedor")

            try:

                opt = int(input("Digite la opcion: "))

                if opt == 1:
                    dia = int(input("Ingrese el dia: "))
                    mes = int(input("Ingrese el mes: "))
                    año = int(input("Ingrese el año: "))

                    fecha = "{}/{}/{}".format(dia, mes, año)
                    input()
                    fecha_completa = datetime.strptime(fecha, "%d/%m/%Y")
                    self.ventas[pos_ven].fecha = fecha

                elif opt == 2:
                    id_producto=int(input("Ingrese el nuevo Id del producto: "))

                    if (self.buscar_producto(id_producto) == -1):
                        print("***************************")
                        print("Error - El Id del producto no exite")
                        print("***************************")
                        input()
                        return False
                    
                    self.ventas[pos_ven].id_producto = id_producto

                elif opt == 3:
                    id_producto = self.ventas[pos_ven].id_producto
                    pos_pro = self.buscar_producto(id_producto)

                    cantidad_disponible = self.productos[pos_pro].cantidad_producto + self.ventas[pos_ven].cantidad

                    cantidad_nueva = int(input("Ingrese la nueva cantidad: "))

                    if cantidad_nueva > cantidad_disponible:
                        print("***************************")
                        print("Error - No hay productos disponibles")
                        print("***************************")
                        input()
                        return False
                    
                    print("***************************")
                    print("Info - Se realizo el cambio correcta mente")
                    print("***************************")
                    input()

                    self.productos[pos_pro].cantidad_producto = cantidad_nueva
                    self.ventas[pos_ven].cantidad = cantidad_nueva
                    self.ventas[pos_ven].total = cantidad_nueva * self.productos[pos_pro].valor_producto
                    input()

                elif opt == 4:
                    id_vendedor=int(input("Ingrese el nuevo Id del vendedor: "))

                    if (self.buscar_vendedor(id_vendedor) == -1):
                        print("***************************")
                        print("Error - El Id del vendedor no exite")
                        print("***************************")
                        input()
                        return False
                    
                    self.ventas[pos_ven].id_vendedor = id_vendedor

            except:
                print("***************************")
                print("Error - No se pudo modificar venta")
                print("***************************")
                input()   

    def mostrar_ventas(self):
        id = int(input("Ingrese el Id del producto: "))

        if(self.buscar_producto(id) == -1):
            print("***************************")
            print("Error - El producto no exite")
            print("***************************")
            input()
            return False
        self.mostrar_ventas_2(id)
        
    def mostrar_ventas_2(self, id):
        total = 0

        for i in range(0,len(self.ventas)):
            print("***************************")
            if self.ventas[i].id_producto == id:
                total += self.ventas[i].total
                self.ventas[i].mostrar_venta()

        print("Total de todas las ventas: ", total)        
        input()

    def mostrar_ventas_fecha(self):

        try:

            dia = int(input("Ingrese el dia: "))
            mes = int(input("Ingrese el mes: "))
            año = int(input("Ingrese el año: "))

            fecha = "{}/{}/{}".format(dia, mes, año)
            fecha_completa = datetime.strptime(fecha, "%d/%m/%Y")

            for i in range(0, len(self.ventas)):
                print("***************************")
                if self.ventas[i].fecha == fecha:
                    self.ventas[i].mostrar_venta()
            input()

        except:
            print("***************************")
            print("Error - La fecha no existe")
            print("***************************")
            input()

    def mostrar_ventas_vendedor(self):
        id = int(input("Ingrese el Id del vendedor: "))

        if(self.buscar_vendedor(id) == -1):
            print("***************************")
            print("Error - El vendedor no exite")
            print("***************************")
            input()
            return False
        self.mostrar_ventas_vendedor_2(id)
        
    def mostrar_ventas_vendedor_2(self, id):
        total = 0

        for i in range(0,len(self.ventas)):
            print("***************************")
            if self.ventas[i].id_vendedor == id:
                total += self.ventas[i].total
                self.ventas[i].mostrar_venta()

        print("Total de todas las ventas: ", total)        
        input()