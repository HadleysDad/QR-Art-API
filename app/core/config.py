from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_host: str = "0.0.0.0"
    app_port: int = 8000
    log_level: str = "info"

    # Feature flags (mirror RapidAPI plan gating)
    allow_svg_for_free: bool = False
    allow_logo_for_free: bool = False
    
    # Storage
    supabase_url: str | None = None
    supabase_key: str | None = None
    s3_endpoint: str | None = None
    s3_bucket: str | None = None
    s3_access_key: str | None = None
    s3_secret_key: str | None = None
    
    # Upload / generation limits (server-side safety)
    max_upload_mb: int = 5
    max_size_px: int = 2000
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()