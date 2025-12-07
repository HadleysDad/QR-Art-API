from pydantic import BaseModel, Field

class GenerateRequest(BaseModel):
    data: str = Field(..., description="Content to encode")
    format: str = Field("svg", description="svg or png")
    size: int = Field(800, description="pixel size for PNG output (svg uses scale)")
    dark: str = Field("#000000")
    light: str = Field("#ffffff")
    logo_scale: float = Field(0.2, description="fraction of QR width the logo occupies")
    