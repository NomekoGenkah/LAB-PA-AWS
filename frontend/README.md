# Frontend - Hierarchical To-Do App

Aplicación React + Vite + TypeScript para gestionar tareas jerárquicas (tareas y sub-tareas recursivas).

## Páginas

- `Home`: Estado del backend y navegación.
- `Task List`: Lista de tareas raíz y creación de nuevas tareas.
- `Task Detail`: Vista detalle de una tarea con todas sus sub-tareas.

## Componentes Clave

- `components/TaskTree.tsx`: Render recursivo de una tarea y sus sub-tareas.
- `store/tasks.ts`: Estado global con Zustand (lista de tareas raíz y tarea seleccionada).
- `api/tasks.ts`: Cliente de API (axios) para CRUD y obtención recursiva.

## Variables de Entorno

Crear `.env` basado en `.env.example`:

```
VITE_API_URL=http://localhost:8000
```

## Comandos

```powershell
cd frontend
npm install
npm run dev      # Vite dev server con HMR
npm run build    # tsc -b && vite build
npm run preview  # servir build en :5173
```

## Docker (producción)

Construir y correr con una URL de API específica:

```powershell
cd frontend
docker build -t todo-frontend --build-arg VITE_API_URL=http://localhost:8000 .
docker run -d -p 5173:5173 --name todo-frontend todo-frontend
```

En Docker Compose, se usa `VITE_API_URL=http://backend:8000` para comunicar con el servicio backend.

## Arquitectura rápida

- Router con `react-router-dom` para rutas `/`, `/tasks`, `/tasks/:id`.
- Estado global con Zustand para tareas.
- `TaskTree` renderiza la jerarquía de forma recursiva.

## Notas

- Para ver sub-tareas recién creadas o eliminar, refresca la vista (boilerplate inicial; se puede mejorar con invalidación/refresh automático).
- Por defecto, CORS está abierto en el backend durante desarrollo.
