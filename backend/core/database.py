"""
Database configuration for AWS RDS
"""
from sqlalchemy import create_engine

# AWS RDS Database URL
DATABASE_URL = "postgresql://postgres:cacaseca000@database-1.cb2682icmjpq.us-east-2.rds.amazonaws.com:5432/postgres"

# Create engine
engine = create_engine(DATABASE_URL)

def get_db_connection():
    """Get database connection"""
    return engine.connect()
