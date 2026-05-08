import numpy as np
# =====================================================================
# 6. APLICA DIVISAO
# =====================================================================

# Assume que as duas imagens possuem as mesmas resoluções
# Assume que as duas imagems estão na escala de cinza
def div(primeira_imagem, segunda_imagem):

    img1 = primeira_imagem.astype(np.float32)
    img2 = segunda_imagem.astype(np.float32)

    img2_segura = np.where(img2 == 0, 1e-5, img2)

    res = img1 / img2_segura

    minimo = res.min()
    maximo = res.max()

    if maximo == minimo:
        imagem_resultado = np.zeros_like(res)
    else:
        imagem_resultado = (res - minimo) / (maximo - minimo) * 255.0

    return np.clip(imagem_resultado, 0, 255).astype(np.uint8)