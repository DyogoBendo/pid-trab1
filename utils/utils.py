import cv2
import numpy as np
import io
from fastapi.responses import StreamingResponse
from fastapi import UploadFile, HTTPException, Response, File
from operacoes_pontuais.escala_cinza import rgb_para_cinza

async def preparar_imagem(file: UploadFile):    
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    if img is None:
        raise HTTPException(status_code=400, detail="Arquivo de imagem inválido.")    
        
    return rgb_para_cinza(img)

def codificar_imagem(img):
    success, encoded_image = cv2.imencode('.jpg', img)
    if not success:
        raise HTTPException(status_code=500, detail="Falha ao codificar a imagem.")
    
    return Response(content=encoded_image.tobytes(), media_type="image/jpeg")


async def processar_imagem(file: UploadFile, funcao_filtro, **kwargs):            
    img_base = await preparar_imagem(file)
    img_processada = funcao_filtro(img_base, **kwargs)
    return codificar_imagem(img_processada)

async def processar_par_imagem(file1: UploadFile, file2: UploadFile, funcao_filtro, **kwargs):            
    img_base1 = await preparar_imagem(file1)
    img_base2 = await preparar_imagem(file2)
    
    altura, largura = img_base1.shape[:2]
    img_base2_redimensionada = cv2.resize(img_base2, (largura, altura))
    
    img_processada = funcao_filtro(img_base1, img_base2_redimensionada, **kwargs)
    return codificar_imagem(img_processada)

