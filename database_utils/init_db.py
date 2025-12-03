import os
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from dotenv import load_dotenv


def ensure_database():
    host = os.getenv('POSTGRES_HOST', 'localhost')
    port = int(os.getenv('POSTGRES_PORT', '5432'))
    user = os.getenv('POSTGRES_USER', 'postgres')
    password = os.getenv('POSTGRES_PASSWORD', 'postgres')
    dbname = os.getenv('POSTGRES_DB', 'todo_db')

    # Connect to default 'postgres' database to create target DB if not exists
    conn = psycopg2.connect(host=host, port=port, user=user, password=password, dbname='postgres')
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    cur.execute("SELECT 1 FROM pg_database WHERE datname = %s", (dbname,))
    exists = cur.fetchone() is not None
    if not exists:
        cur.execute(f'CREATE DATABASE {dbname};')
        print(f"Database '{dbname}' created.")
    else:
        print(f"Database '{dbname}' already exists.")
    cur.close()
    conn.close()


if __name__ == '__main__':
    # Load .env if present
    load_dotenv()
    ensure_database()
    print('Done.')
