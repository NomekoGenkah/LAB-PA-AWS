# Componentes Clave del Frontend

## `TaskTree`
- Renderiza una tarea y sus `subtasks` recursivamente.
- Acciones básicas: expandir/colapsar, añadir sub-tarea, eliminar.
- Se puede extender para edición inline y reordenamiento.

## Páginas
- `Home`: muestra health del backend y navegación.
- `TaskList`: carga tareas raíz (`root_only=true`), crea nuevas, y enlaza a detalles.
- `TaskDetail`: carga una tarea con todas sus sub-tareas (`/with-subtasks`).

## Estado (Zustand)
- `useTaskStore`: almacena `tasks` (raíces), `selectedTask`, `loading`, `error`.
- Acciones: `loadRootTasks`, `loadTaskWithSubtasks`, `addTask`, `editTask`, `removeTask`.

## Cliente HTTP
- `api/client.ts`: axios con `VITE_API_URL`.
- `api/tasks.ts`: funciones CRUD y endpoints recursivos.
