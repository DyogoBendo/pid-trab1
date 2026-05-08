import numpy as np

def gerar_kernel_gaussiano(tamanho, sigma):
    """Gera a matriz de pesos baseada na função Gaussiana."""
    kernel = np.zeros((tamanho, tamanho))
    meio = tamanho // 2
    soma = 0.0
    
    for y in range(-meio, meio + 1):
        for x in range(-meio, meio + 1):
            # Fórmula de Gauss
            valor = (1 / (2 * np.pi * sigma**2)) * np.exp(-(x**2 + y**2) / (2 * sigma**2))
            kernel[y + meio, x + meio] = valor
            soma += valor
            
    # Normaliza o kernel para que a soma de todos os pesos seja 1 (evita escurecer/clarear a imagem)
    return kernel / soma

def passa_baixa_gaussiano(img_cinza, tamanho_mascara=3, sigma=1.0):
    altura, largura = img_cinza.shape
    img_borrada = np.zeros((altura, largura), dtype=np.uint8)
    
    # Gera os pesos
    kernel = gerar_kernel_gaussiano(tamanho_mascara, sigma)
    offset = tamanho_mascara // 2
    
    # Varre a imagem
    for y in range(offset, altura - offset):
        for x in range(offset, largura - offset):
            
            # Extrai a região da imagem do mesmo tamanho do kernel (Slicing do NumPy)
            regiao = img_cinza[y - offset : y + offset + 1, x - offset : x + offset + 1]
            
            # Multiplica a região pelo kernel Gaussiano e soma tudo
            valor_pixel = np.sum(regiao * kernel)
            
            # Garante que o valor fique no limite de 0 a 255
            img_borrada[y, x] = np.clip(valor_pixel, 0, 255)
            
    return img_borrada