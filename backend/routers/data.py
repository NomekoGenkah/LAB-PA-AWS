from fastapi import APIRouter, Query

router = APIRouter(prefix="/api/v1/data", tags=["data"])

@router.get("/")
def get_data(page: int = 1, limit: int = 50,
             region: str | None = None,
             cargo: str | None = None):
    # (Later: SQL query with filters + pagination)
    return {"page": page, "limit": limit, "results": []}

@router.get("/search")
def search_data(q: str):
    # (Later: full-text or LIKE search)
    return {"query": q, "results": []}
