# Sistema de Gestión de Inventario de Productos

**Trabajo Final Integrador — TalentoTech 2026**

| Campo | Detalle |
|---|---|
| Alumno | Hernán Pérez Melgar |
| DNI | 26145643 |
| Comisión | C26108 |
| Profesor | Leandro Fazio |

---

## Descripción

Aplicación de consola desarrollada en Python para la gestión de un inventario de productos. Permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre una base de datos SQLite local, con validaciones y manejo de errores.

---

## Requisitos

- Python 3.10 o superior
- No requiere instalación de librerías externas

Módulos utilizados: `sqlite3`, `os` (biblioteca estándar de Python)

---

## Estructura de archivos

```
├── tfi.py           # Punto de entrada. Contiene la función main()
├── mod_backend.py   # Conexión a la DB y operaciones CRUD
├── mod_frontend.py  # Interfaz de usuario, menús y visualización
├── inventario.db    # Base de datos SQLite (se crea al ejecutar)
└── README.md        # Este archivo
```

---

## Cómo ejecutar

1. Abrir una terminal en la carpeta del proyecto.
2. Ejecutar el siguiente comando:

```bash
python tfi.py
```

3. Navegar por el menú usando los números indicados.

---

## Funcionalidades

| Opción | Función | Descripción |
|---|---|---|
| `1` | Agregar producto | Registra un nuevo producto en la DB |
| `2` | Visualizar | Muestra todos los productos en tabla |
| `3` | Actualizar | Modifica los datos de un producto por ID |
| `4` | Eliminar | Borra un producto por ID con confirmación |
| `5` | Buscar | Busca por ID, nombre o categoría |
| `6` | Reporte stock bajo | Lista productos con cantidad ≤ límite |
| `0` | Salir | Cierra la aplicación |

---

## Base de datos

- **Archivo:** `inventario.db`
- **Tabla:** `productos`

| Campo | Tipo | Descripción |
|---|---|---|
| `id` | INTEGER | Clave primaria, autoincremental |
| `nombre` | TEXT | Obligatorio. Solo letras y números, máx. 30 caracteres |
| `descripcion` | TEXT | Opcional |
| `cantidad` | INTEGER | Obligatorio. Valor ≥ 0 |
| `precio` | REAL | Obligatorio. Valor > 0 |
| `categoria` | TEXT | Opcional |

---

## Seguridad

- Todas las consultas SQL usan parametrización con `?` para prevenir inyección SQL.
- Las validaciones de datos se implementan mediante constraints en la definición de la tabla (cláusula `CHECK`).
- Los errores de base de datos se capturan con excepciones `sqlite3.IntegrityError` y `sqlite3.Error`.
