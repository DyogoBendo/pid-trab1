from fastapi import APIRouter, UploadFile, File
from utils.utils import processar_imagem, preparar_imagem
from .calculo_histograma import calculo_histograma
from .equalizacao import equalizacao_histograma

router = APIRouter()    

@router.post("/frequencia")
async def processa_histograma(file: UploadFile = File(...)):
    img = await preparar_imagem(file)
    histograma = calculo_histograma(img)    
    return {"frequencias": histograma.tolist()}    

@router.post("/equalizacao")
async def aplicar_equalizacao_histograma(file: UploadFile = File(...)):
    return await processar_imagem(file, equalizacao_histograma)