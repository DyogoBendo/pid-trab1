from fastapi import APIRouter, UploadFile, File
from utils.utils import processar_par_imagem
from .divisao import divisao
from .multiplicacao import multiplicacao
from .soma import soma
from .subtracao import subtracao

router = APIRouter()    

@router.post("/soma")
async def processa_soma(file1: UploadFile = File(...), file2: UploadFile = File(...)):
    return await processar_par_imagem(file1,file2, soma)

@router.post("/subtracao")
async def processa_soma(file1: UploadFile = File(...), file2: UploadFile = File(...)):
    return await processar_par_imagem(file1,file2, subtracao)

@router.post("/divisao")
async def processa_soma(file1: UploadFile = File(...), file2: UploadFile = File(...)):
    return await processar_par_imagem(file1,file2, divisao)

@router.post("/multiplicacao")
async def processa_soma(file1: UploadFile = File(...), file2: UploadFile = File(...)):
    return await processar_par_imagem(file1,file2, multiplicacao)