import math as m
import numpy as num
import random as r
from random import seed
from copy import deepcopy
import matplotlib.pyplot as plt

MAXITER = 40
NUMPARTICULAS = 50
XMAX = 5.12
VMAX = 0.8
NUMDIMENSOES = 4
RASTRIGIN = 1
EGGHOLDER = 0

seed()

def Rastrigin(particula): # recebe por parametros a matriz de particulas p
    f = 10 * NUMDIMENSOES
    for i in range(NUMDIMENSOES):
        f += (particula[i] * particula[i]) - 10*m.cos(2*m.pi*particula[i])
    
    if(f>5.12):
        f = 5.12
    elif(f<-5.12):
        f = -5.12
        
    return f

def Eggholder(particula): # funcao para 2 dimensoes
    if NUMDIMENSOES > 2: print("\nFuncao somente para duas dimensoes\n")
    f = -(particula[1]+47)*m.sin( num.abs(particula[1]+(particula[0]/2)+47) ** (1/2))
    f += - particula[0]*m.sin(num.abs(particula[0]-(particula[1]+47)) ** (1/2))
    if(f > 512):
        f = 512
    elif(f < -512):
        f = -512
    return f

def Inicializa(posParticulas, velParticulas, posBestParticulas, globalBest):
    for i in range(NUMPARTICULAS):
        aleatorio = r.random()
        x1 = (aleatorio * (2*XMAX)) - XMAX
        x2 = (aleatorio * (2*XMAX)) - XMAX
        posParticulas.append( [x1 , x2] )
        velParticulas.append([0,0])
        #velParticulas.append([r.random(), r.random()])
        posBestParticulas.append( [x1 , x2] )
    globalBest = x1
    return globalBest
    
def Multiplica(escalar, lista):
    for i in range(len(lista)):
        lista[i]=lista[i]*escalar
    return deepcopy(lista)

def Subtrai(lista1, lista2):
    for i in range(len(lista1)-1):
        lista1[i] = lista1[i] - lista2[i]
    return deepcopy(lista1)

def Confinamento(velParticula):
    for i in range(len(velParticula)):
        if velParticula[i] > VMAX:
            velParticula[i] = VMAX
        elif velParticula[i] < -VMAX:
            velParticula[i] = -VMAX

def PSO(posParticulas, velParticulas, posBestParticulas, globalBest):
    Inicializa(posParticulas, velParticulas, posBestParticulas, globalBest)    
    aleatorio = r.random()
    ale1 = r.random()
    ale2 = r.random()
    r1 = aleatorio
    r2 = 1 - r1
    #cognitivo = ale1
    #social = ale2
    #inercia = 1 - cognitivo - social
    inercia = 0.6
    cognitivo = 0.1
    social = 0.3
    
    for k in range(MAXITER): # maximo de 40 iterações do algoritmo
        vt1 = vt2 = []
        for i in range(NUMPARTICULAS):
                        
            #calcular nova velocidade
            vt1 = Multiplica(inercia, velParticulas[i])
            vt2 = Multiplica(cognitivo * r1, Subtrai(posBestParticulas[i], posParticulas[i]))
            vt3 = Multiplica(social * r2, Subtrai(globalBest, posParticulas[i]))
            velParticulas[i][0] = vt1[0] + vt2[0] + vt3[0]
            velParticulas[i][1] = vt1[1] + vt2[1] + vt3[1]
            Confinamento(velParticulas[i])
            posParticulasAnterior = deepcopy(posParticulas)
            posParticulas[i][0] = posParticulas[i][0] + velParticulas[i][0]
            posParticulas[i][1] = posParticulas[i][1] + velParticulas[i][1]
            
            if RASTRIGIN == 1:
                if Rastrigin(posParticulas[i]) < Rastrigin(posParticulasAnterior[i]): # verifica se a posição atual é melhor que a posição ANTERIOR p atualizar o pbest
                    posBestParticulas[i] = deepcopy(posParticulas[i])
                if Rastrigin(posParticulas[i]) < Rastrigin(globalBest): # verifica se a posição atual é melhor que a posição BLOBAL p atualizar o Gbest
                    globalBest = deepcopy(posParticulas[i])
            elif EGGHOLDER == 1:
                if Eggholder(posParticulas[i]) < Eggholder(posParticulasAnterior[i]): # verifica se a posição atual é melhor que a posição ANTERIOR p atualizar o pbest
                    posBestParticulas[i] = deepcopy(posParticulas[i])
                if Eggholder(posParticulas[i]) < Eggholder(globalBest): # verifica se a posição atual é melhor que a posição BLOBAL p atualizar o Gbest
                    globalBest = deepcopy(posParticulas[i])
        # fim do for        
    #fim das 40 iterações das N particulas
    
    return globalBest
#FIM DO PSO

def Inicio():  
    menor = 9999
    somaFitness = 0
    listaResultados = list()
    for i in range(50):
        posParticulas = list()
        velParticulas = list()
        posBestParticulas = list()
        globalBest = [0,0]
        
        Inicializa(posParticulas, velParticulas, posBestParticulas, globalBest)
        melhorResultado = PSO(posParticulas, velParticulas, posBestParticulas, globalBest)
        if RASTRIGIN == 1 :
            result = Rastrigin(melhorResultado)
        else:
            result = Eggholder(melhorResultado)
        somaFitness += result
        listaResultados.append(result)
        
        if result < menor:
            menor = result
        
    plt.title(u"Otimização por Enxame de Partículas\nAplicado À Minimizaçãp da Função Rastrigin e Eggholder\n")
    plt.ylabel(u"Força de Sinal de Saída")
    plt.xlabel(u"Quantidade de Iterações")
    plt.plot(listaResultados)
    plt.show()
    
    print("\n\n# Melhor Solucao Encontrada: ", menor)
    print("\n# Valor Médio de Fitness:      ", somaFitness/50)

Inicio()