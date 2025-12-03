# Database Utilities

Utilidades para inicializar la base de datos PostgreSQL local.

## Archivos

- `init_db.py`: Crea la base de datos si no existe (no crea tablas; para tablas usar Alembic o `models.Base.metadata.create_all`).
- `.env.example`: Variables de conexión a PostgreSQL.

## Uso

1. Crear `.env` a partir de `.env.example` y ajustar valores.

```powershell
cd database_utils
copy .env.example .env
```

2. Instalar dependencias necesarias (puedes usar un venv):

```powershell
pip install psycopg2-binary python-dotenv
```

3. Ejecutar el script:

```powershell
python init_db.py
```

4. Crear tablas

Usa Alembic en `backend/` para generar y aplicar migraciones:

```powershell
cd ..\backend
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
```
