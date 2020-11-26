import matplotlib.pyplot as plt
from math import sqrt

def correlacao(vetor_x, vetor_y):
    # calcula as médias de x e y
    media_x = calcular_media(vetor_x)
    media_y = calcular_media(vetor_y)

    # calcula o valor de cada uma das partes da função r
    r1 = 0 # guarda o resultado de [ soma de (x – média de x) * (y – média de y) ]
    r2 = 0 # guarda o resultado de  [ soma de (x – média de x)2 ]
    r3 = 0 # guarda o resultado de [ soma de (y – média de y)2 ]

    for i in range(len(vetor_x)):
        r1 += (vetor_x[i] - media_x) * (vetor_y[i] - media_y)
        r2 += (vetor_x[i] - media_x) ** 2
        r3 += (vetor_y[i] - media_y) ** 2

    # calcula o coeficiente da correlação r
    r = r1 / sqrt(r2 * r3)

    return r


def regressao (vetor_x, vetor_y):
    # calcula as médias de x e y
    media_x = calcular_media(vetor_x)
    media_y = calcular_media(vetor_y)

    # calcula o valor das partes de b1
    b1_1 = 0 # guarda o resultado de [ soma de (x – média de x) * (y – média de y) ]
    b1_2 = 0 # guarda o resultado de  [ soma de (x – média de x)2 ]

    for i in range(len(vetor_y)):
        b1_1 += (vetor_x[i] - media_x) * (vetor_y[i] - media_y)
        b1_2 += (vetor_x[i] - media_x) ** 2

    # calcula o valor de b1
    b1 = b1_1 / b1_2

    # calcula o valor de b0
    b0 = media_y - b1 * media_x

    return b0, b1


def calcular_media (vetor):
    tamanho = len(vetor)
    media = 0

    for i in range(tamanho):
        media += vetor[i]
    
    media /= tamanho

    return media


# Fase 1: Análise de Correlação e Regressão Linear

x1 = [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]
y1 = [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]
x2 = [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]
y2 = [9.14, 8.14, 8.47, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74]
x3 = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 19]
y3 = [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 5.56, 7.91, 6.89, 12.50]

def analisar_dados(vetor_x, vetor_y, titulo):
    # verifica se os vetores possuem o mesmo tamanho
    if len(vetor_x) != len(vetor_y):
        raise IndexError('Os vetores passados não tem o mesmo tamanho!')
    
    # busca valores dos coeficientes de correlação e regressão
    r = correlacao(vetor_x, vetor_y)
    b0, b1 = regressao(vetor_x, vetor_y)

    # adiciona reta de regressão no gráfico
    x = []
    y = []
    for i in range(max(vetor_x) + 1):
        x.append(i)
        y.append(b0 + b1 * i)

    plt.plot(x, y)
 
    # adiciona pontos no gráfico
    plt.plot(vetor_x, vetor_y, 'ro')
    plt.xlabel('x')  
    plt.ylabel('y')  
    
    # adiciona coeficientes
    #'r = ' + str(r) + '\nb0 = ' + str(b0) + '\nb1 = ' + str(b1)
    plt.title(titulo + f' - Correlação = {r:.5f}   B0 = {b0:.5f}   B1 = {b1:.5f}') 

    plt.show()

analisar_dados(x1, y1, 'Dataset 1')
analisar_dados(x2, y2, 'Dataset 2')
analisar_dados(x3, y3, 'Dataset 3')