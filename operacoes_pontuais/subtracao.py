import numpy as np

# =====================================================================
# 4. FAZ A DIFERENCA ABSOLUTA ENTRE DUAS IMAGENS
# =====================================================================

# Assume que as duas imagens possuem as mesmas resoluções e estão em tons de cinza
# Faz a diferenca absoluta
def subtracao(primeira_imagem, segunda_imagem):

    # Transforma para ponto flutuante para evitar underflow
    img1 = primeira_imagem.astype(np.float32)
    img2 = segunda_imagem.astype(np.float32)

    # Subtrai a segunda imagem da primeira
    diff = img1 - img2

    # Transforma valores negativos em positivos
    res = np.abs(diff)
    
    # Converte para o formato padrao 8 bits sem sinal
    return res.astype(np.uint8)