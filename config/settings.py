from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    # Database
    DATABASE_URL: str
    
    # WhatsApp
    WHATSAPP_PHONE_NUMBER_ID: str
    WHATSAPP_ACCESS_TOKEN: str
    WHATSAPP_VERIFY_TOKEN: str
    WHATSAPP_WEBHOOK_URL: str
    
    # Claude AI
    CLAUDE_API_KEY: str
    CLAUDE_MODEL: str = "claude-3-sonnet-20240229"
    
    # Redis
    REDIS_URL: str
    
    # Application
    SECRET_KEY: str
    DEBUG: bool = False
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    
    # Clinic
    CLINIC_NAME: str
    CLINIC_TIMEZONE: str = "Europe/London"
    CLINIC_PHONE: str
    CLINIC_EMAIL: str
    
    # Email
    SMTP_HOST: str
    SMTP_PORT: int = 587
    SMTP_USERNAME: str
    SMTP_PASSWORD: str
    
    class Config:
        env_file = ".env"


settings = Settings()