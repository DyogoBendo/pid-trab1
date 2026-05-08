import cv2
import numpy as np
import io
from fastapi.responses import StreamingResponse
from fastapi import File, UploadFile

async def ler_imagem(file: UploadFile = File(...)):
    contents = await file.read()

    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img

def codificar_imagem(img):
    success, encoded_image = cv2.imencode('.jpg', img)
    
    if not success:
        return {"error": "Failed to encode image."}
    return StreamingResponse(io.BytesIO(encoded_image.tobytes()), media_type="image/jpeg")