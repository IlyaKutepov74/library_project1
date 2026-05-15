from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    postgres_user: str = 'POSTGRES_USER'
    postgres_password: str = 'POSTGRES_PASSWORD'
    postgres_db: str = 'POSTGRES_DB'
    postgres_host: str = 'POSTGRES_HOST'
    postgres_port: int = 'POSTGRES_PORT'

    @property
    def database_url(self) -> str:
        return f'postgresql+asyncpg://{self.postgres_user}:{self.postgres_password}@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}'

    #  Общие 
    title: str = 'Library API'

    secret_key: str

    algorithm: str = 'HS256'

    access_token_expire_minutes: int = 30

    first_superuser_email: str | None = None
    first_superuser_password: str | None = None

    #  Внешние API 
    google_books_api_url: str | None = None
    google_books_api_key: str | None = None

    # Ollama 
    ollama_base_url: str = 'http://ollama:11434'
    ollama_model: str = 'qwen2.5:3b'
    ollama_timeout: float = 60.0

    model_config: SettingsConfigDict = {
        'env_file': '.env',
        'env_file_encoding': 'utf-8',
        'extra': 'ignore'
    }


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings: Settings = get_settings()
