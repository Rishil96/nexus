from pydantic_settings import BaseSettings, SettingsConfigDict


# Set up environment variables
class Settings(BaseSettings):
    openai_api_key: str
    model_name: str = "gpt-5.4-nano"
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()   # noqa
