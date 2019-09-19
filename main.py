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

'''
Estrutura de dados:

fitness da particula:
[(x0,y0,fp0), ..., (xn,yn,fpn)]

se o valor de fp for melhor que o pB, é só substituir na lista pB

pB da particula:
[(x0,y0,pB0), ..., (xn,yn,pBn)]

velocidade:
[(v0x,v0y), ..., (v0n,v0n)]



'''

import random
import math
import matplotlib.pyplot

# Objeto da Particula
class Particula:

    def __init__(self, x_atual, y_atual, velocidade_x, velocidade_y):
        self.x_atual = x_atual
        self.y_atual = y_atual
        self.velocidade_x = velocidade_x
        self.velocidade_y = velocidade_y
        
        self.valor_fitness = None

        # pB -> melhor posição da particula
        self.x_best = x_atual
        self.y_best = y_atual
    
    
    def calcula_aptidao(self):
        return (-(self.y_atual + 47) * math.sin(abs(((self.x_atual/2) + (self.y_atual + 47)) ** (1/2)))) - (self.x_atual * math.sin(abs((self.x_atual - (self.y_atual - 47)) ** (1/2))))


    def set_x_y_best(self, x_best, y_best):
        self.x_best = x_best
        self.y_best = y_best

    
    def set_valor_fitness(self, valor_fitness):
        self.valor_fitness = valor_fitness

    
    def get_valor_fitness(self):
        return self.valor_fitness

    def get_x_best(self):
        return self.x_best

    def get_x_atual(self):
        return self.x_atual

        
    def set_velocidade_x(self, velocidade):
        self.velocidade_x = velocidade
    
    def set_velocidade_y(self, velocidade):
        self.velocidade_y = velocidade


def verifica_velocidade(velocidade):
    if (velocidade >= -77) and (velocidade <= 77):
        velocidade_correta = velocidade
    elif (velocidade <= -77):
        velocidade_correta = -77
    elif (velocidade >= 77):
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


def algoritmo_PSO():
    # Lista para armazenar os resultados para o gráfico
    lista_g_best = []

    melhor_fitness = -959.6407

    # Estrutura de dados para armazenar as particulas
    lista_populacao = []

    # 1. Determine o número de partículas P da população. (testar com 50 e 100)
    populacao = 10
    # populacao = 50
    # populacao = 100

    # 3. Atribua uma velocidade inicial (v) igual para todas as partículas.
    velocidade_x = random.randint(-77,77)
    velocidade_y = random.randint(-77,77)
    
    # Cria as particulas da população
    for i in range(populacao):    
        # 2. Inicialize aleatoriamente a posição inicial (x) (x,y) de cada partícula p de P.
        x = random.randint(-512,512)
        y = random.randint(-512,512)

        # Instancia a particula
        particula = Particula(x, y, velocidade_x, velocidade_y)
        lista_populacao.append(particula)

        valor_fitness = particula.calcula_aptidao()
        particula.set_valor_fitness(valor_fitness)

    # 4. Para cada partícula p em P faça:
    x = 0

    # 7. Se condição de término não for alcançada, retorne ao passo 4.
    iteracoes = 20 #50 #100
    while x < iteracoes:
        #lista_g_best.append([])
        # Calculo do W 
        w = 0.9 - x * ((0.9-0.4)/iteracoes)

        for particula in lista_populacao:
            # (a) Calcule sua aptidão fp = f (p).
            valor_fitness = particula.calcula_aptidao()

            # (b) Calcule a melhor posição da partícula p até o momento (pΒ)
            if (valor_fitness < particula.get_valor_fitness()):
                particula.set_valor_fitness(valor_fitness)
                particula.set_x_y_best(particula.x_atual, particula.y_atual)

        # 5. Descubra a partícula com a melhor aptidão de toda a população (gΒ).
        lista_ordenada = list(lista_populacao)
        lista_ordenada = sorted(lista_ordenada , key=Particula.get_valor_fitness)
        # for i in lista_ordenada:
        #    print(i.get_valor_fitness())
        # print()
        g_best = lista_ordenada[0]
        #print(g_best.x_best)
        x_aux  = g_best.x_best
        y_aux = g_best.y_best
        lista_g_best.append((x_aux,y_aux))
        
        # 6. Para cada partícula p em P faça:
        for particula in lista_populacao:
            # Sabe Deus que erro é esse
            # (a) Atualize a velocidade da partícula pela fórmula:
            # Limite de [-77, 77]

            # Calcula a velocidade x
            a = w * particula.velocidade_x
            b = 0.72 * random.uniform(0,1)
            c = particula.x_best - particula.x_atual
            d = 0.72 * random.uniform(0,1)
            e = g_best.x_best - particula.x_best

            velocidade_x = a + b * c + d * e

            # Verifica se a velocidade x ultrapassou o limite
            velocidade = verifica_velocidade(velocidade_x)
            particula.set_velocidade_x(velocidade)

            # Calcula a velocidade y            
            a = w * particula.velocidade_y
            b = 0.72 * random.uniform(0,1)
            c = particula.y_best - particula.y_atual
            d = 0.72 * random.uniform(0,1)
            e = g_best.y_best - particula.y_best

            velocidade_y = a + b * c + d * e
            
            # Verifica se a velocidade y ultrapassou o limite
            velocidade = verifica_velocidade(velocidade_y)
            particula.set_velocidade_y(velocidade)

            # (b) Atualize a posição da particular pela fórmula:
            # Limite de [-512, 512]
            # Se ultrapassar o limite, zerar a velocidade
            nova_posicao_x = particula.x_atual + velocidade_x
            nova_posicao_y = particula.x_atual + velocidade_y

            posicao, velocidade = verifica_posicao(nova_posicao_x, velocidade_x)
            particula.set_velocidade_x(velocidade)
            particula.x_atual = posicao

            posicao, velocidade = verifica_posicao(nova_posicao_y, velocidade_y)
            particula.set_velocidade_y(velocidade)
            particula.y_atual = posicao
        
        x += 1
    
    return lista_g_best


def main():
    lista_resultado = []

    # 10 iterações
    for i in range(10):
        lista_iteracao = algoritmo_PSO()
        #print(lista_iteracao)
        #print()

        lista_resultado.append(lista_iteracao)
    
    #print(lista_resultado)
    #print()

    
    arquivo = open("resultado_constante_072.csv", "w")
    
    for iteracoes in range(20):
        arquivo.write('x y ')
    arquivo.write('\n')

    for iteracoes in range(20):
        for lista in lista_resultado:
            #print(str(lista[iteracoes]))
            print(lista[iteracoes][0])
            arquivo.write(str(lista[iteracoes][0]).replace('.',',') + " ")
            arquivo.write(str(lista[iteracoes][1]).replace('.',',') + " ")
        arquivo.write('\n')
    
    #matplotlib.pyplot.plot(x, y)
    #matplotlib.pyplot.show()

    return 0

if __name__ == "__main__":
    main()