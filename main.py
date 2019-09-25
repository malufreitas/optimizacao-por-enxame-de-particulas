
import persistencia
import pso

def main():
    # Determinando o numero de testes
    vetor_numero_testes = [10]

    # Determinando o numero de interações
    vetor_numero_interacoes = [20,50,100]

    # Determinando o número de partículas P da população
    vetor_numero_populacao = [50,100]







    # Constants de Phi (ϕ), para uso na equacao da velocidade
    const = 2.09
    
    for numero_interacoes in vetor_numero_interacoes:
        for numero_populacao in vetor_numero_populacao:
            for numero_testes in vetor_numero_testes:
                nome_arquivo = "Processamento_" + str(numero_interacoes) + "Interações_"   
                nome_arquivo+=str(numero_populacao) + "Particulas_"   
                nome_arquivo+=str(numero_testes) + "Testes"   
                lista_resultado = []
                for _ in range(numero_testes):
                    lista_iteracao = pso.algoritmo_PSO(numero_populacao,numero_interacoes,const)
                    lista_resultado.append(lista_iteracao)
                persistencia.salvar_dados(nome_arquivo,lista_resultado)

if __name__ == "__main__":
    main()