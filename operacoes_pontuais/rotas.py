from fastapi import APIRouter, UploadFile, File
from utils.utils import processar_imagem

from .escala_cinza import rgb_para_cinza
from .negativo import negativo
from .transformacao_logaritmica import transformacao_logaritmica

router = APIRouter()

@router.post("/escala-cinza")
async def processa_escala_cinza(file: UploadFile = File(...)):
    return await processar_imagem(file, rgb_para_cinza)

@router.post("/negativo")
async def processa_negativo(file: UploadFile = File(...)):
    return await processar_imagem(file, negativo)

@router.post("/transformacao-logaritmica")
async def processa_transformacao_logaritmica(file: UploadFile = File(...)):
    return await processar_imagem(file, transformacao_logaritmica)
    