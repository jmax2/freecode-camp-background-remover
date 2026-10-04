from fastapi import FastAPI, UploadFile, File, Response
from rembg import remove
from PIL import Image
import io
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500", "http://localhost:5500"], # L'indirizzo di Live Server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/remove-bg")
async def remove_bg(file: UploadFile = File(...)):
    image_bytes = await file.read()
    # image = Image.open(io.BytesIO(image_bytes))
    # output = remove(image)
    # buffer = io.BytesIO()
    # output.save(buffer, format="PNG")
    # buffer.seek(0)

    # return buffer.getvalue()
    output_bytes = remove(image_bytes)
    return Response(content=output_bytes, media_type="image/png")
