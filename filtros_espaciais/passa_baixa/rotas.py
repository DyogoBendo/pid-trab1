from fastapi import APIRouter, UploadFile, File
from utils.utils import processar_imagem

from .passa_baixa_media import passa_baixa_media
from .passa_baixa_mediana import passa_baixa_mediana
from .passa_baixa_gaussiana import passa_baixa_gaussiano
from .passa_baixa_max import passa_baixa_max
from .passa_baixa_min import passa_baixa_min

router = APIRouter()

@router.post("/media")
async def process_passa_baixa_media(tamanho_mascara: int = 3, file: UploadFile = File(...)):
    return await processar_imagem(file, passa_baixa_media, tamanho_mascara=tamanho_mascara)

@router.post("/mediana")
async def process_passa_baixa_media(tamanho_mascara: int = 3, file: UploadFile = File(...)):    
    return await processar_imagem(file, passa_baixa_mediana, tamanho_mascara=tamanho_mascara)

@router.post("/maximo")
async def process_passa_baixa_maximo(tamanho_mascara: int = 3, file: UploadFile = File(...)):    
    return await processar_imagem(file, passa_baixa_max, tamanho_mascara=tamanho_mascara)

@router.post("/minimo")
async def process_passa_baixa_min(tamanho_mascara: int = 3, file: UploadFile = File(...)):    
    return await processar_imagem(file, passa_baixa_min, tamanho_mascara=tamanho_mascara)

@router.post("/gaussiano")
async def process_passa_baixa_gaussiano( tamanho_mascara: int = 3,  sigma: float = 1.0, file: UploadFile = File(...)):
    return await processar_imagem(file, passa_baixa_gaussiano, tamanho_mascara=tamanho_mascara, sigma=sigma)