'''
Algoritmo: Pseudocódigo do PSO.

1. Determine o número de partículas P da população.
2. Inicialize aleatoriamente a posição inicial (x) de cada partícula p de P.
3. Atribua uma velocidade inicial (v) igual para todas as partículas.
4. Para cada partícula p em P faça:
    (a) Calcule sua aptidão fp = f(p).
    (b) Calcule a melhor posição da partícula p até o momento (pΒ).
5. Descubra a partícula com a melhor aptidão de toda a população (gΒ).
6. Para cada partícula p em P faça:
    (a) Atualize a velocidade da partícula pela fórmula:
        vi(t+1) = (W ∗ vi(t)) + (ϕ1 ∗ rand1 ∗ (pB − xi(t))) + (ϕ2 ∗ rand2 * (gB − xi(t))
    (b) Atualize a posição da particular pela fórmula:
        xi(t+1) = xi(t) + vi(t+1)
7. Se condição de término não for alcançada, retorne ao passo 4.

Legenda:
dominio -> x[512, -512] e y[512, -512]

x -> vetor de posição (x,y) da particula
x -> posição x da particula
y -> posição y da particula
p -> particulas da população
fp -> fitness (calculo: f(x,y) = .... calculo no pdf = -959.6407 )
v -> velocidade (limitado em 15% do dominio = ~[-77, 77])
W -> constante 
t -> posição
ϕ1 -> constante (2.5)
ϕ2 -> constante (2.5)
rand1 -> range de 0 à 1
rand2 -> range de 0 à 1
pB -> melhor posição/aptidão local  (cada particula tem um) (valor mais próximo de -959.6407)
gB -> melhor posição/aptidão global (melhor da população toda) (valor mais próximo de -959.6407)

'''

import random
import copy
from Particula import Particula

def verifica_velocidade(velocidade):
    if (velocidade >= -77) and (velocidade <= 77):
        velocidade_correta = velocidade
    elif (velocidade <= -77):
        velocidade_correta = -77
    else:
        velocidade_correta = 77
    
    return velocidade_correta

def verifica_posicao(posicao, velocidade):
    if (posicao >= -512) and (posicao <= 512):
        posicao_correta = posicao
    elif (posicao <= -512):
        posicao_correta = -512
        velocidade = 0
    elif (posicao >= 512):
        posicao_correta = 512
        velocidade = 0
    
    return posicao_correta, velocidade

def gera_populacao_inicial(numero_populacao):
    # Estrutura de dados para armazenar as particulas
    lista_populacao = []

    # 3. Atribua uma velocidade inicial (v) igual para todas as partículas.
    velocidade_x = random.uniform(-77,77)
    velocidade_y = random.uniform(-77,77)

    # Cria as particulas da população
    for _ in range(numero_populacao):    
        # 2. Inicialize aleatoriamente a posição inicial (x) (x,y) de cada partícula p de P.
        x = random.uniform(-512,512)
        y = random.uniform(-512,512)

        # Instancia a particula
        particula = Particula(x, y, velocidade_x, velocidade_y)
        lista_populacao.append(particula)

        valor_fitness = particula.calcula_aptidao()
        particula.set_valor_fitness(valor_fitness)
    
    return lista_populacao

def algoritmo_PSO(numero_populacao, iteracoes,const):
    # Lista para armazenar os resultados para o gráfico
    # Guarda o Gbest de Cada nova iteração
    lista_gbest = []

    # Definicao da populacao inicial
    lista_populacao = gera_populacao_inicial(numero_populacao)

    x = 0
    while x < iteracoes:
        # Calculo da Constante W 
        w = 0.9 - x * ((0.9-0.4)/iteracoes)

        for particula in lista_populacao:
            # Calcule sua aptidão fp = f (p). | Calculo do Fitness
            valor_fitness = particula.calcula_aptidao()
            
            # Definindo a melhor posição da partícula p até o momento (pΒest)
            if (valor_fitness < particula.get_valor_fitness()):
                particula.set_valor_fitness(valor_fitness)
                particula.set_x_y_best(particula.x_atual, particula.y_atual)

        # Descobrindo a partícula com a melhor aptidão de toda a população (gΒest).
        lista_ordenada = list(lista_populacao)
        lista_ordenada = sorted(lista_ordenada , key=Particula.get_valor_fitness)
        
        # Como cada particula guarda sua melhor posicao, o GBest sera \
        # a primeira particula de uma lista ordenada crescentemente de acordo com o melhor fitness 
        # de cada uma
        g_best = lista_ordenada[0]

        lista_gbest.append(copy.copy(g_best))
        
        for particula in lista_populacao:
            # Atualizando a velocidade da partícula pela fórmula: 
            # vi(t+1) = (W ∗ vi(t)) + (ϕ1 ∗ rand1 ∗ (pB − xi(t))) + (ϕ2 ∗ rand2 * (gB − xi(t))
            constante = const

            # Calcula a equacao da velocidade x
            a = w * particula.velocidade_x
            b = constante * random.uniform(0,1)
            c = particula.x_best - particula.x_atual
            d = constante * random.uniform(0,1)
            e = g_best.x_best - particula.x_best

            velocidade_x = a + b * c + d * e

            # Verifica se a velocidade x ultrapassou o limite
            velocidade = verifica_velocidade(velocidade_x)
            particula.set_velocidade_x(velocidade)

            # Atualizando a posição da particula pela fórmula:
            # xi(t+1) = xi(t) + vi(t+1)
            # Limite de [-512, 512]
            # Se ultrapassar o limite, zerar a velocidade    
            nova_posicao_x = particula.x_atual + velocidade_x

            posicao, velocidade = verifica_posicao(nova_posicao_x, velocidade_x)
            particula.set_velocidade_x(velocidade)
            particula.x_atual = posicao

            # Calcula a velocidade y            
            a = w * particula.velocidade_y
            b = constante * random.uniform(0,1)
            c = particula.y_best - particula.y_atual
            d = constante * random.uniform(0,1)
            e = g_best.y_best - particula.y_best

            velocidade_y = a + b * c + d * e
            
            # Verifica se a velocidade y ultrapassou o limite
            velocidade = verifica_velocidade(velocidade_y)
            particula.set_velocidade_y(velocidade)

            # (b) Atualize a posição da particular pela fórmula:
            # Limite de [-512, 512]
            # Se ultrapassar o limite, zerar a velocidade
            nova_posicao_y = particula.x_atual + velocidade_y

            posicao, velocidade = verifica_posicao(nova_posicao_y, velocidade_y)
            particula.set_velocidade_y(velocidade)
            particula.y_atual = posicao
        
        x += 1
    
    return lista_gbest