import subprocess
import sys

def create_database_with_psql():
    """Create database using psql command line"""
    print("Creating database 'transparencia' using psql...")
    
    # SQL command to create database
    sql_command = "CREATE DATABASE transparencia;"
    
    try:
        # Run psql command
        result = subprocess.run(
            ['psql', '-U', 'postgres', '-c', sql_command],
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='ignore'  # Ignore encoding errors
        )
        
        if result.returncode == 0 or 'already exists' in result.stderr.lower():
            print("Database 'transparencia' is ready!")
            return True
        else:
            print(f"Error: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"Error running psql: {e}")
        print("Please create the database manually:")
        print("  psql -U postgres")
        print("  CREATE DATABASE transparencia;")
        return False

if __name__ == "__main__":
    if create_database_with_psql():
        print("\nNow run: python create_db.py")
    else:
        sys.exit(1)
