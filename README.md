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

- `config/`: Configuración de la base de datos (SQLAlchemy), jwt, mensajes logger y decorador de roles.

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

| **Módulo** | **Método** | **Endpoint** | **Descripción** | **Autenticación / Rol** |
|-------------|-------------|---------------|------------------|--------------------------|
| **Inicio** | GET | `/` | Muestra mensaje de bienvenida del sistema. | No requiere |
| **Usuarios** | GET | `/users` | Lista todos los usuarios. | No requiere |
|  | GET | `/users/<id>` | Obtiene un usuario por su ID. | admin, editor, user |
|  | GET | `/users/<email>` | Obtiene un usuario por su email. | admin, editor, user |
|  | POST | `/users` | Crea un nuevo usuario. | admin |
|  | PUT | `/users/<id>` | Actualiza los datos de un usuario. | admin, editor |
|  | DELETE | `/users/<id>` | Elimina un usuario. | admin |
| **Autores** | GET | `/authors` | Lista todos los autores. | No requiere |
|  | GET | `/authors/<id>` | Obtiene un autor por su ID. | admin, editor, user |
|  | POST | `/authors` | Crea un nuevo autor. | admin, editor |
|  | PUT | `/authors/<id>` | Actualiza los datos de un autor. | admin, editor |
|  | DELETE | `/authors/<id>` | Elimina un autor. | admin |
| **Libros** | GET | `/books` | Lista todos los libros. | No requiere |
|  | GET | `/books/<id>` | Obtiene un libro por su ID. | admin, editor, user |
|  | POST | `/books` | Crea un nuevo libro. | admin, editor |
|  | PUT | `/books/<id>` | Actualiza los datos de un libro. | admin, editor |
|  | DELETE | `/books/<id>` | Elimina un libro. | admin |
| **Préstamos** | GET | `/loans` | Lista todos los préstamos. | admin, editor |
|  | GET | `/loans/<id>` | Obtiene un préstamo por su ID. | admin, editor, user |
|  | POST | `/loans` | Crea un nuevo préstamo. | admin, user |
|  | PUT | `/loans/<id>` | Actualiza un préstamo existente. | admin, editor |
|  | DELETE | `/loans/<id>` | Elimina un préstamo. | admin |

## ------------------------------------------------------------------------------------------------------------------
## 🔐 Flujo de Autenticación

El sistema implementa autenticación mediante **JWT (JSON Web Tokens)** y control de acceso basado en roles.  
A continuación, se describe el flujo completo desde el registro de un nuevo usuario hasta el acceso a rutas protegidas.

---

### 1. Registro de usuario
Antes de iniciar sesión, el usuario debe registrarse en el sistema enviando sus datos al endpoint correspondiente.

```bash
curl -X POST http://127.0.0.1:5000/register \
   -H "Content-Type: application/json" \
   -d '{"name": "Juan Perez", "email": "juan@example.com", "password": "12345"}'
```
Resultado esperado:
{
  "message": "Usuario registrado exitosamente"
}

### 2. Inicio de sesión
Una vez registrado, el usuario puede iniciar sesión con sus credenciales.
El servidor valida los datos y genera un token JWT que debe usarse en las solicitudes protegidas.

```bash
curl -X POST http://127.0.0.1:5000/login \
   -H "Content-Type: application/json" \
   -d '{"email": "juan@example.com", "password": "12345"}'
```

Resultado esperado:
{
  "access_token": "<TOKEN_JWT_GENERADO>"
}

### 3. Envío del token en solicitudes protegidas
Para acceder a endpoints que requieren autenticación, se debe incluir el token en el encabezado HTTP Authorization:

```bash
curl -X GET http://127.0.0.1:5000/authors/1 \
   -H "Authorization: Bearer <TOKEN_JWT_GENERADO>"
```

### 4. Validación del token (@jwt_required())
El decorador @jwt_required() se utiliza en los controladores para restringir el acceso a usuarios autenticados.
Antes de procesar la solicitud, el sistema verifica que el token sea válido, no esté expirado y corresponda a un usuario existente.
Si el token no se envía o es inválido, el servidor responde con un error 401 Unauthorized.

### 5. Control de roles (@role_required([...]))
Además de validar el token, el sistema restringe el acceso según el rol del usuario.
El decorador @role_required([...]) permite definir qué roles tienen permiso sobre un endpoint específico:

```python
@jwt_required()
@role_required(["admin", "editor"])
def create_book():
    ...
```

### 6. Expiración y renovación del token
Los tokens tienen un tiempo de vida definido por el servidor.
Una vez expirado, el usuario debe iniciar sesión nuevamente para obtener un nuevo token válido.