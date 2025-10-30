from fastapi import APIRouter, Response

router = APIRouter(prefix="/api/v1/export", tags=["export"])

@router.get("/")
def export_data():
    csv_content = "nombre,cargo,region,remuneracion\nJuan,Perez,Coquimbo,2010410"
    return Response(content=csv_content, media_type="text/csv")
