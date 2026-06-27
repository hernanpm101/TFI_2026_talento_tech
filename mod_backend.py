# mod_backend.py
# Modulo de backend: conexion a la base de datos y operaciones CRUD.
# Alumno: Hernan Perez Melgar - Comision C26108 - TalentoTech 2026

import sqlite3


def inicializa_db(archivo_db_nombre, create_table_sql):
    """Crea la base de datos y la tabla si no existen."""
    with sqlite3.connect(archivo_db_nombre) as con:
        try:
            con.execute(create_table_sql)
            con.commit()
        except sqlite3.Error:
            print('Error de base de datos.')
            exit()


def agregar_producto(archivo_db_nombre, tabla_nombre, nombre, descripcion, cantidad, precio, categoria):
    """Inserta un nuevo producto en la base de datos."""
    sql = f'INSERT INTO {tabla_nombre} (nombre, descripcion, cantidad, precio, categoria) VALUES (?, ?, ?, ?, ?)'
    with sqlite3.connect(archivo_db_nombre) as con:
        try:
            con.execute(sql, (nombre, descripcion, cantidad, precio, categoria))
            con.commit()
            print('Producto agregado correctamente.')
        except sqlite3.IntegrityError:
            print('Error: datos invalidos. Revise que el nombre no este vacio, que la cantidad sea >= 0 y el precio > 0.')
        except sqlite3.Error:
            print('Error de base de datos.')
            exit()


def obtener_productos(archivo_db_nombre, tabla_nombre):
    """Retorna todos los productos de la tabla."""
    sql = f'SELECT * FROM {tabla_nombre}'
    with sqlite3.connect(archivo_db_nombre) as con:
        try:
            cursor = con.execute(sql)
            return cursor.fetchall()
        except sqlite3.Error:
            print('Error de base de datos.')
            exit()


def obtener_producto_por_id(archivo_db_nombre, tabla_nombre, id_producto):
    """Retorna un producto por su ID, o None si no existe."""
    sql = f'SELECT * FROM {tabla_nombre} WHERE id == ?'
    with sqlite3.connect(archivo_db_nombre) as con:
        try:
            cursor = con.execute(sql, (id_producto,))
            return cursor.fetchone()
        except sqlite3.Error:
            print('Error de base de datos.')
            exit()


def buscar_productos(archivo_db_nombre, tabla_nombre, campo, termino):
    """Busca productos por nombre o categoria usando LIKE."""
    sql = f'SELECT * FROM {tabla_nombre} WHERE {campo} LIKE ?'
    with sqlite3.connect(archivo_db_nombre) as con:
        try:
            cursor = con.execute(sql, (f'%{termino}%',))
            return cursor.fetchall()
        except sqlite3.Error:
            print('Error de base de datos.')
            exit()


def actualizar_producto(archivo_db_nombre, tabla_nombre, id_producto, nombre, descripcion, cantidad, precio, categoria):
    """Actualiza los campos de un producto existente por su ID."""
    sql = f'UPDATE {tabla_nombre} SET nombre = ?, descripcion = ?, cantidad = ?, precio = ?, categoria = ? WHERE id == ?'
    with sqlite3.connect(archivo_db_nombre) as con:
        try:
            con.execute(sql, (nombre, descripcion, cantidad, precio, categoria, id_producto))
            con.commit()
            print('Producto actualizado correctamente.')
        except sqlite3.IntegrityError:
            print('Error: datos invalidos. Revise que el nombre no este vacio, que la cantidad sea >= 0 y el precio > 0.')
        except sqlite3.Error:
            print('Error de base de datos.')
            exit()


def eliminar_producto(archivo_db_nombre, tabla_nombre, id_producto):
    """Elimina un producto por su ID."""
    sql = f'DELETE FROM {tabla_nombre} WHERE id == ?'
    with sqlite3.connect(archivo_db_nombre) as con:
        try:
            cursor = con.execute(sql, (id_producto,))
            con.commit()
            if cursor.rowcount == 0:
                print('No existe un producto con ese ID.')
            else:
                print('Producto eliminado correctamente.')
        except sqlite3.Error:
            print('Error de base de datos.')
            exit()


def reporte_stock_bajo(archivo_db_nombre, tabla_nombre, limite):
    """Retorna productos con cantidad igual o inferior al limite indicado."""
    sql = f'SELECT * FROM {tabla_nombre} WHERE cantidad <= ?'
    with sqlite3.connect(archivo_db_nombre) as con:
        try:
            cursor = con.execute(sql, (limite,))
            return cursor.fetchall()
        except sqlite3.Error:
            print('Error de base de datos.')
            exit()
