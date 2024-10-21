productos = []

def añadir_producto():
    nombre = input("Introduce el nombre del producto: ")
    while True:
        try:
            precio = int(input("Introduce el precio del producto: "))
            cantidad = int(input("Introduce la cantidad disponible del producto: "))
            break
        except ValueError:
            print("Error: Debes introducir valores numéricos para el precio y la cantidad.")
    productos.append({
        'nombre': nombre,
        'precio': precio,
        'cantidad': cantidad
    })
    print(f"Producto '{nombre}' añadido correctamente.")

def ver_productos():
    print("\nLista de productos:")
    for i, producto in enumerate(productos, 1):
        print(f"{i}. {producto['nombre']} - Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
    print()

def actualizar_producto():
    ver_productos()
    nombre_producto = input("Introduce el nombre del producto que quieres actualizar: ")
    for producto in productos:
        if producto['nombre'] == nombre_producto:
            nuevo_nombre = input(f"Introduce el nuevo nombre (o presiona Enter para mantener '{nombre_producto}'): ")
            if nuevo_nombre:
                producto['nombre'] = nuevo_nombre
            while True:
                try:
                    nuevo_precio = input(f"Introduce el nuevo precio (o presiona Enter para mantener '{producto['precio']}'): ")
                    if nuevo_precio:
                        producto['precio'] = float(nuevo_precio)
                    nueva_cantidad = input(f"Introduce la nueva cantidad (o presiona Enter para mantener '{producto['cantidad']}'): ")
                    if nueva_cantidad:
                        producto['cantidad'] = int(nueva_cantidad)
                    print(f"Producto '{nombre_producto}' actualizado correctamente.")
                    break
                except ValueError:
                    print("Error: Debes introducir valores numéricos.")
            return
    print(f"Producto '{nombre_producto}' no encontrado.")

def eliminar_producto():
    ver_productos()
    nombre_producto = input("Introduce el nombre del producto que deseas eliminar: ")
    for producto in productos:
        if producto['nombre'] == nombre_producto:
            productos.remove(producto)
            print(f"Producto '{nombre_producto}' eliminado correctamente.")
            return
    print(f"Producto '{nombre_producto}' no encontrado.")

def guardar_datos():
    with open("productos.txt", "w") as archivo:
        for producto in productos:
            archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
    print("Datos guardados correctamente.")

def cargar_datos():
    try:
        with open("productos.txt", "r") as archivo:
            for linea in archivo:
                nombre, precio, cantidad = linea.strip().split(',')
                productos.append({
                    'nombre': nombre,
                    'precio': float(precio),
                    'cantidad': int(cantidad)
                })
        print("Datos cargados correctamente.")
    except FileNotFoundError:
        print("Archivo de productos no encontrado, iniciando con lista vacía.")

def menu():
    cargar_datos()  # Cargar los productos al inicio
    while True:
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            break
        else:
            print("Por favor, selecciona una opción válida.")

menu()
