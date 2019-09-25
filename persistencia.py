import statistics
from Particula import Particula

def salvar_dados(nome_arquivo,lista_resultado):    
    precisao_casas_decimais = 6
    
    with open(nome_arquivo + ".csv", "w") as arquivo:
        # gb1 gb1 gb1 gb1 gb1 .... n testes
        # gb2
        # .
        # .
        # .
        # m interacoes            
        
        #Cabeçalho
        arquivo.write(" ")
        for i in range(len(lista_resultado)):
            arquivo.write("Teste" + str(i+1) + " ")        
        arquivo.write("Media"+ " ")
        arquivo.write("Melhor" + " ")
        # arquivo.write("Pior" + " ")
        # arquivo.write("DesvioPadrao")
        arquivo.write("xBest" + " ")
        arquivo.write("yBest")
        arquivo.write('\n')

        #Conteudo
        for i in range(len(lista_resultado)):
            data = []
            data_particula = []
            arquivo.write("gBest" + str(i + 1) + " ")
            for lista in lista_resultado:
                particula_global = lista[i].get_valor_fitness()
                particula_global = round(particula_global,precisao_casas_decimais)
                data.append(particula_global)
                data_particula.append(lista[i])
                arquivo.write(str(particula_global).replace('.',',') + " ")

            lista = sorted(data_particula , key=Particula.get_valor_fitness)
            
            #Media
            media = statistics.mean(data)
            arquivo.write(str(media).replace('.',',') + " ")

            #Melhor
            menor = lista[0].get_valor_fitness()
            arquivo.write(str(menor).replace('.',',') + " ")

            #xBest
            xBest = lista[0].x_best
            arquivo.write(str(xBest).replace('.',',') + " ")

            #yBest
            yBest = lista[0].y_best
            arquivo.write(str(yBest).replace('.',','))

            # #Pior
            # maior = lista[-1].get_valor_fitness()
            # arquivo.write(str(maior).replace('.',',') + " ")

            # #Desvio padrão   
            # desvio = statistics.pstdev(data)
            # arquivo.write(str(desvio).replace('.',','))

            arquivo.write('\n')