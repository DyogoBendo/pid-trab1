from filtros_espaciais.passa_baixa.passa_baixa_media import passa_baixa_media
from filtros_espaciais.passa_baixa.passa_baixa_mediana import passa_baixa_mediana
from filtros_espaciais.passa_baixa.passa_baixa_gaussiana import passa_baixa_gaussiano
from operacoes_pontuais.escala_cinza import rgb_para_cinza
from operacoes_pontuais.negativo import negativo
from segmentacao.limiarizacao_simples import threshold   
from fastapi import FastAPI, File, UploadFile
from utils.utils import ler_imagem, codificar_imagem
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/process/grayscale")
async def process_grayscale(file: UploadFile = File(...)):
    img = await ler_imagem(file)
    if img is None:
        return {"error": "Invalid image file."}
    
    print("Convertendo para escala de cinza...")
    processed_img = rgb_para_cinza(img)

    return codificar_imagem(processed_img)

@app.post("/process/threshold")
async def process_threshold(value: int = 128, file: UploadFile = File(...)):
    img = await ler_imagem(file)
    if img is None:
        return {"error": "Invalid image file."}
    
    print("Convertendo para escala de cinza...")
    processed_img = rgb_para_cinza(img)
    processed_img = threshold(processed_img, value)

    return codificar_imagem(processed_img)

@app.post("/process/passa_baixa_media")
async def process_passa_baixa_media(kernel_size: int = 3, file: UploadFile = File(...)):
    img = await ler_imagem(file)
    if img is None:
        return {"error": "Invalid image file."}
    
    print("Convertendo para escala de cinza...")
    processed_img = rgb_para_cinza(img)
    
    print(f"Aplicando filtro Passa-Baixa (Média) com máscara {kernel_size}x{kernel_size}...")
    processed_img = passa_baixa_media(processed_img, kernel_size)

    return codificar_imagem(processed_img)

@app.post("/process/passa_baixa_mediana")
async def process_passa_baixa_media(kernel_size: int = 3, file: UploadFile = File(...)):
    img = await ler_imagem(file)
    if img is None:
        return {"error": "Invalid image file."}
    
    print("Convertendo para escala de cinza...")
    processed_img = rgb_para_cinza(img)
    
    print(f"Aplicando filtro Passa-Baixa (Mediana) com máscara {kernel_size}x{kernel_size}...")
    processed_img = passa_baixa_mediana(processed_img, kernel_size)

    return codificar_imagem(processed_img)

@app.post("/process/negativo")
async def process_negativo(file: UploadFile = File(...)):
    img = await ler_imagem(file)
    if img is None:
        return {"error": "Invalid image file."}
    
    print("Convertendo para escala de cinza...")
    processed_img = rgb_para_cinza(img)
    
    print(f"Aplicando filtro Negativo")
    processed_img = negativo(processed_img)

    return codificar_imagem(processed_img)

@app.post("/process/passa_baixa_gaussiano")
async def process_passa_baixa_gaussiano(
    tamanho_mascara: int = 3, 
    sigma: float = 1.0, 
    file: UploadFile = File(...)
):
    img = await ler_imagem(file)
    if img is None:
        return {"error": "Invalid image file."}
    
    # Validações de segurança
    if tamanho_mascara not in [3, 5]:
        tamanho_mascara = 3
    if sigma <= 0:
        sigma = 0.1
        
    print(f"Aplicando Gaussiano: Máscara {tamanho_mascara}x{tamanho_mascara}, Sigma {sigma}...")
    processed_img = rgb_para_cinza(img)
        
    processed_img = passa_baixa_gaussiano(processed_img, tamanho_mascara, sigma)

    return codificar_imagem(processed_img)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)