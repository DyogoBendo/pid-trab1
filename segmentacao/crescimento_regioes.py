import numpy as np

vizinhos = [
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),          ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1)
    ]

def segmentacao_crescimento_regioes(img_cinza, x, y, tolerancia=20):
    altura, largura = img_cinza.shape    
    img_resultado = np.zeros((altura, largura), dtype=np.uint8)        
        
    pontos_verificar = []                        
    pontos_verificar.append((x, y, int(img_cinza[x, y])))
    img_resultado[x, y] = 255  
                
    while len(pontos_verificar) > 0:                
        y_atual, x_atual, valor_semente_base = pontos_verificar.pop()                
        for vy, vx in vizinhos:
            y_viz = y_atual + vy
            x_viz = x_atual + vx                        
            if 0 <= y_viz < altura and 0 <= x_viz < largura and img_resultado[y_viz, x_viz] == 0:                                                                    
                    pixel_vizinho = int(img_cinza[y_viz, x_viz])                                        
                    if abs(pixel_vizinho - valor_semente_base) <= tolerancia:                                            
                        img_resultado[y_viz, x_viz] = 255                                            
                        pontos_verificar.append((y_viz, x_viz, valor_semente_base))
                        
    return img_resultado