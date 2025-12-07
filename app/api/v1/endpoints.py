from fastapi import APIRouter, File, UploadFile, Depends, Response, HTTPException, status, Form
from app.core.rapidapi import get_rapidapi_plan
from app.core.config import settings
from app.services.qr_service import (
    generate_qr_svg_bytes, embed_raster_logo_in_svg, generate_png_with_logo
)
from app.api.v1.schemas import GenerateRequest
from typing import Optional

router = APIRouter()

@router.get("/health", tags=["health"])
def health():
    return {"status": "ok"}

@router.post("/generate", tags=["generate"])
async def generate(
    data: str = Form(None),
    format: str = Form("svg"),
    size: int = Form(800),
    dark: str = Form("#000000"),
    light: str = Form("#ffffff"),
    logo_scale: float = Form(0.2),
    logo: UploadFile = File(None),
    plan: str = Depends(get_rapidapi_plan)
):
    # prefer form data (multipart) since logo upload is multipar; clients may also POST JSON and no logo
    if not data:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="'data' is required")
    
    fmt = (format or "svg").lower()
    
    # Feature gating based on plan
    
    allow_svg = settings.allow_svg_for_free or plan == "paid"
    allow_logo = settings.allow_logo_for_free or plan == "paid"
    
    if fmt == "svg" and not allow_svg:
        raise HTTPException(status_code=403, detail="SVG output is restriced to paid plan")
    
    if logo and not allow_logo:
        raise HTTPException(status_code=403, detail="Logo uploads are restriced to paid plans")
    
    # Basic upload size guard
    if logo: 
        content = await logo.read()
        mb = len(content) / (1024 * 1024)
        if mb > settings.max_upload_mb:
            raise HTTPException(status_code=413, detail=f"Uploaded logo exceeds {settings.max_upload_mb} MB limit")
        logo_bytes = content
        logo_mime = logo.content_type or "image/png"
    else:
        logo_bytes = None
        logo_mime = None
    
    if fmt == "svg":
        # Use segno to get SVG bytes; embed logo if provided
        svg_bytes = generate_qr_svg_bytes(data, scale=max(1, size//100), dark=dark, light=light)
        if logo_bytes:
            svg_bytes = embed_raster_logo_in_svg(svg_bytes, logo_bytes, logo_mime, logo_scale)
        return Response(content=svg_bytes, media_type="image/svg+xml")
    elif fmt == "png":
        png = generate_png_with_logo(data, size=min(size, settings.max_size_px), logo_bytes=logo_bytes, logo_scale=logo_scale)
        return Response(content=png, media_type="image/png")
    else:
        raise HTTPException(status_code=400, detail="Unsupported format")
    
    