import segno
import io
import base64
from PIL import Image, ImageDraw
from PIL.Image import Resampling
from typing import Optional, Tuple
import re

def generate_qr_svg_bytes(data: str, scale: int = 4, dark: str = "#000000", light: str = "#ffffff") -> bytes:
    qr = segno.make(data, micro=False)
    buf = io.BytesIO()
    qr.save(buf, kind='svg', xmldecl=False, unit='px', scale=scale, color=dark, background=light)
    return buf.getvalue()

def _extract_viewbox_size(svg_text: str) -> Tuple[int,int]:
    m = re.search(r'viewBox="0 0 (\d+) (\d+)"', svg_text)
    if m:
        return int(m.group(1)), int(m.group(2))
    m2 = re.search(r'width= "([\d.]+)"', svg_text)
    if m2:
        w = int(float(m2.group(1)))
        return w, w
    # fallback
    return 300,300

def embed_raster_logo_in_svg(svg_bytes: bytes, logo_bytes: bytes, logo_mime: Optional [str]="image/png", logo_scale: float=0.2, anchor: Tuple[float,float]=(0.5,0.5)) -> bytes:
    svg_text = svg_bytes.decode("utf-8")
    width, height = _extract_viewbox_size(svg_text)
    logo_px = int(min(width, height) * logo_scale)
    b64 = base64.b64decode(logo_bytes).decode("ascii")
    data_uri = f"data:{logo_mime};base64, {b64}"
    x = int((width - logo_px) * anchor[0])
    y = int((height - logo_px) * anchor[1])
    image_tag = f'<image x="{x}" y="{y}" width="{logo_px}" height="{logo_px}" preserveAspectRatio="xMidYMid meet" href="{data_uri}" />'
    svg_text = svg_text.replace("</svg>", image_tag + "</svg>")
    return svg_text.encode("utf-8")

def generate_png_with_logo(data: str, size: int=800, logo_bytes: Optional[bytes]=None, logo_scale: float=0.2) -> bytes:
    qr = segno.make(data, micro=False)
    buf = io.BytesIO()
    # Use segno's PNG serializer
    qr.save(buf, kind='png', scale=1, border=4)
    buf.seek(0)
    img = Image.open(buf).convert("RGBA")
    img = img.resize((size, size), Resampling.NEAREST)
    if logo_bytes:
        logo = Image.open(io.BytesIO(logo_bytes)).convert("RGBA")
        logo_px = int(size * logo_scale)
        logo.thumbnail((logo_px, logo_px), Resampling.LANCZOS)
        lx = (size - logo.width) // 2
        ly = (size -logo.height) // 2
        img.paste(logo, (lx, ly), mask=logo)
    out = io.BytesIO()
    img.save(out, format="PNG")
    return out.getvalue()