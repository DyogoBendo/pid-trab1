import numpy as np
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
