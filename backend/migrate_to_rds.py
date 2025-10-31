"""
Migration script to load Data.csv directly to AWS RDS
"""
from sqlalchemy import create_engine, text
import pandas as pd
import os
import sys

# Target database (AWS RDS)
TARGET_DB = "postgresql://postgres:cacaseca000@database-1.cb2682icmjpq.us-east-2.rds.amazonaws.com:5432/postgres"

def load_csv_to_rds():
    """Load Data.csv directly to AWS RDS"""
    
    # Get CSV file path
    csv_path = os.path.join(os.path.dirname(__file__), "Data.csv")
    
    if not os.path.exists(csv_path):
        print(f"❌ Error: Data.csv not found at {csv_path}")
        sys.exit(1)
    
    print("Reading CSV file...")
    # Read CSV with semicolon delimiter
    df = pd.read_csv(csv_path, delimiter=';', encoding='latin-1')
    
    # Clean column names
    df.columns = df.columns.str.strip().str.replace('"', '')
    
    print(f"Found {len(df)} rows in CSV")
    
    print("\nConnecting to AWS RDS database...")
    engine = create_engine(TARGET_DB)
    
    # Create table in target database
    print("Creating table in RDS...")
    with engine.connect() as conn:
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS spending (
                id SERIAL PRIMARY KEY,
                anio VARCHAR(10),
                mes VARCHAR(50),
                estamento VARCHAR(100),
                nombre_completo VARCHAR(255),
                cargo VARCHAR(255),
                grado VARCHAR(50),
                calificacion VARCHAR(255),
                region VARCHAR(100),
                asignaciones_especiales TEXT,
                remuneracion_bruta VARCHAR(50),
                remuneracion_liquida VARCHAR(50),
                rem_adicionales VARCHAR(50),
                rem_bonos VARCHAR(50),
                derecho_horas_extra VARCHAR(10),
                horas_extra_diurnas VARCHAR(100),
                horas_extra_nocturnas VARCHAR(100),
                horas_extra_festivas VARCHAR(100),
                fecha_inicio VARCHAR(20),
                fecha_termino VARCHAR(50),
                observaciones TEXT,
                viaticos VARCHAR(50)
            )
        """))
        conn.commit()
        print("✓ Table created successfully!")
    
    # Rename columns to match database schema
    column_mapping = {
        df.columns[0]: 'anio',
        df.columns[1]: 'mes',
        df.columns[2]: 'estamento',
        df.columns[3]: 'nombre_completo',
        df.columns[4]: 'cargo',
        df.columns[5]: 'grado',
        df.columns[6]: 'calificacion',
        df.columns[7]: 'region',
        df.columns[8]: 'asignaciones_especiales',
        df.columns[9]: 'remuneracion_bruta',
        df.columns[10]: 'remuneracion_liquida',
        df.columns[11]: 'rem_adicionales',
        df.columns[12]: 'rem_bonos',
        df.columns[13]: 'derecho_horas_extra',
        df.columns[14]: 'horas_extra_diurnas',
        df.columns[15]: 'horas_extra_nocturnas',
        df.columns[16]: 'horas_extra_festivas',
        df.columns[17]: 'fecha_inicio',
        df.columns[18]: 'fecha_termino',
        df.columns[19]: 'observaciones',
        df.columns[20]: 'viaticos'
    }
    
    df.rename(columns=column_mapping, inplace=True)
    
    # Load data using pandas to_sql
    print("Loading data into RDS...")
    df.to_sql('spending', engine, if_exists='append', index=False)
    
    print(f"\n✓ Successfully loaded {len(df)} rows into AWS RDS!")
    
    # Verify data
    print("\nVerifying data in RDS...")
    with engine.connect() as conn:
        result = conn.execute(text("SELECT COUNT(*) FROM spending"))
        count = result.scalar()
        print(f"✓ RDS database now has {count} rows")

if __name__ == "__main__":
    print("="*60)
    print("CSV to AWS RDS Migration Script")
    print("="*60)
    print()
    print("RDS Host: database-1.cb2682icmjpq.us-east-2.rds.amazonaws.com")
    print("Database: postgres")
    print()
    
    try:
        load_csv_to_rds()
        print("\n" + "="*60)
        print("✓ Migration completed successfully!")
        print("="*60)
    except Exception as e:
        print(f"\n❌ Error during migration: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
