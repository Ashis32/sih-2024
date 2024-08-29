from fastapi import FastAPI, File, UploadFile  # Import File and UploadFile
from PIL import Image
import io

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI server!"}

@app.post("/upload/")
async def upload_image(image: UploadFile = File(...)):
    try:
        img = Image.open(io.BytesIO(await image.read()))
        # Here you can add code to pass the image to the ML model
        return {"message": "Image received successfully"}
    except Exception as e:
        return {"error": str(e)}
