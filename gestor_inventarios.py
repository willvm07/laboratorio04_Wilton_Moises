class Producto():
    def __init__(self, pcodigo, pnombre, pprecio, pexistencias, pproveedor):
        self.codigo = pcodigo
        self.nombre = pnombre
        self.precio = pprecio
        self.existencias = pexistencias
        self.proveedor = pproveedor

lstProductos = []
lstprovedores = []
def agregarProductos(Producto):
    while True:
        codProvedor = int(input("Ingrese el codigo de provedor: "))
        nomProvedor = input("Ingrese el nombre del proveedor: ")
        paisProvedor = input("Ingrese el pais del proveedor: ")
        provedores = {
            "Codigo": codProvedor,
            "Nombre": nomProvedor,
            "Pais": paisProvedor
        }
        lstprovedores.append(provedores)
        opcion  = input("Desea agregar otro proveedor")
        if opcion.lower()!= "s":
            break
    while True:
        codigo = input("Ingrese el codigo del producto: ")
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        existencias = int(input("Ingrese las existencias del producto: "))
        for i, provedor in enumerate(lstprovedores):
            print(f"{i+1}. {provedor['Nombre']} - Pais: {provedor['Pais']}")
        provedor_index = int(input("Digite el numero del provedor a elegir: ")) - 1
        provedor = lstprovedores[provedor_index]

        Producto(codigo, nombre, precio, existencias, provedor)
        lstProductos.append(Producto)
        print(lstProductos) 
        opcion = input("Desea agregar otro producto: ")
        if opcion.lower()!= "s":
            break
def eliminarProducto():
    print(lstProductos)
    eliminar = int(input("Ingrese el codigo del proucto a eliminar: "))
    del eliminar
    print("Producto eliminado exitosamente")

def actualizarPrecio():
    print(lstProductos)
    codigo = input("Ingrese el codigo del producto a actualizar: ")
    for producto in lstProductos:
        if producto.codigo == codigo:
            precio = float(input("Ingrese el nuevo precio del producto: "))
            producto.precio = precio
            print("Precio actualizado exitosamente")
    return Menu_principal
def listarProductos(): 
    print("Listado de productos:")
    for indice, producto in enumerate(lstProductos):
        print(f"{indice+1}. {producto.nombre} - Precio: {producto.precio} - Existencias: {producto.existencias}")
    return Menu_principal

def buscarProducto():
    buscar = int(input("Ingrese el codigo del producto a buscar: "))
    for producto in lstProductos:
        if producto.codigo == buscar:
            print(f"Producto encontrado: {producto.nombre} - Precio: {producto.precio} - Existencias: {producto.existencias}")
    return Menu_principal

def guardar_inventario_archivo():
    with open("inventario.txt", "w") as file:
        for producto in lstProductos:
            file.write(f"{producto.codigo},{producto.nombre},{producto.precio},{producto.existencias},{producto.proveedor}\n")
    print("Inventario guardado exitosamente en el archivo inventario.txt")
    return Menu_principal
def cargar_inventario_archivo():
    with open("inventario.txt", "r") as file:
        for linea in file:
            datos = linea.strip().split(",")
            codigo = datos[0]
            nombre = datos[1]
            precio = float(datos[2])
            existencias = int(datos[3])
            proveedor = int(datos[4])
            Producto(codigo, nombre, precio, existencias, proveedor)
    print("Inventario cargado exitosamente desde el archivo inventario.txt")
    return Menu_principal

def Menu_principal():
    print("Bienvenido al Gestor de Inventario")
    while True:
        print("1. agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar precio de producto")
        print("4. Listar productos")
        print("5. Buscar productos")
        print("6. Guardar inventario en archivo")
        print("7. cargar inventario desde archivo")
        print("8. Salir")
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            agregarProductos(Producto)
        elif opcion == 2:
            eliminarProducto()
        elif opcion == 3:
            actualizarPrecio()
        elif opcion == 4:
            listarProductos()
        elif opcion == 5:
            buscarProducto()
        elif opcion == 6:
            guardar_inventario_archivo()
        elif opcion == 7:
            cargar_inventario_archivo()
        elif opcion == 8:
            break

if __name__ == "__main__":
    Menu_principal()
