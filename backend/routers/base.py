from fastapi import APIRouter

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
