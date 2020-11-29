import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from pylab import figure
from math import sqrt
import numpy as np
import csv

def calcular_media (vetor):
    tamanho = len(vetor)
    media = 0

    for i in range(tamanho):
        media += vetor[i]
    
    media = media / tamanho

    return media


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

def regmultipla(x, y):
    # calcula os valores de beta por partes, sendo que 𝛽 = [(Xt X)**-1] * Xt * y
    b = np.dot(x.T, x) #  (Xt X)
    b = np.power(b, -1)     #  (Xt X) ** -1
    b = np.dot(b, x.T) # [(Xt X) ** -1] * Xt
    b = np.dot(b, np.matrix(y).T)   # [(Xt X) ** -1] * Xt * y

    return b


def ler_arquivo():
    # abre o arquivo para leitura (o arquivo fica na pasta atual)
    with open('data.csv', 'r') as ficheiro:
        reader = csv.reader(ficheiro)
        x = [] 
        y = []
        for linha in reader:
            # lê as linhas do arquivo e separa cada informação (tamanho da casa, número de quartos e preço) 
            # converte as informações para seus devidos 'tipos' para que não fiquem como string
            # tamanho da casa e número de quartos são guardados na matriz x, cada um sendo uma coluna
            # preço é salvo na lista y
            
            linha[0] = int(linha[0])
            linha[1] = int(linha[1])

            # se existe o caracter 'e' na string, pega o valor até aquela posição, senão pode 
            # pegar o valor presenta na string inteira
            linha[2] = float( linha[2][:linha[2].find('e')]  if  linha[2].find('e') != -1  else  linha[2] )

            x.append(linha[0:2])
            y.append(linha[2])
    
    x = np.matrix(x) # cria uma matriz para x, para que fique mais fácil fazer operações com as colunas
    return x, y

def analisar_dados(entrada_x, entrada_y):

    # gera a matrix x com Xi0 = 1
    x = np.hstack((np.ones((len(entrada_y), 1)), entrada_x))

    # busca a correlação e regressão para tamanho de casa e preço
    tp_r = correlacao(entrada_x[:,0].A1, entrada_y)
    tp_b0, tp_b1 = regressao(entrada_x[:,0].A1, entrada_y)

    # busca a correlação e regressão para número de quartos e preço
    qp_r = correlacao(entrada_x[:,1].A1, entrada_y)
    qp_b0, qp_b1 = regressao(entrada_x[:,1].A1, entrada_y)

    # calcula os valores de beta
    b = regmultipla(x, entrada_y)

    # cria gráfico 3D
    fig = figure()
    ax = Axes3D(fig)
    
    for i in range(len(entrada_y)):
        # adiciona os dados de entrada ao gráfico
        ax.scatter3D(entrada_x[i,0], entrada_x[i, 1].tolist(), entrada_y[i], c='red')

    # cria linha de regressão e adiciona ao gráfico
    y = np.dot(x, b)
    ax.plot(entrada_x[:,0].A1, entrada_x[:,1].A1, y.A1)

    # apresenta o gráfico
    tp_coeficientes = f'Correlação (Tamanho x Preço) = {tp_r:.5f}   B0 = {tp_b0:.5f}   B1 = {tp_b1:.5f}'
    qp_coeficientes = f'Correlação (N° Quartos x Preço) = {qp_r:.5f}   B0 = {qp_b0:.5f}   B1 = {qp_b1:.5f}'
    ax.text2D(0.01, 0.9, tp_coeficientes + '\n' + qp_coeficientes, transform=ax.transAxes)
    ax.set_xlabel('tamanho da casa')
    ax.set_ylabel('número de quartos')
    ax.set_zlabel('preço')
    plt.show()

    


x, y = ler_arquivo()
analisar_dados(x, y)