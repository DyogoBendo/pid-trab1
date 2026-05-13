import numpy as np

def normalizar_matriz(matriz_temp):
    """
    Recebe uma matriz com valores brutos (float) e aplica a re-escala Min-Max
    para retornar uma matriz de imagem válida (0 a 255 em inteiros).
    """
    
    altura, largura = matriz_temp.shape
    
    valor_minimo = float('inf')
    valor_maximo = float('-inf')
        
    for y in range(altura):
        for x in range(largura):
            valor = matriz_temp[y, x]
            if valor < valor_minimo:
                valor_minimo = valor
            if valor > valor_maximo:
                valor_maximo = valor
                    
    diferenca = valor_maximo - valor_minimo
    if diferenca == 0:
        diferenca = 1
            
    img_result = np.zeros((altura, largura), dtype=np.uint8)
    
    for y in range(altura):
        for x in range(largura):            
            pixel_proporcional = ((matriz_temp[y, x] - valor_minimo) / diferenca) * 255
            img_result[y, x] = int(pixel_proporcional)
            
    return img_result