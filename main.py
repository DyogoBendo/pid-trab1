from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from filtros_espaciais.passa_baixa.rotas import router as rotas_passa_baixa
from filtros_espaciais.passa_alta.rotas import router as rotas_passa_alta
from histograma.rotas import router as rotas_histograma
from operacoes_aritmeticas.rotas import router as rotas_operacoes_aritmeticas
from operacoes_pontuais.rotas import router as rotas_operacoes_pontuais
from segmentacao.rotas import router as rotas_segmentacao

app = FastAPI(
    title="API de Processamento de Imagens",
    description="Implementação manual de algoritmos de PID",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(rotas_passa_baixa, prefix="/passa-baixa", tags=["Filtros Passa-Baixa"])
app.include_router(rotas_passa_alta, prefix="/passa-alta", tags=["Filtros Passa-Alta"])
app.include_router(rotas_operacoes_aritmeticas, prefix="/operacao-aritmetica", tags=["Operações Aritméticas"])
app.include_router(rotas_operacoes_pontuais, prefix="/operacao-pontual", tags=["Operações Pontuais"])
app.include_router(rotas_histograma, prefix="/histograma", tags=["Histograma"])
app.include_router(rotas_segmentacao, prefix="/segmentacao", tags=["Segmentação"])

uvicorn.run(app, host="0.0.0.0", port=8000)