from fastapi import Header, HTTPException, Request
from typing import Optional

def get_rapidapi_plan(
    request: Request,   # <-- add this so we can read raw headers
    x_rapidapi_key: Optional[str] = Header(None, alias="X-RapidAPI-Key", convert_underscores=False),
    x_rapidapi_host: Optional[str] = Header(None, alias="X-RapidAPI-Host", convert_underscores=False),
    x_rapidapi_plan: Optional[str] = Header(None, alias="x-rapidapi-plan", convert_underscores=False),
) -> str:
    # Fallback in case something still sends lowercase/underscores
    key = x_rapidapi_key or request.headers.get("x-rapidapi-key") or request.headers.get("X-RapidAPI-Key")
    
    if not key:
        raise HTTPException(status_code=401, detail="Missing RapidAPI key header")
    
    if x_rapidapi_plan and x_rapidapi_plan.lower() in {"paid", "pro", "premium"}:
        return "paid"
    
    return "free"