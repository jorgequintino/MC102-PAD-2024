###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 15 - Pac-Man II
# Nome: Jorge Felipe Lopes Pereira
# RA: 251771
###################################################

'''
Função para simular um caminho percorrido pelo Pac-Man, essa função deve ser
implementada de forma recursiva. A função recebe a matriz representando o
mapa, a posição (i,j) do pacman, uma variável dir representando a direção
atual, o tempo t de duração do pastilha de poder ativa (se houver), o valor
T e o número de pastilhas recolhidas até o momento. A função deve retornar o
número de pastilhas comidas pelo Pac-Man.

IMPORTANTE: A submissão de um programa sem uma FUNÇÃO RECURSIVA válida
            implementada será considerada TENTATIVA DE FRAUDE.
'''
def simula_caminho(mapa, i, j, dir, t, T, pastilhas, aux, contador):
    pastilhas += comidas(mapa, i, j)
    tanterior = t
    maior_parcial = 0

    direcoes = [(0,1),(-1,0),(0,-1),(1,0)]
    for direcao in direcoes:
        auxcopia = copiar(aux)
        mapacopia = clean(copiar(mapa), i, j)
        if (dir[0]*(-1),dir[1]*(-1)) != direcao:

            mapacopia, moveu, t, ic, jc = gameon(mapacopia, i, j, direcao, T, t)

            if moveu:
                entra = True
                if auxcopia[ic][jc] != 0:
                    if auxcopia[i][j] != 0:
                        if auxcopia[ic][jc]>=auxcopia[i][j]:
                            entra = False
                contador+=1
                auxcopia[i][j] = contador
                    
                if not ehvazio(mapacopia) and entra:
                    quantidadepr = simula_caminho(mapacopia, ic, jc, direcao, t+1, T, pastilhas, auxcopia, contador)
                    t = tanterior
                    if jc>j or ic>i:
                        mapacopia = clean(mapacopia, i, j)
                    else:
                        mapacopia = clean(mapacopia, ic, jc)
                    
                    if quantidadepr > maior_parcial:
                        maior_parcial = quantidadepr
    if maior_parcial > pastilhas:
        pastilhas = maior_parcial
    return pastilhas

def comidas(mapa, linha, coluna):
    if mapa[linha][coluna] == "." or mapa[linha][coluna] == "*":
        return 1
    return 0

def clean(mapa, i, j):
    for linha in range(len(mapa)):
        for coluna in range(len(mapa[linha])):
            if mapa[linha][coluna] == "C":
                if (linha, coluna) != (i, j):
                    mapa[linha][coluna] = " "
    mapa[i][j] = "C"
    return mapa

def movimentacao(mapa, linha, coluna, movimento, T, t):
    if mapa[linha+movimento[0]][coluna+movimento[1]] != "#":
        if mapa[linha+movimento[0]][coluna+movimento[1]] == "X":
            if t>0 and T>t:
                return mapa, True, t, linha+movimento[0], coluna+movimento[1]
            else:
                #gameover
                return mapa, False, t, linha, coluna
        elif mapa[linha+movimento[0]][coluna+movimento[1]] == ".":
            return mapa, True, t, linha+movimento[0], coluna+movimento[1]
        elif  mapa[linha+movimento[0]][coluna+movimento[1]] == "*":
            t=-1
            return mapa, True, t, linha+movimento[0], coluna+movimento[1]
        else:
            return mapa, True, t, linha+movimento[0], coluna+movimento[1]
    return  mapa, False, t, linha, coluna

def gameon(mapa, linha, coluna, movimento, T, t):
    if linha+movimento[0]<0:
        mapa, moveu, t, i, j = movimentacao(mapa, len(mapa), coluna, movimento, T, t)
    elif linha+movimento[0]>=len(mapa):
        mapa, moveu, t, i, j = movimentacao(mapa, -1, coluna, movimento, T, t)
    elif coluna+movimento[1]<0:
        mapa, moveu, t, i, j = movimentacao(mapa, linha, len(mapa[0]), movimento, T, t)
    elif coluna+movimento[1]>=len(mapa[0]):
        mapa, moveu, t, i, j = movimentacao(mapa, linha, -1, movimento, T, t)
    else:
        mapa, moveu, t, i, j = movimentacao(mapa, linha, coluna, movimento, T, t)
    return mapa, moveu, t, i, j

def posicao(mapa):
    for linha in range(len(mapa)):
        for coluna in range(len(mapa[linha])):
            if mapa[linha][coluna] == "C":
                return linha, coluna
    return None, None

def ehvazio(mapa):
    for linha in range(len(mapa)):
        for coluna in range(len(mapa[linha])):
            if mapa[linha][coluna] == "." or mapa[linha][coluna] == "*":
                return False
    return True

def setaux(mapa):
    aux = []
    for linha in range(len(mapa)):
        lista = []
        for coluna in range(len(mapa[linha])):
            if mapa[linha][coluna] != "#":
                lista.append(int(0))
            else:
                lista.append("#")
        aux.append(lista)
    return aux

def copiar(mapa):
    aux = []
    for linha in range(len(mapa)):
        lista = []
        for coluna in range(len(mapa[linha])):
            lista.append(mapa[linha][coluna])
        aux.append(lista)
    return aux

def imprimir(pastilhas):
    print(pastilhas)

def main():
    # Leitura da entrada
    N = int(input())
    T = int(input())
    pastilhas = 0

    mapa = []
    for _ in range(N):
        mapa.append(list(input()))

    i, j = posicao(mapa)
    pastilhas = simula_caminho(mapa, i, j, (0,0), 1, T, 0, setaux(mapa), 0)

    # Impressão da saída
    imprimir(pastilhas)

if __name__ == "__main__":
  main()