from fastapi import APIRouter, UploadFile, File
from utils.utils import processar_imagem
from .passa_alta_alto_reforco import passa_alta_alto_reforco
from .passa_alta_basico import passa_alta_basico
from .passa_alta_prewitt import passa_alta_prewitt
from .passa_alta_roberts import passa_alta_roberts
from .passa_alta_sobel import passa_alta_sobel

router = APIRouter()    

@router.post("/alto-reforco")
async def process_passa_alta_alto_reforco(tamanho_mascara: int = 3, A: float = 1.1, file: UploadFile = File(...)):    
    return await processar_imagem(file, passa_alta_alto_reforco, tamanho_mascara=tamanho_mascara, A=A)

@router.post("/basico")
async def process_passa_alta_basico(tamanho_mascara: int = 3, file: UploadFile = File(...)):    
    return await processar_imagem(file, passa_alta_basico, tamanho_mascara=tamanho_mascara)

@router.post("/prewitt")
async def process_passa_alta_basico(file: UploadFile = File(...)):    
    return await processar_imagem(file, passa_alta_prewitt)

@router.post("/roberts")
async def process_passa_alta_basico(file: UploadFile = File(...)):    
    return await processar_imagem(file, passa_alta_roberts)

@router.post("/sobel")
async def process_passa_alta_basico(file: UploadFile = File(...)):    
    return await processar_imagem(file, passa_alta_sobel)