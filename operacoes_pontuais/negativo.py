import numpy as np
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