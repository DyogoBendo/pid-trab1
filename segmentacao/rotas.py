from fastapi import APIRouter, UploadFile, File
from utils.utils import processar_imagem
from .limiarizacao import limiarizacao

router = APIRouter()

@router.post("/limiarizacao")
async def processa_limiarizacao(limiar: int = 128, file: UploadFile = File(...)):
    return await processar_imagem(file, limiarizacao, limiar=limiar)
    