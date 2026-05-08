import numpy as np

def passa_baixa_mediana(img_cinza, tamanho_mascara=3):
    altura, largura = img_cinza.shape
    # Cria a imagem de saída vazia (preta)
    img_borrada = np.zeros((altura, largura), dtype=np.uint8)
    
    # Offset é a borda que ignoramos para não dar erro de índice fora da matriz
    offset = tamanho_mascara // 2 
    
    # Varre a imagem ignorando as bordas extremas
    for y in range(offset, altura - offset):
        for x in range(offset, largura - offset):
            
            # Lista para guardar os valores dos pixels vizinhos
            vizinhanca = []
            
            # Varre a vizinhança (a máscara) ao redor do pixel central
            for my in range(-offset, offset + 1):
                for mx in range(-offset, offset + 1):
                    vizinhanca.append(img_cinza[y + my, x + mx])
            
            # Ordena a lista de pixels do menor para o maior
            vizinhanca.sort()
            
            # Encontra o índice do meio da lista
            # Ex: Se a máscara for 3x3, a lista terá 9 itens. O meio é 9 // 2 = 4 (o 5º elemento)
            indice_meio = len(vizinhanca) // 2
            
            # Extrai o valor da mediana e aplica na imagem
            mediana = vizinhanca[indice_meio]
            img_borrada[y, x] = mediana
            
    return img_borrada