import numpy as np
# =====================================================================
# 5. APLICA MULTIPLICACAO
# =====================================================================

# Assume que as duas imagens possuem as mesmas resoluções
# Assume que as duas imagems estão na escala de cinza
def mult(primeira_imagem, segunda_imagem):
    
    img1 = primeira_imagem.astype(np.float32)
    img2 = segunda_imagem.astype(np.float32)

    imagem_resultado = img1 * (img2 / 255.0)

    return np.clip(imagem_resultado, 0, 255).astype(np.uint8)