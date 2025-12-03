# Backend - Hierarchical To-Do API

FastAPI backend para gestionar tareas con estructura recursiva (tareas y sub-tareas infinitas).

## Stack Tecnológico

- **FastAPI**: Framework web moderno y rápido
- **SQLAlchemy**: ORM para gestión de base de datos
- **PostgreSQL**: Base de datos relacional
- **Alembic**: Manejo de migraciones de base de datos
- **Pydantic**: Validación de datos y schemas

## Arquitectura

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py          # Punto de entrada de FastAPI
│   ├── config.py        # Configuración y variables de entorno
│   ├── database.py      # Configuración de SQLAlchemy
│   ├── models.py        # Modelos de base de datos
│   ├── schemas.py       # Schemas Pydantic
│   └── crud.py          # Operaciones CRUD
├── alembic/             # Migraciones de base de datos
├── Dockerfile
├── requirements.txt
├── alembic.ini
└── README.md
```

## Modelo de Datos

### Task (Tarea)

```python
{
    "id": int,
    "title": str,
    "description": str | null,
    "parent_id": int | null,  # Referencia a tarea padre
    "created_at": datetime,
    "updated_at": datetime
}
```

## Endpoints de la API

### Health Check

- `GET /health` - Verifica el estado del servicio

### CRUD de Tareas

- `POST /tasks` - Crear nueva tarea
- `GET /tasks` - Listar todas las tareas (paginado)
  - Query params: `skip`, `limit`, `root_only`
- `GET /tasks/{task_id}` - Obtener tarea específica
- `GET /tasks/{task_id}/with-subtasks` - Obtener tarea con todas sus sub-tareas recursivamente
- `PUT /tasks/{task_id}` - Actualizar tarea
- `DELETE /tasks/{task_id}` - Eliminar tarea y todas sus sub-tareas (cascade)

## Configuración Local

### 1. Requisitos Previos

- Python 3.11+
- PostgreSQL 15+
- pip

### 2. Configurar Variables de Entorno

Copia `.env.example` a `.env` y ajusta las variables:

```bash
cp .env.example .env
```

Contenido de `.env`:
```
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/todo_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=todo_db
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

### 3. Instalar Dependencias

```bash
pip install -r requirements.txt
```

### 4. Crear Base de Datos

Asegúrate de tener PostgreSQL corriendo y crea la base de datos:

```sql
CREATE DATABASE todo_db;
```

O usa el script en `database_utils/`.

### 5. Ejecutar Migraciones

```bash
# Generar migración inicial
alembic revision --autogenerate -m "Initial migration"

# Aplicar migraciones
alembic upgrade head
```

### 6. Ejecutar el Servidor

```bash
# Modo desarrollo
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# O usando Python directamente
python -m app.main
```

El servidor estará disponible en: `http://localhost:8000`

Documentación interactiva:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Uso con Docker

### Construir Imagen

```bash
docker build -t todo-backend .
```

### Ejecutar Container

```bash
docker run -d \
  --name todo-backend \
  -p 8000:8000 \
  -e DATABASE_URL=postgresql://postgres:postgres@host.docker.internal:5432/todo_db \
  todo-backend
```

### Usando Docker Compose

Ver `docker-compose.yml` en la raíz del proyecto para levantar todo el stack.

```bash
# Desde la raíz del proyecto
docker-compose up -d
```

## Desarrollo

### Crear Nueva Migración

```bash
alembic revision --autogenerate -m "Descripción del cambio"
alembic upgrade head
```

### Rollback de Migración

```bash
alembic downgrade -1
```

### Tests Manuales con cURL

```bash
# Health check
curl http://localhost:8000/health

# Crear tarea raíz
curl -X POST http://localhost:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Tarea Principal", "description": "Descripción"}'

# Crear sub-tarea
curl -X POST http://localhost:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Sub-tarea", "parent_id": 1}'

# Obtener tarea con sub-tareas
curl http://localhost:8000/tasks/1/with-subtasks
```

## Estructura Recursiva

El modelo soporta jerarquía infinita de tareas:

```
Tarea 1 (parent_id: null)
├── Tarea 2 (parent_id: 1)
│   ├── Tarea 3 (parent_id: 2)
│   │   └── Tarea 4 (parent_id: 3)
│   └── Tarea 5 (parent_id: 2)
└── Tarea 6 (parent_id: 1)
```

El endpoint `/tasks/{id}/with-subtasks` retorna toda la estructura recursiva en formato JSON anidado.

## Despliegue en AWS EC2

1. **Preparar instancia EC2**:
   - Instalar Docker y Docker Compose
   - Abrir puerto 8000 en Security Group

2. **Subir código**:
   ```bash
   scp -r backend/ ec2-user@<EC2_IP>:/home/ec2-user/
   ```

3. **Configurar variables de entorno** en el servidor

4. **Construir y ejecutar**:
   ```bash
   docker build -t todo-backend .
   docker run -d -p 8000:8000 --env-file .env todo-backend
   ```

## Troubleshooting

### Error de conexión a PostgreSQL

Verifica que:
- PostgreSQL esté corriendo
- Credenciales en `.env` sean correctas
- El host sea accesible (usa `localhost` o `host.docker.internal` en Docker)

### Error en migraciones

```bash
# Reset de base de datos (CUIDADO: elimina datos)
alembic downgrade base
alembic upgrade head
```

### Puerto ya en uso

```bash
# Cambiar puerto en comando uvicorn
uvicorn app.main:app --reload --port 8001
```

## Próximos Pasos

- [ ] Agregar tests unitarios (pytest)
- [ ] Implementar autenticación (JWT)
- [ ] Agregar logging estructurado
- [ ] Implementar cache con Redis
- [ ] Agregar rate limiting
