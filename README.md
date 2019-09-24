# Algoritmo PSO 

Trabalho desenvolvido para a Disciplina de Inteligência Artificial

Alunos: [Maria Luiza](https://github.com/malufreitas) e [Tarcísio Bruni](https://github.com/tarcisiobruni)

## Explicação Teórica

O algoritmo de Otimização por Enxame de Partículas (*Particle Swarm Optimization*) ou PSO , é um algoritmo dentro do ramo da Inteligência Artificial e Computação Evolutiva e foi concebido por James Kennedy e Russel Eberhart. O objetivo deste algoritmo está em otimizar um problema de maneira interativa, baseado em aspectos semelhantes aos da iteração de cardumes de peixes ou revoadas de pássaros.

Ele está entre as meta-heurísticas de algoritmos de otimização baseados em padrões da natureza mais populares e é inspirado no comportamento social e cooperativo exibido por várias espécies de forma a realizar as necessidades no espaço de busca. Por se tratar de uma meta-heurística, reliza pouca ou quase nenhuma premissa sobre algum problema que é proposto e com isso pode procurar soluções em grande espaço de busca. Por sua vez há de se observar que:

- Não garante que uma solução ideal seja achada e,
- Guia-se por experiência pessoal (pBest), experiência global (gBest), e o movimento atual das particulas  para decidir o próximo espaço a ser analisado.

O algoritmo PSO está dentro das soluções da computação inspiradas nos fenômenos da natureza, como por exemplo a Computação Evolucionária e Inteligência Coletiva – dentre os estudos dessas áreas também estão Algoritmos Genéticos, Programação Coletiva, Evolução Gramatical e Programação Evolutiva.

O algoritmo resolve um problema criando uma população de soluções candidatas, também conhecidas como partículas. Essas partículas são movidas em torno do espaço de pesquisa. Tais movimentos são realizados de acordo com fórmulas matemáticas (equação da velocidade) sobre a posição e velocidade correntes de cada membro (ou partícula) do bando.

## Problema Proposto

O problema sugerido pelo professor envolve utilizar algum algoritmo de otimização por enxame de partículas para minimar a função *Eggholder*, que é uma função clássica na condução de testes para otimização de funções.

## Instalação e Execução

A construção do programa utilizou a versão 3 do [Python](https://www.python.org/), então recomendamos o uso dessa mesma versão para execução do arquivo main.py. Segue link da documentação da linguagem para as instalações da versão 3:
- https://docs.python.org/3/using/index.html

Continuando...

- Faça um clone do projeto ou faça o download dos arquivos
- Por meio da linha de comando caminhe até o diretório onde se encontram os arquivos-fonte
- ...

## Implementação

A estrutura da implementação tomou como base não somente o pseudocódigo passado pelo professor, mas também por meio de inferências e deduções com base em materias pesquisados. Para fins de transparência, segue o modelo de pseudocódigo que foi usado como suporte:

1- Determinação do número de partículas
2- Inicialização dos elementos iniciais dentro do domínio especificado
3- Atribuição de velocidade normalizada a todas as partículas
4- Loop iterativo nas partículas processando-as da seguinte forma:
    - Calculo da Função Fitness para posição corrente e, definição da melhor posição da partícula
5- Identificação da melhor partícula global (gBest)
6- Loop iterativo nas partículas processando-as da seguinte forma:
    - Calculo da nova velocidade, com base na equação. (Para cada dimensão da partícula)
    - Atualização da posição em função do cálculo da velocidade e posição anterior
7- Realizar as operações enquanto não chegar na condição de parada

### Trechos mais importantes da implementação segundo o Pseudocódigo

**Inicialização das Partículas**

**Velocidade Iniciais**

**Cálculo do Fitness e Checagem de pBest**

**Identificação do gBest**

**Atualização das Velocidades x e y**

**Atualização das Posições x e y**

## Resultados

As tabelas a seguir mostra os resultados de gBest em cada iteração, exibidos em uma pilha de 10 testes para os casos de:

- 20 Iterações e 50 Indivíduos
- 20 Iterações e 100 Indivíduos
- 50 Iterações e 50 Indivíduos
- 50 Iterações e 100 Indivíduos
- 100 Iterações e 50 Indivíduos
- 100 Iterações e 100 Indivíduos

### Referências

- Slides e Aulas em Sala
- [PSO](https://pt.wikipedia.org/wiki/Optimiza%C3%A7%C3%A3o_por_enxame_de_part%C3%ADculas), WikiPédia
- [Algoritmo de Otimização por Enxame de Partículas](https://www.youtube.com/watch?v=xaFbSqhtlTo), Youtube
