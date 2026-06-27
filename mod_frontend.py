# mod_frontend.py
# Modulo de frontend: interfaz de usuario, menus y visualizacion de datos.
# Alumno: Hernan Perez Melgar - Comision C26108 - TalentoTech 2026

import os


def limpiar_pantalla():
    """Limpia la pantalla de la terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')
    return None


def pausa():
    """Pausa la ejecucion hasta que el usuario presione Enter."""
    input('Presione Enter para continuar!')
    return None


def menu():
    """Muestra el menu principal y retorna la opcion elegida."""
    print('=== Sistema de Gestion de Inventario ===')
    print('1. Agregar producto')
    print('2. Visualizar productos')
    print('3. Actualizar producto')
    print('4. Eliminar producto')
    print('5. Buscar producto')
    print('6. Reporte de stock bajo')
    print('0. Salir')
    opcion = input('\nIngrese una opcion: ').strip()
    return opcion


def valida_entero_positivo(mensaje):
    """Pide un numero entero positivo al usuario y lo retorna validado."""
    while True:
        valor = input(mensaje).strip()
        if valor.isdigit() and int(valor) > 0:
            return int(valor)
        print('Ingrese un numero entero positivo valido.')


def mostrar_tabla(productos):
    """Muestra una lista de productos en formato tabla."""
    if not productos:
        print('No se encontraron productos.')
        return None
    ancho = 85
    print('\n' + '-' * ancho)
    print(f" {'ID':<4}| {'Nombre':<15}| {'Descripcion':<20}| {'Cantidad':<10}| {'Precio':<10}| {'Categoria':<15}")
    print('-' * ancho)
    for p in productos:
        print(f" {p[0]:<4}| {str(p[1]):<15}| {str(p[2]):<20}| {p[3]:<10}| ${p[4]:<10.2f}| {str(p[5]):<15}")
    print('-' * ancho)
    return None


def pedir_datos_producto():
    """Solicita al usuario los datos para agregar un nuevo producto."""
    print('\n-- Agregar producto --')
    nombre = input('Nombre (obligatorio, solo letras y numeros, max 30 caracteres): ').strip()
    descripcion = input('Descripcion (opcional, Enter para omitir): ').strip()
    cantidad = valida_entero_positivo('Cantidad (entero positivo): ')
    precio_str = input('Precio (mayor a 0, usar coma para decimales. Ej: 4000,50): ').strip()
    try:
        precio = float(precio_str.replace(',', '.'))
        if precio <= 0:
            raise ValueError
    except ValueError:
        print('Precio invalido. Operacion cancelada.')
        return None
    categoria = input('Categoria (opcional, Enter para omitir): ').strip()
    return nombre, descripcion, cantidad, precio, categoria


def pedir_id(mensaje='Ingrese el ID del producto: '):
    """Solicita y retorna un ID valido al usuario."""
    return valida_entero_positivo(mensaje)


def mostrar_producto(producto):
    """Muestra los datos de un producto individual en formato tabla."""
    mostrar_tabla([producto])
    return None


def pedir_datos_actualizacion(producto_actual):
    """
    Muestra el producto actual y pide los nuevos valores campo por campo.
    Si el usuario presiona Enter sin ingresar nada, conserva el valor actual.
    """
    print('\nProducto actual:')
    mostrar_tabla([producto_actual])
    print('\nIngrese los nuevos valores (Enter para conservar el valor actual):\n')

    nombre_nuevo = input(f'Nombre [{producto_actual[1]}]: ').strip()
    if nombre_nuevo == '':
        nombre_nuevo = producto_actual[1]

    descripcion_nueva = input(f'Descripcion [{producto_actual[2]}]: ').strip()
    if descripcion_nueva == '':
        descripcion_nueva = producto_actual[2]

    cantidad_str = input(f'Cantidad [{producto_actual[3]}]: ').strip()
    if cantidad_str == '':
        cantidad_nueva = producto_actual[3]
    elif cantidad_str.isdigit() and int(cantidad_str) >= 0:
        cantidad_nueva = int(cantidad_str)
    else:
        print('Cantidad invalida. Operacion cancelada.')
        return None

    precio_str = input(f'Precio [{producto_actual[4]}] (usar coma para decimales. Ej: 4000,50): ').strip()
    if precio_str == '':
        precio_nuevo = producto_actual[4]
    else:
        try:
            precio_nuevo = float(precio_str.replace(',', '.'))
            if precio_nuevo <= 0:
                raise ValueError
        except ValueError:
            print('Precio invalido. Operacion cancelada.')
            return None

    categoria_nueva = input(f'Categoria [{producto_actual[5]}]: ').strip()
    if categoria_nueva == '':
        categoria_nueva = producto_actual[5]

    return nombre_nuevo, descripcion_nueva, cantidad_nueva, precio_nuevo, categoria_nueva


def menu_busqueda():
    """Muestra el submenu de busqueda y retorna la opcion elegida."""
    print('\n-- Buscar producto --')
    print('1. Buscar por ID')
    print('2. Buscar por nombre')
    print('3. Buscar por categoria')
    opcion = input('Ingrese una opcion: ').strip()
    return opcion
