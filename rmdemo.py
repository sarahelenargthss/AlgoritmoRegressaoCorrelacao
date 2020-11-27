from demo import analisar_dados
import matplotlib.pyplot as plt
from demo import correlacao
from demo import regressao
import csv
import numpy as np




def ler_arquivo():
    with open('data.csv', 'r') as ficheiro:
        reader = csv.reader(ficheiro)
        x = [] 
        y = []
        for linha in reader:
            linha[0] = int(linha[0])
            linha[1] = int(linha[1])
            linha[2] = float(linha[2])
            x.append(linha[0:2])
            y.append(linha[2])
    
    return x, y

def analisar_dados(x, y):
    # busca a correlação e regressão para tamanho de casa e preço
    r = correlacao(x[:,0], y)
    b0, b1 = regressao(x[:,0], y)

    # busca a correlação e regressão para número de quartos e preço
    r = correlacao(x[:,1], y)
    b0, b1 = regressao(x[:,1], y)


x, y = ler_arquivo()
analisar_dados(x, y)