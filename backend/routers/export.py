from fastapi import APIRouter, Response
from sqlalchemy import create_engine, text
import csv
from io import StringIO

router = APIRouter(prefix="/api/v1/export", tags=["export"])

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/transparencia"

@router.get("/")
def export_data():
    # Connect to database
    engine = create_engine(DATABASE_URL)
    
    with engine.connect() as conn:
        # Get all data from spending table
        result = conn.execute(text("SELECT * FROM spending"))
        rows = result.fetchall()
        column_names = result.keys()
    
    # Create CSV in memory
    output = StringIO()
    writer = csv.writer(output)
    
    # Write header
    writer.writerow(column_names)
    
    # Write data
    writer.writerows(rows)
    
    # Get CSV content
    csv_content = output.getvalue()
    output.close()
        
    return Response(
        content=csv_content,
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=spending_data.csv"}
    )
