from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import base, data, summary, export

app = FastAPI(title="Transparencia Ciudadana API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(base.router)
app.include_router(data.router)
app.include_router(summary.router)
app.include_router(export.router)
