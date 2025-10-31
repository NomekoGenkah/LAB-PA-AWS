"""
Script to verify RDS connection and data
"""
from sqlalchemy import create_engine, text

DATABASE_URL = "postgresql://postgres:cacaseca000@database-1.cb2682icmjpq.us-east-2.rds.amazonaws.com:5432/postgres"

def check_connection():
    """Check database connection and data"""
    
    print("Connecting to AWS RDS...")
    engine = create_engine(DATABASE_URL)
    
    try:
        with engine.connect() as conn:
            print("✓ Connection successful!\n")
            
            # Check if table exists
            result = conn.execute(text("""
                SELECT EXISTS (
                    SELECT FROM information_schema.tables 
                    WHERE table_name = 'spending'
                );
            """))
            table_exists = result.scalar()
            
            if table_exists:
                print("✓ Table 'spending' exists\n")
                
                # Get row count
                result = conn.execute(text("SELECT COUNT(*) FROM spending"))
                count = result.scalar()
                print(f"✓ Total rows in spending table: {count}\n")
                
                # Get first 3 rows
                print("First 3 rows:")
                print("-" * 80)
                result = conn.execute(text("SELECT nombre_completo, cargo, region, remuneracion_bruta FROM spending LIMIT 3"))
                for row in result:
                    print(f"  Nombre: {row[0]}")
                    print(f"  Cargo: {row[1]}")
                    print(f"  Región: {row[2]}")
                    print(f"  Remuneración: {row[3]}")
                    print("-" * 80)
                
                print("\n✓ Database is ready to use!")
            else:
                print("❌ Table 'spending' does not exist")
                print("Run migrate_to_rds.py first")
                
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    check_connection()
