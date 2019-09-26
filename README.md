# Algoritmo PSO 

Trabalho desenvolvido para a Disciplina de Inteligência Artificial

Alunos: [Maria Luiza](https://github.com/malufreitas) e [Tarcísio Bruni](https://github.com/tarcisiobruni)

## Explicação Teórica

O algoritmo de Otimização por Enxame de Partículas (*Particle Swarm Optimization*) ou PSO , é um algoritmo dentro do ramo da Inteligência Artificial e Computação Evolutiva e foi concebido por James Kennedy e Russel Eberhart. O objetivo deste algoritmo está em otimizar um problema de maneira iterativa, baseado em aspectos semelhantes aos da iteração de cardumes e revoadas.

Ele está entre as meta-heurísticas de algoritmos de otimização baseados em padrões da natureza mais populares e é inspirado no comportamento social e cooperativo exibido por várias espécies de forma a realizar as necessidades no espaço de busca. Por se tratar de uma meta-heurística, realiza pouca ou quase nenhuma premissa sobre algum problema que é proposto e com isso pode procurar soluções em grande espaço de busca. Por sua vez há de se observar que:

- Não garante que uma solução ideal seja achada e,
- Guia-se por experiência pessoal (pBest), experiência global (gBest), e o movimento atual das particulas para decidir o próximo espaço a ser analisado.

O algoritmo PSO está dentro das soluções da computação inspiradas nos fenômenos da natureza, como por exemplo a Computação Evolucionária e Inteligência Coletiva – dentre os estudos dessas áreas também estão Algoritmos Genéticos, Programação Coletiva, Evolução Gramatical e Programação Evolutiva.

O algoritmo resolve um problema criando uma população de partículas, como soluções candidatas. Essas partículas são movidas em torno do espaço de pesquisa e tais movimentos são realizados de acordo com fórmulas matemáticas (equação da velocidade) sobre a posição e velocidade correntes de cada membro do bando.

## Problema Proposto

O problema sugerido pelo professor envolve utilizar algum algoritmo de otimização por enxame de partículas para minimar a função *Eggholder*, que é uma função clássica na condução de testes para otimização de funções. O objetivo final então, é se aproximar o máximo possível do mínimo global desta função, que é exibida abaixo:

<p align="center">
  <img  src="https://github.com/malufreitas/optimizacao-por-enxame-de-particulas/blob/master/images/funcao_eggholder.png?raw=true">
</p>

## Instalação e Execução

A construção do programa utilizou a versão 3 do [Python](https://www.python.org/), então recomendamos o uso dessa mesma versão para execução do arquivo main.py. Segue link da documentação da linguagem para as instalações da versão 3:
- https://docs.python.org/3/using/index.html

Continuando...

- Faça um clone do projeto ou faça o download dos arquivos
- Por meio da linha de comando caminhe até o diretório onde se encontram os arquivos-fonte
- Execute o comando *python main.py*

O comando acima **gera** os arquivos com resultados separados pelos processamentos de número de testes , quantidade de iterações e número da população.

## Implementação

A estrutura da implementação tomou como base não somente o pseudocódigo passado pelo professor, mas também por meio de inferências/deduções com base nos materias pesquisados (referências ao final do documento). Para fins de transparência, segue o modelo de pseudocódigo que foi usado como suporte:

1- Determinação do número de partículas <br>
2- Inicialização dos elementos iniciais dentro do domínio especificado <br>
3- Atribuição de velocidade normalizada a todas as partículas <br>
4- Loop iterativo nas partículas processando-as da seguinte forma: <br>
>- Calculo da Função Fitness para posição corrente e, definição da melhor posição da partícula

5- Identificação da melhor partícula global (gBest) <br>
6- Loop iterativo nas partículas processando-as da seguinte forma: <br>
>- Calculo da nova velocidade, com base na equação. (Para cada dimensão da partícula)
>- Atualização da posição em função do cálculo da velocidade e posição anterior

7- Realizar as operações enquanto não chegar na condição de parada

#### Descrição dos Arquivos:
- *main.py* - Arquivo de chamada principal onde são especificados a quantidade de testes para rodar, a quantidade de iterações do PSO e quantidade de populações.
- *pso.py* - Arquivo com a implementação do algoritmo junto com funções de validação, que são listadas no escopo do problema.
- *Particula.py* - Arquivo com a Classe que representa uma entidade Particula.
> Contém os atributos de:
> - Posição x atual,
> - Posição y atual,
> - Velocidade x atual,
> - Velocidade y atual,
> - Valor do Melhor Fitness para a própria particula,
> - Posição x e y do melhor Fitness

- *persistencia.py* - Arquivo com funçoes para exportação dos resultados.

### Trechos mais importantes da implementação segundo o Pseudocódigo

**Inicialização das Partículas**

<p align="center">
  <img  src="https://github.com/malufreitas/optimizacao-por-enxame-de-particulas/blob/master/images/gera_populacao_inicial.png">
</p>

**Cálculo do Fitness e Checagem de pBest**

<p align="center">
  <img  src="https://github.com/malufreitas/optimizacao-por-enxame-de-particulas/blob/master/images/calculo_checagem_fitness.png">
</p>

**Identificação do gBest**

<p align="center">
  <img  src="https://github.com/malufreitas/optimizacao-por-enxame-de-particulas/blob/master/images/identifica_gbest.png">
</p>

**Atualização das Velocidades x e y**

<p align="center">
  <img  src="https://github.com/malufreitas/optimizacao-por-enxame-de-particulas/blob/master/images/calculo_validacao_velocidade.png">
</p>

**Atualização das Posições x e y**

<p align="center">
  <img  src="https://github.com/malufreitas/optimizacao-por-enxame-de-particulas/blob/master/images/calculo_checagem_posicao.png">
</p>

## Resultados

As tabelas a seguir mostram os resultados gráficos (média e melhor) de gBest em cada iteração, processados em uma pilha de 10 testes para os casos de:

- [20 Iterações e 50 Indivíduos](https://github.com/malufreitas/optimizacao-por-enxame-de-particulas/blob/master/images/Processamento_20Intera%C3%A7%C3%B5es_50Particulas_10Testes.PNG)
- [20 Iterações e 100 Indivíduos](https://github.com/malufreitas/optimizacao-por-enxame-de-particulas/blob/master/images/Processamento_20Intera%C3%A7%C3%B5es_100Particulas_10Testes.PNG)
- [50 Iterações e 50 Indivíduos](https://github.com/malufreitas/optimizacao-por-enxame-de-particulas/blob/master/images/Processamento_50Intera%C3%A7%C3%B5es_50Particulas_10Testes.PNG)
- [50 Iterações e 100 Indivíduos](https://github.com/malufreitas/optimizacao-por-enxame-de-particulas/blob/master/images/Processamento_50Intera%C3%A7%C3%B5es_100Particulas_10Testes.PNG)
- [100 Iterações e 50 Indivíduos](https://github.com/malufreitas/optimizacao-por-enxame-de-particulas/blob/master/images/Processamento_100Intera%C3%A7%C3%B5es_50Particulas_10Testes.PNG)
- [100 Iterações e 100 Indivíduos](https://github.com/malufreitas/optimizacao-por-enxame-de-particulas/blob/master/images/Processamento_100Intera%C3%A7%C3%B5es_100Particulas_10Testes.PNG)

### Referências

- Slides e Aulas em Sala
- [PSO](https://pt.wikipedia.org/wiki/Optimiza%C3%A7%C3%A3o_por_enxame_de_part%C3%ADculas), WikiPédia
- [Algoritmo de Otimização por Enxame de Partículas](https://www.youtube.com/watch?v=xaFbSqhtlTo), Youtube
