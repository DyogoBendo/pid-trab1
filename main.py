import cv2
import numpy as np

# Função auxiliar apenas para abrir a imagem como matriz
def ler_imagem(caminho):
    return cv2.imread(caminho)

# Função auxiliar para salvar a matriz resultante como imagem
def salvar_imagem(caminho, imagem_matriz):
    cv2.imwrite(caminho, imagem_matriz)

# =====================================================================
# 1. CONVERSÃO RGB PARA ESCALA DE CINZA
# =====================================================================
def rgb_para_cinza(img_colorida):
    altura, largura, canais = img_colorida.shape
    # Cria uma nova matriz vazia para a imagem em tons de cinza
    img_cinza = np.zeros((altura, largura), dtype=np.uint8)
    
    for y in range(altura):
        for x in range(largura):
            # O OpenCV lê no formato BGR (Azul, Verde, Vermelho)
            b, g, r = img_colorida[y, x]
            
            # Fórmula padrão da luminância vista em aula
            # L = R*0.299 + G*0.587 + B*0.114
            cinza = int((r * 0.299) + (g * 0.587) + (b * 0.114))
            img_cinza[y, x] = cinza
            
    return img_cinza

# =====================================================================
# 2. NEGATIVO DA IMAGEM
# =====================================================================
def negativo(img_cinza):
    altura, largura = img_cinza.shape
    img_negativo = np.zeros((altura, largura), dtype=np.uint8)
    
    for y in range(altura):
        for x in range(largura):
            # O negativo é o valor máximo (255) menos o valor do pixel atual
            img_negativo[y, x] = 255 - img_cinza[y, x]
            
    return img_negativo

# =====================================================================
# 3. THRESHOLD MANUAL
# =====================================================================
def threshold(img_cinza, limiar):
    altura, largura = img_cinza.shape
    img_limiar = np.zeros((altura, largura), dtype=np.uint8)
    
    for y in range(altura):
        for x in range(largura):
            # Se o pixel for maior que o limiar, vira branco (255)
            # Caso contrário, vira preto (0)
            if img_cinza[y, x] >= limiar:
                img_limiar[y, x] = 255
            else:
                img_limiar[y, x] = 0
                
    return img_limiar

# =====================================================================
# 4. FILTRO PASSA-BAIXA BÁSICO / MÉDIA
# =====================================================================
def passa_baixa_media(img_cinza, tamanho_mascara=3):
    altura, largura = img_cinza.shape
    img_borrada = np.zeros((altura, largura), dtype=np.uint8)
    
    # Offset é a borda que ignoramos para não dar erro de índice fora da matriz
    offset = tamanho_mascara // 2 
    
    # Varre a imagem ignorando as bordas extremas
    for y in range(offset, altura - offset):
        for x in range(offset, largura - offset):
            
            soma_pixels = 0
            
            # Varre a vizinhança (a máscara 3x3) ao redor do pixel central
            for my in range(-offset, offset + 1):
                for mx in range(-offset, offset + 1):
                    soma_pixels += img_cinza[y + my, x + mx]
            
            # Calcula a média da região
            media = soma_pixels // (tamanho_mascara * tamanho_mascara)
            img_borrada[y, x] = media
            
    return img_borrada

# =====================================================================
# EXECUÇÃO DO CÓDIGO
# =====================================================================
if __name__ == "__main__":
    # Carrega a matriz original
    img_original = ler_imagem("cat.jpg")
    
    # 1. Converte para cinza
    print("Convertendo para escala de cinza...")
    img_cinza = rgb_para_cinza(img_original)
    salvar_imagem("01_escala_cinza.jpg", img_cinza)
    
    # 2. Aplica o Negativo
    print("Gerando negativo...")
    img_neg = negativo(img_cinza)
    salvar_imagem("02_negativo.jpg", img_neg)
    
    # 3. Aplica Limiarização (Binarização com limiar de 127)
    print("Aplicando limiarização...")
    img_thresh = threshold(img_cinza, limiar=127)
    salvar_imagem("03_limiar.jpg", img_thresh)
    
    # 4. Aplica Filtro Passa-Baixa (Suavização Média 3x3)
    print("Aplicando filtro passa-baixa (Média)...")
    img_media = passa_baixa_media(img_cinza, tamanho_mascara=3)
    salvar_imagem("04_passa_baixa.jpg", img_media)
    
    print("Processamento concluído!")