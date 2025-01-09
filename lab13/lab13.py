###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 13 - Transporte de Itens
# Nome: Jorge Felipe Lopes Pereira
# RA: 251771
###################################################

def carregamento(dadosobjetos, valor, carregado, capacidade):
    for fator in range(len(dadosobjetos)):
        if dadosobjetos[fator][1] <= capacidade:
            # Cabe no caminhão.
            capacidade-=dadosobjetos[fator][1]
            carregado+=dadosobjetos[fator][1]
            valor+=dadosobjetos[fator][2]
    return valor, carregado

def insertionsort(lista, fator):
    for i in range(1, len(lista)):
        auxiliar = lista[i]
        j = i-1
        while (j>=0 and lista[j][fator]>=auxiliar[fator]):
            lista[j+1] = lista[j]
            j = j-1
        lista[j+1] = auxiliar
    return lista[::-1]

def imprimir(valor_por_peso, valor_por_valor, valor_por_razao, carregado_por_peso, carregado_por_valor, carregado_por_razao):
    print('Valor carregado considerando o peso dos itens: R$', valor_por_peso)
    print('Peso carregado considerando o peso dos itens:', carregado_por_peso, 'Kg\n')
    print('Valor carregado considerando o valor dos itens: R$', valor_por_valor)
    print('Peso carregado considerando o valor dos itens:', carregado_por_valor, 'Kg\n')
    print('Valor carregado considerando a razão de valor por peso: R$', valor_por_razao)
    print('Peso carregado considerando a razão de valor por peso:', carregado_por_razao, 'Kg')

def main():
    # Leitura da capacidade e quantidade de itens
    capacidade = int(input())
    objetos = int(input())
    dadosobjetos = []

    # Leitura dos itens, pesos e valores
    for i in range(objetos):
        item = input().split()
        item[1] = int(item[1])
        item[2] = int(item[2])
        item.append(item[2]/item[1])
        dadosobjetos.append(item)

    valor_por_peso, valor_por_valor, valor_por_razao = 0, 0, 0
    carregado_por_peso, carregado_por_valor, carregado_por_razao = 0, 0, 0

    # Ordenação por peso
    valor_por_peso, carregado_por_peso = carregamento(insertionsort(dadosobjetos.copy(), 1), valor_por_peso, carregado_por_peso, capacidade)

    # Ordenação por valor
    valor_por_valor, carregado_por_valor = carregamento(insertionsort(dadosobjetos.copy(), 2), valor_por_valor, carregado_por_valor, capacidade)

    # Ordenação pela razão de valor por peso
    valor_por_razao, carregado_por_razao = carregamento(insertionsort(dadosobjetos.copy(), 3), valor_por_razao, carregado_por_razao, capacidade)

    # Impressão da resposta
    imprimir(valor_por_peso, valor_por_valor, valor_por_razao, carregado_por_peso, carregado_por_valor, carregado_por_razao)
    
if __name__ == "__main__":
  main()