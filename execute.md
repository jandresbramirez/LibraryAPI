# Ejecuciones con CURL para la LibraryAPI
## Users | Authors | Books | Loans

## -- USUARIOS --

```bash
TOKEN=$(curl -s -X POST http://127.0.0.1:5000/login \
  -H "Content-Type: application/json" \
  -d '{"email": "juan@example.com", "password": "juan123"}' | jq -r '.access_token')
```

1. **Login de Usuarios**
```bash
curl -X POST http://127.0.0.1:5000/login \
   -H "Content-Type: application/json" \
   -d '{"email": "juan@example.com", "password": "juan123"}'
```
**Erroneo**
```bash
curl -X POST http://127.0.0.1:5000/login \
   -H "Content-Type: application/json" \
   -d '{"email": "admin@example.com", "password": "admin123"}'
```

2. **Listar usuarios**
```bash
curl -X GET http://127.0.0.1:5000/users \
   -H "Authorization: Bearer $TOKEN" \
   -H "Content-Type: application/json"
```

3. **Obtener usuario por ID**
```bash
curl -X GET http://127.0.0.1:5000/users/1 \
   -H "Authorization: Bearer $TOKEN" \
   -H "Content-Type: application/json"
```

4. **Obtener usuario por email**
```bash
curl -X GET http://127.0.0.1:5000/users/juan@example.com \
   -H "Authorization: Bearer $TOKEN" \
   -H "Content-Type: application/json"
```

5. **Registrar Nuevo Usuario**
```bash
curl -X POST http://127.0.0.1:5000/registry \
   -H "Content-Type: application/json" \
   -d '{"name": "Juan Perez", "email": "juan@example.com", "password": "juan123"}'
```

6. **Actualizar Usuario**
```bash
curl -X PUT http://127.0.0.1:5000/users/1 \
   -H "Authorization: Bearer $TOKEN" \
   -H "Content-Type: application/json" \
   -d '{"name": "Juan Actualizado", "email": "juan_updated@example.com", "password": "nuevo123"}'
```
7. **Eliminar Usuario**
```bash
curl -X DELETE http://127.0.0.1:5000/users/1 \
   -H "Authorization: Bearer $TOKEN" \
   -H "Content-Type: application/json"
```
8. **Cerrar Sesión**
```bash
curl -X POST http://127.0.0.1:5000/logout \
   -H "Authorization: Bearer $TOKEN"
```


## -- LIBROS --

1. **Listar libros**
```bash
curl -X GET http://127.0.0.1:5000/books
```

2. **Obtener libro por ID**
```bash
curl -X GET http://127.0.0.1:5000/books/1 \
   -H "Authorization: Bearer $TOKEN" \
   -H "Content-Type: application/json"
```

3. **Crear nuevo libro**
```bash
curl -X POST http://127.0.0.1:5000/books \
   -H "Authorization: Bearer $TOKEN" \
   -H "Content-Type: application/json" \
   -d '{"title": "El Principito", "author_id": 1}'
```

4. **Actualizar libro**
```bash
curl -X PUT http://127.0.0.1:5000/books/1 \
   -H "Authorization: Bearer $TOKEN" \
   -H "Content-Type: application/json" \
   -d '{"title": "El Principito (Edición Revisada)", "author_id": 1}'
```

5. **Eliminar libro**
```bash
curl -X DELETE http://127.0.0.1:5000/books/1 \
   -H "Authorization: Bearer $TOKEN" \
   -H "Content-Type: application/json"
```

## -- PRÉSTAMOS --

1. **Listar préstamos**
```bash
curl -X GET http://127.0.0.1:5000/loans \
   -H "Authorization: Bearer $TOKEN" \
   -H "Content-Type: application/json"
```

2. **Obtener préstamo por ID**
```bash
curl -X GET http://127.0.0.1:5000/loans/1 \
   -H "Authorization: Bearer $TOKEN" \
   -H "Content-Type: application/json"
```

3. **Crear prestamo**
```bash
curl -X POST http://127.0.0.1:5000/loans \
   -H "Authorization: Bearer $TOKEN" \
   -H "Content-Type: application/json" \
   -d '{"user_id": 1, "book_id": 2}'
```

4. **Actualizar fecha de devolución de préstamo**
```bash
curl -X PUT http://127.0.0.1:5000/loans/1 \
   -H "Authorization: Bearer $TOKEN" \
   -H "Content-Type: application/json" \
   -d '{"return_date": "2025-10-20"}'
```

5. **Eliminar préstamo**
```bash
curl -X DELETE http://127.0.0.1:5000/loans/1 \
   -H "Authorization: Bearer $TOKEN" \
   -H "Content-Type: application/json"
```

## -- AUTORES --

1. **Listar autores**
```bash
curl -X GET http://127.0.0.1:5000/authors
```

2. **Obtener autor por ID**
```bash
curl -X GET http://127.0.0.1:5000/authors/1 \
   -H "Authorization: Bearer $TOKEN" \
   -H "Content-Type: application/json"
```

3. **Crear Autor**
```bash
curl -X POST http://127.0.0.1:5000/authors \
   -H "Authorization: Bearer $TOKEN" \
   -H "Content-Type: application/json" \
   -d '{"name": "Gabriel García Márquez"}'
```

4. **Actualizar autor**
```bash
curl -X PUT http://127.0.0.1:5000/authors/1 \
   -H "Authorization: Bearer $TOKEN" \
   -H "Content-Type: application/json" \
   -d '{"name": "Gabo Actualizado"}'
```

5. **Eliminar autor**
```bash
curl -X DELETE http://127.0.0.1:5000/authors/1 \
   -H "Authorization: Bearer $TOKEN" \
   -H "Content-Type: application/json"
```