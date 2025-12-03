# Hierarchical To-Do App

Repositorio monorepo con frontend (React + Vite), backend (FastAPI) y utilidades de base de datos para una To-Do App jerárquica.

## Estructura

```
frontend/         # SPA React + Vite + TS
backend/          # FastAPI + SQLAlchemy + Alembic
database_utils/   # Scripts para inicializar DB
docs/             # Documentación del proyecto
docker-compose.yaml
```

## Levantar localmente (Docker Compose)

```powershell
docker compose up -d --build

# Ver servicios
docker compose ps

# Ver logs
docker compose logs -f backend
```

- Frontend: http://localhost:5173
- Backend: http://localhost:8000
- PostgreSQL: localhost:5432

## Levantar manualmente

Backend:
```powershell
cd backend
pip install -r requirements.txt
# Alembic (opcional)
alembic revision --autogenerate -m "Initial"; alembic upgrade head
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Frontend:
```powershell
cd frontend
npm install
npm run dev
```

## Documentación

- `docs/architecture.md` — Arquitectura general
- `docs/flows.md` — Flujo de sub-tareas
- `docs/backend-endpoints.md` — Endpoints FastAPI
- `docs/frontend-components.md` — Componentes clave del frontend
- `docs/docker.md` — Guía Docker / Compose

## Despliegue en AWS EC2 (futuro)

- Usar los `Dockerfile` de `frontend/` y `backend/` y `docker-compose.yaml`.
- Configurar seguridad y variables de entorno.

