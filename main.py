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


def algoritmo_PSO():
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
    while x < 20: #50 #100:
        for particula in lista_populacao:
            # (a) Calcule sua aptidão fp = f (p).
            valor_fitness = particula.calcula_aptidao()

            # (b) Calcule a melhor posição da partícula p até o momento (pΒ)
            if (valor_fitness < particula.get_valor_fitness()):
                particula.set_valor_fitness(valor_fitness)
                particula.set_x_y_best(particula.x_atual, particula.y_atual)
        x += 1

    # 5. Descubra a partícula com a melhor aptidão de toda a população (gΒ).

def main():
    return 0

if __name__ == "__main__":
    main()