from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="TRIAGE_", env_file=".env")

    app_name: str = "ai-incident-triage"
    env: str = "dev"
    log_level: str = "info"


settings = Settings()
