from fastapi.testclient import TestClient
from app.main import app
from app.core.config import settings

client = TestClient(app)

def test_health():
    r = client.get("/api/v1/health")
    assert r.status_code == 200

def test_png_free_no_logo():
    # Simulate RapidAPI header presence (Rapid will provide X-RapidAPI-Key)
    headers = {"x-rapidapi-key": "fake-key", "x-rapidapi-plan": "free"}
    r = client.post("/api/v1/generate", data={"data":"hello","format":"png","size":"400"}, headers=headers)
    assert r.status_code == 200
    assert r.headers["content-type"].startswith("image/png")

def test_svg_paid_allowed():
    headers = {"x-rapidapi-key": "fake-key", "x-rapidapi-plan": "paid"}
    r = client.post("/api/v1/generate", data={"data":"hello","format":"svg"}, headers=headers)
    assert r.status_code == 200
    assert "svg" in r.headers["content-type"]
