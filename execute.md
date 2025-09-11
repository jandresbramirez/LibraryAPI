# Ejecuciones con CURL para la LibraryAPI
## Users | Authors | Books | Loans

# <USUARIOS>

1. **Listar usuarios**
```bash
curl -X GET http://127.0.0.1:5000/users
```

2. **Crear usuario**
```bash
curl -X POST http://127.0.0.1:5000/users \
   -H "Content-Type: application/json" \
   -d '{"name": "Juan Perez", "email": "juan@example.com"}'
```

3. **Obtener usuario por ID**
```bash
curl -X GET http://127.0.0.1:5000/users/1
```

4. **Actualizar usuario**
```bash
curl -X PUT http://127.0.0.1:5000/users/1 \
   -H "Content-Type: application/json" \
   -d '{"name": "Juan Actualizado", "email": "juan_updated@example.com"}'
```

5. **Eliminar usuario**
```bash
curl -X DELETE http://127.0.0.1:5000/users/1
```

# <LIBROS>

1. **Listar libros**
```bash
curl -X GET http://127.0.0.1:5000/books
```

2. **Crear libro**
```bash
curl -X POST http://127.0.0.1:5000/books \
   -H "Content-Type: application/json" \
   -d '{"title": "Cien Años de Soledad", "author": "Gabriel García Márquez"}'
```

3. **Obtener libro por ID**
```bash
curl -X GET http://127.0.0.1:5000/books/1
```

4. **Actualizar libro**
```bash
curl -X PUT http://127.0.0.1:5000/books/1 \
   -H "Content-Type: application/json" \
   -d '{"title": "Cien Años de Soledad (Edición Especial)", "author": "Gabriel García Márquez"}'
```

5. **Eliminar libro**
```bash
curl -X DELETE http://127.0.0.1:5000/books/1
```
# <PRÉSTAMOS>

1. **Listar préstamos**
```bash
curl -X GET http://127.0.0.1:5000/loans
```

2. **Crear préstamo**
```bash
curl -X POST http://127.0.0.1:5000/loans \
   -H "Content-Type: application/json" \
   -d '{"user_id": 1, "book_id": 1, "due_date": "2025-10-01"}'
```

3. **Obtener préstamo por ID**
```bash
curl -X GET http://127.0.0.1:5000/loans/1
```

4. **Actualizar préstamo**
```bash
curl -X PUT http://127.0.0.1:5000/loans/1 \
   -H "Content-Type: application/json" \
   -d '{"user_id": 1, "book_id": 1, "due_date": "2025-11-01"}'
```

5. **Eliminar préstamo**
```bash
curl -X DELETE http://127.0.0.1:5000/loans/1
```
# <AUTORES>

1. **Listar autores**
```bash
curl -X GET http://127.0.0.1:5000/authors
```

2. **Crear autor**
```bash
curl -X POST http://127.0.0.1:5000/authors \
  -H "Content-Type: application/json" \
  -d '{"name": "Gabriel García Márquez"}'
```

3. **Obtener autor por ID**
```bash
curl -X GET http://127.0.0.1:5000/authors/1
```

4. **Actualizar autor**
```bash
curl -X PUT http://127.0.0.1:5000/authors/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "Gabriel G. Márquez (Edición)"}'
```

5. **Eliminar autor**
```bash
curl -X DELETE http://127.0.0.1:5000/authors/1
```