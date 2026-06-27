# tfi.py
# Punto de entrada de la aplicacion. Contiene unicamente la funcion main().
# Alumno: Hernan Perez Melgar - Comision C26108 - TalentoTech 2026

import os
import mod_backend as be
import mod_frontend as fe


def main():
    """Funcion principal. Inicializa la DB y ejecuta el bucle del menu."""

    # Evita problemas de rutas al abrir la base de datos
    os.chdir(os.path.dirname(__file__))

    # Configuracion de la base de datos
    archivo_db_nombre = 'inventario.db'
    tabla_nombre = 'productos'

    create_table_sql = f'''
CREATE TABLE IF NOT EXISTS "{tabla_nombre}" (
    "id"          INTEGER NOT NULL UNIQUE,
    "nombre"      TEXT    NOT NULL CHECK((trim("nombre") <> '' AND trim("nombre") GLOB '[A-Za-z0-9]*') AND length("nombre") <= 30),
    "descripcion" TEXT,
    "cantidad"    INTEGER NOT NULL CHECK(("cantidad" >= 0)),
    "precio"      REAL    NOT NULL CHECK(("precio" > 0)),
    "categoria"   TEXT,
    PRIMARY KEY("id" AUTOINCREMENT)
) STRICT;'''

    # Inicializa la base de datos
    be.inicializa_db(archivo_db_nombre, create_table_sql)

    # Bucle principal
    while True:
        fe.limpiar_pantalla()
        opcion = fe.menu()

        match opcion:

            case '1': # AGREGAR (Create)
                datos = fe.pedir_datos_producto()
                if datos is not None:
                    nombre, descripcion, cantidad, precio, categoria = datos
                    be.agregar_producto(archivo_db_nombre, tabla_nombre, nombre, descripcion, cantidad, precio, categoria)

            case '2': # VISUALIZAR (Read)
                productos = be.obtener_productos(archivo_db_nombre, tabla_nombre)
                fe.mostrar_tabla(productos)

            case '3': # ACTUALIZAR (Update)
                id_producto = fe.pedir_id('Ingrese el ID del producto a actualizar: ')
                producto_actual = be.obtener_producto_por_id(archivo_db_nombre, tabla_nombre, id_producto)
                if producto_actual is None:
                    print('No existe un producto con ese ID.')
                else:
                    datos_nuevos = fe.pedir_datos_actualizacion(producto_actual)
                    if datos_nuevos is not None:
                        nombre, descripcion, cantidad, precio, categoria = datos_nuevos
                        be.actualizar_producto(archivo_db_nombre, tabla_nombre, id_producto, nombre, descripcion, cantidad, precio, categoria)

            case '4': # ELIMINAR (Delete)
                id_producto = fe.pedir_id('Ingrese el ID del producto a eliminar: ')
                producto = be.obtener_producto_por_id(archivo_db_nombre, tabla_nombre, id_producto)
                if producto is None:
                    print('No existe un producto con ese ID.')
                else:
                    fe.mostrar_producto(producto)
                    confirmacion = input('Confirma la eliminacion? (s/n): ').strip().lower()
                    if confirmacion == 's':
                        be.eliminar_producto(archivo_db_nombre, tabla_nombre, id_producto)
                    else:
                        print('Operacion cancelada.')

            case '5': # BUSCAR
                subopcion = fe.menu_busqueda()
                match subopcion:
                    case '1':
                        id_producto = fe.pedir_id('Ingrese el ID a buscar: ')
                        producto = be.obtener_producto_por_id(archivo_db_nombre, tabla_nombre, id_producto)
                        if producto is None:
                            print('No existe un producto con ese ID.')
                        else:
                            fe.mostrar_producto(producto)
                    case '2':
                        termino = input('Ingrese el nombre a buscar: ').strip()
                        if termino:
                            resultados = be.buscar_productos(archivo_db_nombre, tabla_nombre, 'nombre', termino)
                            fe.mostrar_tabla(resultados)
                    case '3':
                        termino = input('Ingrese la categoria a buscar: ').strip()
                        if termino:
                            resultados = be.buscar_productos(archivo_db_nombre, tabla_nombre, 'categoria', termino)
                            fe.mostrar_tabla(resultados)
                    case _:
                        print('Opcion invalida.')

            case '6': # REPORTE DE STOCK BAJO
                limite = fe.valida_entero_positivo('Ingrese el limite de cantidad para el reporte: ')
                resultados = be.reporte_stock_bajo(archivo_db_nombre, tabla_nombre, limite)
                print(f'\nProductos con stock igual o inferior a {limite}:')
                fe.mostrar_tabla(resultados)

            case '0': # SALIR
                print('Gracias por utilizar el programa, dasarrollado en TalentoTech. saliendo...')
                fe.pausa()
                break

            case _: # OPCION INVALIDA
                print('Opcion invalida. Elija un numero del 0 al 6.')

        fe.pausa()


if __name__ == '__main__':
    main()
