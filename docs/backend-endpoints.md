# Endpoints del Backend

Base URL: `http://localhost:8000`

## Health
- `GET /health` → `{ status, service }`

## Tareas (CRUD)
- `POST /tasks`
  - Body: `{ title, description?, parent_id? }`
  - Respuesta: `Task`
- `GET /tasks`
  - Query: `skip?`, `limit?`, `root_only?`
  - Respuesta: `Task[]`
- `GET /tasks/{id}` → `Task`
- `PUT /tasks/{id}`
  - Body: `{ title?, description?, parent_id? }`
  - Respuesta: `Task`
- `DELETE /tasks/{id}` → 204 sin contenido

## Recursivo
- `GET /tasks/{id}/with-subtasks`
  - Respuesta: `Task` con `subtasks: Task[]` anidado recursivamente
