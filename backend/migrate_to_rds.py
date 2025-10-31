"""
Migration script to copy data from local PostgreSQL to AWS RDS
"""
from sqlalchemy import create_engine, text
import sys

# Source database (local PostgreSQL)
SOURCE_DB = "postgresql://postgres:postgres@localhost:5432/transparencia"

# Target database (AWS RDS)
# Format: postgresql://username:password@host:port/database
# You need to provide the username, password, and database name
TARGET_DB = "postgresql://admin:cacaseca000@database-1.cb2682icmjpq.us-east-2.rds.amazonaws.com:5432/database-1"

def migrate_data():
    """Migrate data from local DB to AWS RDS"""
    
    print("Connecting to source database (local)...")
    source_engine = create_engine(SOURCE_DB)
    
    print("Connecting to target database (AWS RDS)...")
    target_engine = create_engine(TARGET_DB)
    
    # Create table in target database
    print("Creating table in target database...")
    with target_engine.connect() as conn:
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
        print("Table created successfully!")
    
    # Read data from source
    print("Reading data from source database...")
    with source_engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM spending"))
        rows = result.fetchall()
        column_names = result.keys()
        print(f"Found {len(rows)} rows to migrate")
    
    # Insert data into target
    print("Inserting data into target database...")
    with target_engine.connect() as conn:
        for i, row in enumerate(rows, 1):
            conn.execute(text("""
                INSERT INTO spending (
                    anio, mes, estamento, nombre_completo, cargo, grado, calificacion, region,
                    asignaciones_especiales, remuneracion_bruta, remuneracion_liquida,
                    rem_adicionales, rem_bonos, derecho_horas_extra, horas_extra_diurnas,
                    horas_extra_nocturnas, horas_extra_festivas, fecha_inicio, fecha_termino,
                    observaciones, viaticos
                ) VALUES (
                    :anio, :mes, :estamento, :nombre_completo, :cargo, :grado, :calificacion, :region,
                    :asignaciones_especiales, :remuneracion_bruta, :remuneracion_liquida,
                    :rem_adicionales, :rem_bonos, :derecho_horas_extra, :horas_extra_diurnas,
                    :horas_extra_nocturnas, :horas_extra_festivas, :fecha_inicio, :fecha_termino,
                    :observaciones, :viaticos
                )
            """), {
                'anio': row[1],
                'mes': row[2],
                'estamento': row[3],
                'nombre_completo': row[4],
                'cargo': row[5],
                'grado': row[6],
                'calificacion': row[7],
                'region': row[8],
                'asignaciones_especiales': row[9],
                'remuneracion_bruta': row[10],
                'remuneracion_liquida': row[11],
                'rem_adicionales': row[12],
                'rem_bonos': row[13],
                'derecho_horas_extra': row[14],
                'horas_extra_diurnas': row[15],
                'horas_extra_nocturnas': row[16],
                'horas_extra_festivas': row[17],
                'fecha_inicio': row[18],
                'fecha_termino': row[19],
                'observaciones': row[20],
                'viaticos': row[21]
            })
            
            if i % 50 == 0:
                print(f"Migrated {i}/{len(rows)} rows...")
        
        conn.commit()
    
    print(f"\n✓ Migration completed! {len(rows)} rows migrated successfully.")
    
    # Verify data
    print("\nVerifying data in target database...")
    with target_engine.connect() as conn:
        result = conn.execute(text("SELECT COUNT(*) FROM spending"))
        count = result.scalar()
        print(f"Target database now has {count} rows")

if __name__ == "__main__":
    print("="*60)
    print("PostgreSQL to AWS RDS Migration Script")
    print("="*60)
    print()
    print("IMPORTANT: Update TARGET_DB with your RDS credentials:")
    print("  - Username (default: admin)")
    print("  - Password (replace YOUR_PASSWORD)")
    print("  - Database name (default: transparencia)")
    print()
    
    response = input("Have you updated the credentials? (yes/no): ")
    if response.lower() != 'yes':
        print("Please update the TARGET_DB variable in the script first.")
        sys.exit(1)
    
    try:
        migrate_data()
    except Exception as e:
        print(f"\n❌ Error during migration: {e}")
        sys.exit(1)
