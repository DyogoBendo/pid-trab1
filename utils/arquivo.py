import cv2

# Função auxiliar apenas para abrir a imagem como matriz
def ler_imagem(caminho):
    return cv2.imread(caminho)

# Função auxiliar para salvar a matriz resultante como imagem
def salvar_imagem(caminho, imagem_matriz):
    cv2.imwrite(caminho, imagem_matriz)
