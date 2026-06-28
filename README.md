README.txt

Sistema de Gestion de Inventario de Productos
Trabajo Final Integrador - TalentoTech 2026
Alumno: Hernan Perez Melgar
DNI: 26145643
Comision: C26108
Profesor: Leandro Fazio

================================================================
DESCRIPCION
================================================================
Aplicacion de consola desarrollada en Python para la gestion
de un inventario de productos. Permite realizar operaciones
CRUD (Crear, Leer, Actualizar, Eliminar) sobre una base de
datos SQLite local, con validaciones y manejo de errores.

================================================================
REQUISITOS
================================================================
- Python 3.10 o superior
- No requiere instalacion de librerias externas.
  Modulos utilizados: sqlite3, os (biblioteca estandar de Python)

================================================================
ESTRUCTURA DE ARCHIVOS
================================================================
tfi.py          -> Punto de entrada. Contiene la funcion main().
mod_backend.py  -> Conexion a la DB y operaciones CRUD.
mod_frontend.py -> Interfaz de usuario, menus y visualizacion.
inventario.db   -> Base de datos SQLite (se crea al ejecutar).
README.txt      -> Este archivo.

================================================================
COMO EJECUTAR
================================================================
1. Abrir una terminal en la carpeta del proyecto.
2. Ejecutar el siguiente comando:

   python tfi.py

3. Navegar por el menu usando los numeros indicados.

================================================================
FUNCIONALIDADES
================================================================
1. Agregar producto    -> Registra un nuevo producto en la DB.
2. Visualizar          -> Muestra todos los productos en tabla.
3. Actualizar          -> Modifica los datos de un producto por ID.
4. Eliminar            -> Borra un producto por ID con confirmacion.
5. Buscar              -> Busca por ID, nombre o categoria.
6. Reporte stock bajo  -> Lista productos con cantidad <= limite.
0. Salir               -> Cierra la aplicacion.

================================================================
BASE DE DATOS
================================================================
Archivo : inventario.db
Tabla   : productos
Campos  :
  id          INTEGER  Clave primaria, autoincremental.
  nombre      TEXT     Obligatorio. Solo letras y numeros, max 30 caracteres.
  descripcion TEXT     Opcional.
  cantidad    INTEGER  Obligatorio. Valor >= 0.
  precio      REAL     Obligatorio. Valor > 0.
  categoria   TEXT     Opcional.

================================================================
SEGURIDAD
================================================================
- Todas las consultas SQL usan parametrizacion con ? para
  prevenir inyeccion SQL.
- Las validaciones de datos se implementan mediante constraints
  en la definicion de la tabla (clausula CHECK).
- Los errores de base de datos se capturan con excepciones
  sqlite3.IntegrityError y sqlite3.Error.

================================================================

