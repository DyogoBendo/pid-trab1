import numpy as np
# =====================================================================
# 5. APLICA O LOG
# =====================================================================

def log(imagem, fator=10):
    # Garante que o fator seja pelo menos 1 para evitar divisão por zero
    f = max(1.0, float(fator))
    
    # Normaliza a imagem original para a escala de 0.0 a 1.0
    r = imagem.astype(np.float32) / 255.0
    
    # Calcula a constante 'c' para garantir que o branco máximo não passe de 255
    c = 255.0 / np.log(1.0 + f)
        
    # Aplica a fórmula: c * ln(1 + fator * pixel)
    imagem_resultado = c * np.log(1.0 + (f * r))
    
    return np.clip(imagem_resultado, 0, 255).astype(np.uint8)