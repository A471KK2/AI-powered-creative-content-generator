from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from services.text_service import generate_text
from services.image_service import generate_image
from fastapi.responses import StreamingResponse
import io

app = FastAPI()

# 🔥 VERY IMPORTANT (React needs this)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "API running"}

@app.get("/generate-text")
def text(prompt: str):
    result = generate_text(prompt)
    return {"result": result}

@app.get("/generate-image")
def image(prompt: str):
    img_bytes = generate_image(prompt)

    if img_bytes:
        return StreamingResponse(io.BytesIO(img_bytes), media_type="image/png")

    return {"error": "Failed"}