import cv2
import numpy as np
import base64
from fastapi import UploadFile, HTTPException
from operacoes_pontuais.escala_cinza import rgb_para_cinza
from histograma.calculo_histograma import calculo_histograma

async def preparar_imagem(file: UploadFile):    
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    if img is None:
        raise HTTPException(status_code=400, detail="Arquivo de imagem inválido.")    
        
    return rgb_para_cinza(img)

def codificar_imagem(img):    
    sucesso, buffer_png = cv2.imencode('.png', img)
    if not sucesso:
        raise ValueError("Falha ao codificar a imagem")
        
    imagem_base64 = base64.b64encode(buffer_png).decode('utf-8')
        
    return {
        "imagem": imagem_base64,
        "histograma": calculo_histograma(img).tolist()
    }    


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

