from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_url: str = "postgresql+asyncpg://postgres_user:postgres_password@localhost:5430/postgres_db"
    image_saver_url: str = "http://localhost:8000"


config = Settings()
