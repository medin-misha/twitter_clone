from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_url: str = (
        "postgresql+asyncpg://postgres_user:postgres_password@localhost:5430/postgres_db"
    )
    image_saver_url: str = "http://127.0.0.1:8000/"


config = Settings()
