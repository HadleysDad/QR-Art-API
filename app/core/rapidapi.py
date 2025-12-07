from fastapi import Header, HTTPException
from .config import settings
from typing import Optional

# Rapid runtime sends headers such as X-RapidAPI-Key, X-RapidAPI-Host, X-Forwarded-Host
# You may also configure custom tokens in Studio to forward plan metadata (e.g. x-rapidapi-plan)
# If RapidAPI doesn't send plan info, you can map X-RapidAPI-Key via your own backend call (optional).

def get_rapidapi_plan(
  x_rapidapi_key: Optional[str] = Header(None, convert_underscores=False),
  x_rapidapi_host: Optional[str] = Header(None, convert_underscores=False),
  x_rapidapi_plan: Optional[str] = Header(None, alias="x-rapidapi-plan", convert_underscores=False),
  x_forward_host: Optional[str] = Header(None, convert_underscores=False)
) -> str:
    
    """
    Return 'free' or 'paid' depending on headers RapidAPI sends.
    Best practice: configure RapidAPI Studio to forward a header like x-rapidapi-plan containing the plan name.
    If no plan header exists, default to 'free'. This function can be extended to call RapidAPI's management APIs for verification.
    """
    # Basic check: Radpid runtime should forward an app key; if not present, reject
    if not x_rapidapi_key:
        raise HTTPException(status_code=401, detail="Missing RapidAPI key header")
    
    # If RapidAPI has forwarded which plan, use it
    if x_rapidapi_plan:
        plan = x_rapidapi_plan.lower()
        if "paid" in plan or "pro" in plan or "premium" in plan:
            return "paid"
        return "free"
    
    # Otherwise fefault to free - recommeneded: configure Studio to forward a plan header.
    return "free"
    