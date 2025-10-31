from fastapi import APIRouter
import random

router = APIRouter(prefix="", tags=["base"])

@router.get("/")
def root():
    return {"status": "ok", "message": "API is running"}

@router.get("/api/v1/meta")
def get_meta():
    # (Later: query dataset info from DB or metadata table)
    return {
        "dataset_name": "Remuneraciones Municipalidad de La Serena - 2025",
        "rows": 1043,
        "columns": ["Año", "Mes", "Nombre", "Cargo", "Región", "Remuneración"]
    }

@router.get("/api/v1/random")
def get_random_number():
    number = random.randint(1, 10)
    return {"number": number}

@router.get("/api/v1/test")
def test_connection():
    return {
        "status": "success",
        "message": "Backend is working!",
        "server": "Transparencia Ciudadana API"
    }
