###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 5 - Dados da Sorte
# Nome: Jorge Felipe Lopes Pereira
# RA:
###################################################

# Leitura da entrada de dados
dado_1 = int(input())
limite_inferior = int(input())
limite_superior = int(input())

# Processamento dos casos de ativação do bônus
solucoes = 0

for dado_2 in range(1,7):
    for dado_3 in range(1,7):
        for dado_4 in range(1,7):
            valor = dado_1 + dado_2 + dado_3 + dado_4
            #verificar valores diferentes
            if dado_1 != dado_2 and dado_1 != dado_3 and dado_1 != dado_4:
                if dado_2 != dado_3 and dado_2 != dado_4:
                    if dado_3 != dado_4:
                        if valor >= limite_inferior and valor <= limite_superior:
                            solucoes += 1


# Saída de dados
print(solucoes, "de 216 combinações podem ativar o bônus")
