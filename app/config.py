import logging
 
from pydantic_settings import BaseSettings
 
log = logging.getLogger("uvicorn")
 
class Settings(BaseSettings):
    environment: str = "dev"
    testing: bool = bool(0)
 
def get_settings() -> Settings:
    log.info("Loading settings")
    return Settings()