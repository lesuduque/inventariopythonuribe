# MENU DE OPCIONES
# 1. Ingresar producto en bodega
# 2. Verificar los productos en bodega
# 3. Buscar un productos en bodega
# 4. Editar un producto en bodega
# 5. Retirar un producto en bodega
# 6. SALIR

# producto: nombre, codigo, descripción, foto, precio, cantidadEnBodega,fechaEntradaBodega

opcion = 0
print("TIENDA EL GANGAZO DEL")
print("*********************")
print("1. Ingresar producto en bodega")
print("2. Verificar los productos en bodega")
print("3. Buscar un productos en bodega")
print("4. Editar un producto en bodega")
print("5. Retirar un producto en bodega")
print("6. SALIR")
print("*********************")

productos = []

while opcion != 6:
    producto = {}
    opcion = int(input("Digita la opción deseada: "))

    if opcion == 1:
        producto["codigo"] = int(input("Digita la referencia del producto: "))
        producto["nombre"] = input("Digita el nombre del producto: ")
        producto["descripcion"] = input("Digita la descripcion del producto: ")
        producto["foto"] = input("Ingresa la url de la fotografía del producto: ")
        producto["precio"] = float(input("Digita el precio del producto: "))
        producto["stock"] = int(input("Digita el stock del producto: "))
        producto["fechaIngreso"] = input("Digita la fecha de ingreso del producto: ")
        productos.append(producto)
    elif opcion == 2:
        for productoSeleccionado in productos:
            print(f"codigo: {productoSeleccionado ['codigo']}")
            print(f"nombre: {productoSeleccionado ['nombre']}")
            print(f"descripcion: {productoSeleccionado ['descripcion']}")
            print(f"foto: {productoSeleccionado ['foto']}")
            print(f"precio: {productoSeleccionado ['precio']}")
            print(f"stock: {productoSeleccionado ['stock']}")
            print(f"fechaIngreso: {productoSeleccionado ['fechaIngreso']} \n")
    elif opcion == 3:
        #hacer un for para recorrer la lista
        '''https://www.delftstack.com/es/howto/python/python-loop-through-list/#google_vignette'''
        pass
    elif opcion == 4:
        pass
    elif opcion == 5:
        pass
    elif opcion == 6:
        pass
    else:
        print("Opción inválida, vuelva a intentar")
