import matplotlib.pyplot
import statistics

def plotar_dados():
    #matplotlib.pyplot.plot(x, y)
    #matplotlib.pyplot.show()

    # for i in range(numero_testes):
    #         for lista in lista_resultado:
    #         #print(str(lista[iteracoes]))
    #         print(lista[iteracoes][0])
    #         arquivo.write(str(lista[iteracoes][0]).replace('.',',') + " ")
    #         arquivo.write(str(lista[iteracoes][1]).replace('.',',') + " ")
    #     arquivo.write('\n')
    pass

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
        arquivo.write("Pior" + " ")
        arquivo.write("DesvioPadrao")
        arquivo.write('\n')

        #Conteudo
        for i in range(len(lista_resultado)):
            data = []
            arquivo.write("gBest" + str(i + 1) + " ")
            for lista in lista_resultado:
                particula_global = lista[i].get_valor_fitness()
                particula_global = round(particula_global,precisao_casas_decimais)
                data.append(particula_global)
                arquivo.write(str(particula_global).replace('.',',') + " ")
                
            #Media
            media = statistics.mean(data)
            arquivo.write(str(media).replace('.',',') + " ")

            #Melhor
            menor = min(data)
            arquivo.write(str(menor).replace('.',',') + " ")

            #Pior
            maior = max(data)
            arquivo.write(str(maior).replace('.',',') + " ")

            #Desvio padrão   
            desvio = statistics.pstdev(data)
            arquivo.write(str(desvio).replace('.',','))

            arquivo.write('\n')