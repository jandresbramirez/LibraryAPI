# Proyecto de Gestión de Biblioteca (LibraryAPI)

Este proyecto es una base para la gestión de una biblioteca digital, implementado siguiendo el patrón arquitectónico por capas. Utiliza Python, Flask como framework web y SQLAlchemy como ORM para la interacción con bases de datos relacionales.

## Descripción General

El sistema permite registrar, consultar, actualizar y eliminar usuarios, autores, libros y préstamos.
La arquitectura por capas facilita la separación de responsabilidades, mejorando la mantenibilidad, escalabilidad y flexibilidad del código.
El uso de un ORM como SQLAlchemy permite desacoplar la lógica de negocio de la base de datos, facilitando la portabilidad y seguridad.

### Características principales:

- API RESTful para la gestión de usuarios, autores, libros y préstamos.

- Modelos bien definidos y documentados.

- Repositorios para el acceso a datos desacoplados de la lógica de negocio.

- Servicios con validaciones para garantizar reglas de negocio.

- Controladores (Blueprints) que exponen los endpoints de la API.

- Documentación clara para facilitar la comprensión y extensión del sistema.

## Estructura del Proyecto

- `models/`: Definición de los modelos de datos (User, Author, Book, Loan).

- `repositories/`: Implementación de la capa de acceso a datos (repositorios).

- `services/`: Lógica de negocio y validaciones sobre los repositorios.

- `controllers/`: Lógica de los endpoints y controladores de la API.

- `config/`: Configuración de la base de datos (SQLAlchemy).

- `app.py`: Punto de entrada principal de la aplicación.

- `requirements.txt`: Lista de dependencias necesarias para ejecutar el proyecto.


## Cómo crear un entorno virtual en Python
El uso de un entorno virtual es fundamental para aislar las dependencias del proyecto y evitar conflictos con otras aplicaciones o proyectos en tu sistema. Un entorno virtual te permite instalar paquetes específicos para este proyecto sin afectar el entorno global de Python.

### Pasos para crear y activar un entorno virtual:

1. **Instala virtualenv si no lo tienes:**
   ```bash
   pip install virtualenv
   ```

2. **Crea el entorno virtual:**
   ```bash
   python -m venv venv
   ```
   Esto creará una carpeta llamada `venv` en el directorio del proyecto.

3. **Activa el entorno virtual:**
   - En Linux/Mac:
     ```bash
     source venv/bin/activate
     ```
   - En Windows:
     ```cmd
     venv\Scripts\activate
     ```

4. **Instala las dependencias del proyecto:**
   ```bash
   pip install -r requirements.txt
   ```

### Importancia de usar un entorno virtual
- **Aislamiento:** Evita conflictos entre dependencias de diferentes proyectos.
- **Reproducibilidad:** Permite que otros desarrolladores instalen exactamente las mismas versiones de las librerías.
- **Facilidad de despliegue:** Simplifica la migración y despliegue en diferentes entornos (desarrollo, pruebas, producción).
- **Limpieza:** Mantiene tu instalación global de Python libre de paquetes innecesarios.


## Ejecutar el servidor desde la terminal:

```bash
   python app.py
   ```

## La API estará disponible en:

### http://127.0.0.1:5000

## Endpoints principales

#### /users → Gestión de usuarios.

#### /authors → Gestión de autores.

#### /books → Gestión de libros.

#### /loans → Gestión de préstamos.

#### / → Endpoint de bienvenida 📚.