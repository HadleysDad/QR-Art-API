📦 QR Art Generator API
Free PNG & SVG QR Code Generator with Logo Support — FastAPI + Python

The QR Art Generator API is a production-ready FastAPI service that generates:

High-resolution PNG QR codes

Scalable SVG QR codes

Color-customized QR codes

QR codes with centered logo overlays

Artistic, brand-friendly QR outputs

The API is fully compatible with RapidAPI and free to run on platforms like Render.

🚀 Features
✓ PNG Output

Crisp high-resolution PNG images

Custom output size

Custom dark/light colors

Optional logo overlay

✓ SVG Output

Fully scalable vector QR codes

Custom color support

Optional raster logo embedding

✓ Logo Support

Upload PNG/JPG logos

Automatic scaling

Auto-centered

Transparency support

✓ Secure & Production-Ready

CORS protection

Input validation using Pydantic

SVG sanitization

No secrets required to run locally

✓ RapidAPI-Ready

Forward URL compatible

Separate free/paid capabilities possible

Automatic key + host handling

📁 Project Structure
qr-art-api/
│
├── app/
│   ├── main.py
│   ├── endpoints.py
│   ├── qr_service.py
│   ├── settings.py
│   ├── schemas.py
│   └── utils/
│
├── tests/
│   └── test_generate.py
│
├── requirements.txt
├── .gitignore
├── .env.example
└── README.md

⚙️ Installation (Local Development)
1. Clone the Repository
git clone https://github.com/YOUR_USERNAME/qr-art-api.git
cd qr-art-api

2. Create a Virtual Environment
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

3. Install Dependencies
pip install -r requirements.txt

4. Configure Environment Variables

Copy the example file:

cp .env.example .env


Edit .env as needed.

▶️ Running the API (Local)

Start the server using Uvicorn:

uvicorn app.main:app --reload


Visit Swagger docs:

👉 http://127.0.0.1:8000/docs

This allows full testing including logo uploads.

🧪 Example Usage (Swagger / cURL)
Generate PNG
curl -X POST "http://127.0.0.1:8000/api/v1/generate" \
  -F "data=Hello World" \
  -F "format=png" \
  -F "size=400" \
  --output qr.png

Generate SVG
curl -X POST "http://127.0.0.1:8000/api/v1/generate" \
  -F "data=Hello" \
  -F "format=svg" \
  --output qr.svg

PNG with Logo
curl -X POST "http://127.0.0.1:8000/api/v1/generate" \
  -F "data=Brand" \
  -F "format=png" \
  -F "size=500" \
  -F "logo_file=@logo.png" \
  -F "logo_scale=0.22" \
  --output qr-branded.png

🌐 Deploying to Render

Push the repo to GitHub

Create a Render Web Service

Use these settings:

Build Command: pip install -r requirements.txt
Start Command: uvicorn app.main:app --host 0.0.0.0 --port 10000


Add environment variables:

ENV=production
ALLOWED_ORIGINS=*
MAX_QR_PX=1200


Your final URL will look like:

https://qr-art-api.onrender.com


Swagger is at:

https://qr-art-api.onrender.com/docs

🔑 RapidAPI Integration

The API is fully compatible with RapidAPI's forward proxy.

What RapidAPI Handles:

✔ API keys
✔ Rate limiting
✔ Throttling
✔ Billing tiers
✔ Analytics
✔ Marketplace listing

How to Connect:

In your RapidAPI dashboard → "General" → set the Base URL:

https://qr-art-api.onrender.com


Your users will call:

https://YOUR-RAPIDAPI-HOST.p.rapidapi.com/generate


RapidAPI forwards it automatically.

🧩 Environment Variables

Your .env should never be committed.
Use .env.example to guide users.

ENV=development
ALLOWED_ORIGINS=*
MAX_QR_PX=1200

# Optional (if user wants them)
RAPIDAPI_KEY=your_key_here
RAPIDAPI_HOST=your_host_here

🛡️ Security

✔️ No secrets required to run
✔️ CORS restricted by settings
✔️ File type validation
✔️ Limited logo scaling to prevent malicious uploads
✔️ SVG sanitized

🤝 Contributing

Pull requests welcome!
Feel free to submit:

New QR styling options

Gradient support

SVG filters

Performance improvements

Additional test cases

📄 License

MIT License — free to use and modify for commercial & personal projects.

⭐ Support

If you publish this on RapidAPI, consider linking the listing here so others can use it.

If you want, I can also generate:

✅ A RapidAPI marketing description
✅ A “Getting Started” client code section
✅ A visual banner for your README
Just tell me!