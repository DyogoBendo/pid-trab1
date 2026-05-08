import numpy as np

# =====================================================================
# 3. SOMA DUAS IMAGENS
# =====================================================================

# Assume que as duas imagens possuem as mesmas resoluções e estão em tons de cinza
# Normaliza a imagem
def soma(primeira_imagem, segunda_imagem):

    # Converte para ponto flutuante para evitar overflow ou erros de precisao
    img1 = primeira_imagem.astype(np.float32)
    img2 = segunda_imagem.astype(np.float32)

    #Soma as duas imagens
    soma_img = img1 + img2 

    # Encontra o maximo e o minimo das imagens somadas
    minimo = soma_img.min()
    maximo = soma_img.max()
        
    # Evita divisao por zero caso o maximo e o minimo sejem iguais
    if maximo == minimo:
        imagem_resultado = np.zeros_like(soma_img)
    else:
        imagem_resultado = (soma_img - minimo) / (maximo - minimo) * 255.0
                
    # Converte para o formato padrao 8 bits sem sinal
    return imagem_resultado.astype(np.uint8)