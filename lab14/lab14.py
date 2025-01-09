###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 14 - Montanha Russa II
# Nome: Jorge Felipe Lopes Pereira
# RA: 251771
###################################################

"""
Função para simular a compra de ações, que deve ser implementada de forma recursiva.

Argumentos:
    - precos: a matriz contendo o preço diário das ações de cada uma das empresas
    - dia (int): o dia corrente
    - dinheiro (int): o capital inicial a sua disposição no dia especifico
    - acoes_compradas (int): a quantidade de ações em sua posse no dia atual
    - empresa_comprada (int): o índice representando a empresa cujas ações compradas estão em sua posse

IMPORTANTE: A submissão de um programa sem uma FUNÇÃO RECURSIVA válida
            implementada será considerada TENTATIVA DE FRAUDE.
"""
def simula_compra_acoes(N, negocio, precos, dia, dinheiro, acoes_compradas, empresa_comprada):
    # Separar as possíveis ações em níveis de prioridade no dia:

    # Último dia, não é possivel comprar/vender. Deve retornar o que tem.
    if dia == N:
        return [dinheiro,] + negocio
    
    else:
        #Do contrário, escolher entre comprar, vender e não fazer negócio. O dinheiro parcial do começo é zero.
        parcial = [0,]

        # Se açoes já foram compras, tentar vendê-las.
        if acoes_compradas > 0:
            processamento = simula_compra_acoes(N, negocio + ["Vendidas", dia, empresa_comprada], precos, dia + 1, dinheiro + precos[dia][empresa_comprada] * acoes_compradas, 0, empresa_comprada)
            if processamento[0] > parcial[0]:
                parcial = processamento
        
        # Após negociar as ações possíveis, a prioridade deve ser escolher o melhor resultado parcial.
        processamento = simula_compra_acoes(N, negocio, precos, dia + 1, dinheiro, acoes_compradas, empresa_comprada)
        if processamento[0] > parcial[0]:
            # Maior lucro (dinheiro)
            parcial = processamento
            
        # Se é até o antepenultimo dia (tem-se dois dias restante, no mínimo) e não há ações, deve-se comprar novas ações.
        if dia < N - 1 and acoes_compradas == 0:    
            for i in range(len(precos[0])):
                # Preço em baixa.
                if precos[dia][i] < precos[dia + 1][i]:
                    novodinheiro = dinheiro % precos[dia][i]
                    novasacoes = dinheiro // precos[dia][i]
                    processamento = simula_compra_acoes(N, negocio + ["Compradas", dia, i], precos, dia + 1, novodinheiro, novasacoes, i)
                    if processamento[0] > parcial[0]:
                        parcial = processamento

    return parcial

def imprimirdados(precos, dadosfinais):
    for i in range(1, len(dadosfinais), 3):
        if dadosfinais[i] == "Compradas":
            print(f"Acoes da empresa {dadosfinais[i + 2] + 1} compradas no dia {dadosfinais[i + 1] + 1} por R$ {precos[dadosfinais[i + 1]][dadosfinais[i + 2]]}")
        else:
            print(f"Acoes da empresa {dadosfinais[i + 2] + 1} vendidas no dia {dadosfinais[i + 1] + 1} por R$ {precos[dadosfinais[i + 1]][dadosfinais[i + 2]]}")
    print(f"Dinheiro final: R$ {dadosfinais[0]}")

def main():
    # Leitura de dados
    N, M = map(int, input().split())
    precos = []

    for i in range(N):
        precos.append(list(map(int, input().split())))

    dinheiro = int(input())

    # Cálculo dos dias de compra e venda
    dadosfinais = simula_compra_acoes(N, list(), precos, 0, dinheiro, 0, 0)

    # dadosfinais = [dinheiro, negocio, dia, empresa, negocio, dia, empresa, ...]
    # Impressão da saída
    imprimirdados(precos, dadosfinais)

if __name__ == "__main__":
  main()