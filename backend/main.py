from fastapi import FastAPI
from routers import base, data, summary, export

app = FastAPI(title="Transparencia Ciudadana API")

# Register routers
app.include_router(base.router)
app.include_router(data.router)
app.include_router(summary.router)
app.include_router(export.router)
