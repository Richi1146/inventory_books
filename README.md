# 📚 Sistema de Gestión de Biblioteca

Un sistema de consola en Python diseñado para registrar, prestar, devolver, eliminar y buscar libros. Perfecto para bibliotecas pequeñas o como proyecto educativo.

---

## 🧠 Descripción

Este sistema permite manejar el inventario de libros mediante una interfaz de línea de comandos. Cada libro cuenta con información clave como título, autor, año, categoría y estado (disponible o prestado).

---

## 🚀 Características

✅ Registro de nuevos libros  
✅ Búsqueda por título, autor o categoría  
✅ Listado completo y filtrado de libros (disponibles o prestados)  
✅ Préstamo de libros con control de límite por persona  
✅ Devolución de libros  
✅ Eliminación de libros disponibles  
✅ Validaciones amigables al usuario

---

## 🛠️ Tecnologías

- **Lenguaje**: Python 3.10+
- **Paradigma**: Programación estructurada
- **Interfaz**: Consola

---

## 🗂️ Estructura del Proyecto

📦 book_manager/
├── main.py # Menú principal
├── register_book.py # Registro de libros
├── lend_book.py # Préstamos
├── return_book.py # Devoluciones
├── delete_book.py # Eliminaciones
├── list_books.py # Listado y filtrado
├── search_books.py # Búsqueda
├── menu_search.py # Lista de libros compartida
└── README.md # Documentación

yaml
Copiar
Editar

---

## 📋 Menú Principal

```text
1. Registrar libros
2. Listar libros
3. Buscar libros
4. Prestar un libro
5. Devolver un libro
6. Eliminar un libro
7. Salir
🧾 Detalles de Funcionalidades
📥 Registrar libros
Ingreso manual de título, autor, año, categoría e ID.

Estado inicial: available.

📋 Listar libros
Ver todos los libros.

Filtros: disponibles (available) o prestados (borrowed).

En prestados, se muestra nombre del prestatario y fecha de préstamo.

🔍 Buscar libros
Por coincidencia parcial en:

Título

Autor

Categoría

📤 Prestar libros
Se verifica disponibilidad del libro.

Control de máximo 3 préstamos por persona.

Fecha de préstamo validada (YYYY-MM-DD).

Guarda nombre y fecha del préstamo.

📬 Devolver libros
Se busca por título.

Si está prestado, cambia estado a disponible y elimina datos del préstamo.

🗑️ Eliminar libros
Solo elimina libros disponibles.

Confirma antes de borrar.

💻 Ejecución
Descarga el proyecto o clónalo desde GitHub.

Asegúrate de tener todos los archivos en el mismo directorio.

Ejecuta el menú principal desde tu consola:

bash
Copiar
Editar
python main.py
✍️ Autores
👨‍💻 Ricardo Carmona
👨‍💻 David Palacios
👨‍💻 Luis Fernando Rodríguez López

📌 Notas Adicionales
El sistema no utiliza bases de datos, toda la información se maneja en memoria a través de list_books.

Se pueden extender funcionalidades fácilmente (por ejemplo: persistencia en archivos, login de usuarios, reportes).

🧪 Sugerencias de Mejora Futuras
Guardar y cargar datos desde archivos .json o .csv.

Añadir fechas automáticas de préstamo.

Crear interfaz gráfica con tkinter o una API REST con Flask.
