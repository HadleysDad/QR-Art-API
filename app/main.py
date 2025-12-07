from fastapi import FastAPI
from app.api.v1.endpoints import router as v1_router
from app.core.config import settings
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="QR Art API", version="1.0.0")
app.include_router(v1_router, prefix="/api/v1")

# Allowed origins (where requests can come from)
origins = [
    "https://rapidapi.com",  # RapidAPI console
    "https://your-frontend-domain.com",  # Optional: your web frontend
    "*"  # Allow all origins temporarily (good for testing)
]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, # Origins that can call your API
    allow_credentials=True, # Allows cookies, credentials
    allow_methods=["*"], # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"]  # Allow all headers (like X-API-Key)
)

@app.get("/")
def root():
    return {"message": "QR Art API", "version": "1.0.0"}