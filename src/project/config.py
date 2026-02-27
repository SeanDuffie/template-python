""" @file config.py
    @author Sean Duffie
    @brief This file allows us to automatically pull secret envrionment variables from a local .env file
"""
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # This will automatically look for an 'API_KEY' environment variable or .env entry
    api_key: str = "123"
    database_url: str = "sqlite:///./test.db" # Default value if not provided

    model_config = SettingsConfigDict(env_file=".env")

# Create a singleton instance
settings = Settings()
