import numpy as np

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