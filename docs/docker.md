# Guía Docker / Docker Compose

## Servicios
- `db`: PostgreSQL con volumen persistente.
- `backend`: FastAPI exponiendo `:8000`.
- `frontend`: Vite preview sirviendo `:5173` (construido con `VITE_API_URL=http://backend:8000`).

## Levantar con Compose

```powershell
# Desde la raíz
docker compose up -d --build

# Ver logs
docker compose logs -f backend
```

## Puertos
- Frontend: http://localhost:5173
- Backend: http://localhost:8000
- PostgreSQL: localhost:5432 (desde host)

## Notas
- En producción, considera servir el frontend con Nginx. Para este boilerplate usamos `vite preview` por simplicidad.
- Ajusta credenciales/variables en `.env` según tu entorno.
