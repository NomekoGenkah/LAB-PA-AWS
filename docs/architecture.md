# Arquitectura General

El proyecto "Hierarchical To-Do App" se compone de tres capas principales:

- `frontend/`: SPA en React + Vite + TypeScript.
- `backend/`: API en FastAPI con SQLAlchemy y PostgreSQL.
- `database_utils/`: utilidades para inicializar la base de datos.

## Flujo de Datos

1. El usuario interactúa con la SPA (React) y dispara acciones (crear, listar, ver tarea).
2. El frontend llama al backend vía HTTP (REST) usando `axios`.
3. El backend procesa las solicitudes, accede a PostgreSQL mediante SQLAlchemy y devuelve JSON.
4. Para estructuras jerárquicas, el backend expone `/tasks/{id}/with-subtasks` que retorna un árbol recursivo.

## Decisiones Clave

- Relación auto-referenciada en `Task.parent_id` para permitir jerarquía infinita.
- Renderizado recursivo en el frontend (`TaskTree`) para mostrar sub-tareas.
- Alembic para versionar el esquema y facilitar despliegues.
- `VITE_API_URL` configurable para conectar contra diferentes entornos.

## Directorios Clave

- `backend/app/models.py`: Modelo SQLAlchemy `Task`.
- `backend/app/crud.py`: Lógica de acceso/negocio CRUD y carga recursiva.
- `backend/app/main.py`: Rutas FastAPI y CORS.
- `frontend/src/components/TaskTree.tsx`: Render recursivo.
- `frontend/src/store/tasks.ts`: Estado global (Zustand).
- `frontend/src/api/tasks.ts`: Cliente HTTP hacia el backend.