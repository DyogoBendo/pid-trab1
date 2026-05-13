from fastapi import APIRouter, UploadFile, File
from utils.utils import processar_imagem
from .limiarizacao import limiarizacao
from .otsu import segmentacao_otsu
from .crescimento_regioes import segmentacao_crescimento_regioes

router = APIRouter()

@router.post("/limiarizacao")
async def processa_limiarizacao(limiar: int = 128, file: UploadFile = File(...)):
    return await processar_imagem(file, limiarizacao, limiar=limiar)

@router.post("/otsu")
async def aplicar_segmentacao_otsu(file: UploadFile = File(...)):
    return await processar_imagem(file, segmentacao_otsu)

@router.post("/crescimento-regioes")
async def aplicar_segmentacao_otsu(tolerancia: int = 20, file: UploadFile = File(...)):
    return await processar_imagem(file, segmentacao_crescimento_regioes, tolerancia=tolerancia)