from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    database_url: str = "postgresql://postgres:postgres@localhost:5432/todo_db"
    postgres_user: str = "postgres"
    postgres_password: str = "postgres"
    postgres_db: str = "todo_db"
    postgres_host: str = "localhost"
    postgres_port: int = 5432
    
    class Config:
        env_file = ".env"
        case_sensitive = False


@lru_cache()
def get_settings() -> Settings:
    return Settings()
