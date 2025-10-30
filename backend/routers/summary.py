from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/summary", tags=["summary"])

@router.get("/")
def get_summary():
    return {"total": 0, "promedio": 0}

@router.get("/by-region")
def summary_by_region():
    return {"summary": []}

@router.get("/by-cargo")
def summary_by_cargo():
    return {"summary": []}

@router.get("/by-mes")
def summary_by_month():
    return {"summary": []}
