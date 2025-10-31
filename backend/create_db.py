import pandas as pd
from sqlalchemy import create_engine, text
import os
import sys

# Set locale to avoid encoding issues on Windows
if sys.platform == 'win32':
    os.environ['PYTHONIOENCODING'] = 'utf-8'
    os.environ['LANG'] = 'en_US.UTF-8'
    os.environ['LC_ALL'] = 'en_US.UTF-8'

# Database configuration - use ignore_errors to bypass locale issues
DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/transparencia?client_encoding=utf8"

def create_table():
    """Create the spending table"""
    try:
        engine = create_engine(DATABASE_URL, connect_args={'connect_timeout': 10})
    except Exception as e:
        print(f"Error creating engine: {e}")
        print("\nThis is a known issue with psycopg2 on Windows with Spanish PostgreSQL.")
        print("Please try one of these solutions:")
        print("1. Change PostgreSQL locale to English")
        print("2. Use pgAdmin to create the table manually")
        print("3. Install psycopg (version 3): pip install psycopg[binary]")
        raise
    
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
    
    print("Table 'spending' created successfully")

def load_csv_to_db():
    """Read CSV file and load data into PostgreSQL"""
    csv_path = os.path.join(os.path.dirname(__file__), "Data.csv")
    
    # Read CSV with semicolon delimiter
    df = pd.read_csv(csv_path, delimiter=';', encoding='latin-1')
    
    # Clean column names
    df.columns = df.columns.str.strip().str.replace('"', '')
    
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
    engine = create_engine(DATABASE_URL)
    df.to_sql('spending', engine, if_exists='append', index=False)
    
    print(f"Successfully loaded {len(df)} rows into the database")

if __name__ == "__main__":
    print("Starting database setup...")
    print("Note: Make sure the 'transparencia' database exists")
    print("If not, create it manually: CREATE DATABASE transparencia;")
    create_table()
    load_csv_to_db()
    print("Database setup completed!")
