###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 7 - Montanha Russa
# Nome: Jorge Felipe Lopes Pereira
# RA:
###################################################

# Leitura de dados
dias = int(input())
valores = list()
minimos = list()
maximos = list()
iguais = list()
movimentacao = list()

for i in range(dias):
    valores.append(float(input()))
    if i>1:
        if valores[i-2] < valores[i-1] and valores[i] < valores[i-1]:
            maximos.append((valores[i-1], i-1))
        elif valores[i-2] > valores[i-1] and valores[i] > valores[i-1]:
            minimos.append((valores[i-1], i-1))
        elif valores[i] == valores[i-1]:
            iguais.append((valores[i-1], i-1))
            iguais.append((valores[i], i))

dinheiro = float(input())

# Cálculo dos dias de compra e venda

if len(maximos) == 0 and len(minimos) == 0:
    if len(iguais) > 0:
        # degraus
        movimentacao = iguais
    else:
        # reta decrescente
        for i in range(4):
            movimentacao.append((valores[i], i))

elif len(minimos) > 0 and len(maximos) == 0:
    # achar menor diferença antes do minimo
    menor = valores[0] - valores[minimos[0][1]]
    posicao = 0
    for i in range(minimos[0][1]-1):
        if valores[i] - valores[i+1] < menor:
            menor = valores[i] - valores[i+1]
            posicao = i
    movimentacao.append((valores[posicao], posicao))
    movimentacao.append((valores[posicao+1], posicao+1))
    movimentacao.append(minimos[0])
    movimentacao.append((valores[dias-1], dias-1))

elif len(minimos) == 0 and len(maximos) > 0:
    # achar menor diferença antes do maximo
    menor = valores[maximos[0][1]] - valores[0]
    posicao = 0
    for i in range(maximos[0][1]-1):
        if valores[i+1] - valores[i] < menor:
            menor = valores[i+1] - valores[i]
            posicao = i
    movimentacao.append((valores[0], 0))
    movimentacao.append((valores[posicao], posicao))
    movimentacao.append((valores[posicao+1], posicao+1))
    movimentacao.append(maximos[0])

elif len(minimos) == 1 and len(maximos) == 1:
    if minimos[0][1] > maximos[0][1]:
        # maximo é anterior ao minimo
        movimentacao.append((valores[0], 0))
        movimentacao.append(maximos[0])
        movimentacao.append(minimos[0])
        movimentacao.append((valores[dias-1], dias-1))
    else:
        # minimo é anterior ao maximo
        menor = 0
        posicao = 0
        for i in range(minimos[0][1]-1):
            if valores[i+1] - valores[i] > menor:
                menor = valores[i+1] - valores[i]
                posicao = i
        j = maximos[0][1]
        for j in range(dias-1):
            if valores[j+1] - valores[j] > menor:
                menor = valores[j+1] - valores[j]
                posicao = j
        
        if posicao[0]< minimos[0][1]:
            movimentacao.append(valores[posicao], posicao)
            movimentacao.append(valores[posicao+1], posicao+1)
            movimentacao.append(minimos[0])
            movimentacao.append(maximos[0])
        else:
            movimentacao.append(minimos[0])
            movimentacao.append(maximos[0])
            movimentacao.append(valores[posicao], posicao)
            movimentacao.append(valores[posicao+1], posicao+1)

else:
    # multiplos maximos e minimos
    if valores[1] < valores[0]:
        if valores[dias-2] < valores[dias-1]:
            maximos.append((valores[dias-1], dias-1))
        operacao = 0
        movimentacao = [0,0,0,0]
        for i in range(len(minimos)-1):
            # primeiro minimo
            j = len(maximos)-2
            while j >= i:
                # primeiro maximo
                m = j+1
                while m < len(minimos):
                    # segundo minimo
                    k = len(maximos) - 1
                    while k >= m:
                        # segundo maximo
                        conta = (maximos[j][0] - minimos[i][0]) + (maximos[k][0] - minimos[m][0])
                        if conta > operacao:
                            operacao = conta
                            movimentacao[0] = minimos[i]
                            movimentacao[1] = maximos[j]
                            movimentacao[2] = minimos[m]
                            movimentacao[3] = maximos[k]
                        k = k -1
                    m = m + 1
                j = j- 1
        
    if valores[1] > valores[0]:
        minimos = [(valores[0], 0)] + minimos
        if valores[dias-2] < valores[dias-1]:
            maximos.append((valores[dias-1], dias-1))

        operacao = 0
        movimentacao = [0,0,0,0]
        for i in range(len(minimos)-1):
            # primeiro minimo
            j = len(maximos)-2
            while j >= i:
                # primeiro maximo
                m = j+1
                while m < len(minimos):
                    # segundo minimo
                    k = len(maximos) - 1
                    while k >= m:
                        # segundo maximo
                        conta = (maximos[j][0] - minimos[i][0]) + (maximos[k][0] - minimos[m][0])
                        if conta > operacao:
                            operacao = conta
                            movimentacao[0] = minimos[i]
                            movimentacao[1] = maximos[j]
                            movimentacao[2] = minimos[m]
                            movimentacao[3] = maximos[k]
                        k = k -1
                    m = m + 1
                j = j- 1

# calculo dos valores

#compra01
acoes = dinheiro // movimentacao[0][0]
dinheiro = dinheiro % movimentacao[0][0]

#venda01
dinheiro = dinheiro + (acoes * movimentacao[1][0])

#compra02
acoes = dinheiro // movimentacao[2][0]
dinheiro = dinheiro % movimentacao[2][0]

#venda01
dinheiro = dinheiro + (acoes * movimentacao[3][0])


# Impressão da saída

print("Dia da primeira compra:", movimentacao[0][1]+1)
print("Valor de compra: R$ {:.2f}".format(movimentacao[0][0]).replace(".", ","))
print("Dia da primeira venda:", movimentacao[1][1]+1)
print("Valor de venda: R$ {:.2f}".format(movimentacao[1][0]).replace(".", ","))
print("Dia da segunda compra:", movimentacao[2][1]+1)
print("Valor de compra: R$ {:.2f}".format(movimentacao[2][0]).replace(".", ","))
print("Dia da segunda venda:", movimentacao[3][1]+1)
print("Valor de venda: R$ {:.2f}".format(movimentacao[3][0]).replace(".", ","))
print("Valor final: R$ {:.2f}".format(dinheiro).replace(".", ","))
