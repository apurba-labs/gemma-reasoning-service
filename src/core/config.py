from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Core Service Config
    APP_NAME: str = "Gemma-Bridge"
    APP_ENV: str = "development" # Added
    DEBUG: bool = True
    PORT: int = 8001
    
    # AI Model Configuration
    GEMMA_MODEL_ENDPOINT: str
    GEMMA_MODEL_NAME: str = "gemma2:9b"
    REASONING_CONFIDENCE_THRESHOLD: float = 0.85 # Added
    
    # Security
    API_BEARER_TOKEN: str # Added
    
    # This tells Pydantic to ignore extra fields instead of crashing
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore" 
    )

settings = Settings()