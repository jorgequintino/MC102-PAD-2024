###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 12 - Pac-Man I
# Nome: Jorge Felipe Lopes Pereira
# RA:
###################################################

def vazio(mapa):
    for linha in range(len(mapa)):
        for coluna in range(len(mapa[linha])):
            if mapa[linha][coluna] == "." or mapa[linha][coluna] == "*":
                return False
    return True

def mover(mapa, linha, coluna, movimento):
    mapa[linha+movimento[0]][coluna+movimento[1]] = "C"
    if coluna ==len(mapa[0]):
        mapa[linha][0] = " "
    elif linha == len(mapa):
        mapa[0][coluna] = " "
    elif coluna == -1:
        mapa[linha][len(mapa[0])-1] = " "
    elif linha == -1:
        mapa[len(mapa)-1][coluna] = " "
    else:
        mapa[linha][coluna] = " "

    return mapa

def movimentacao(mapa, linha, coluna, zona, movimento, pastilha):
    if mapa[linha+movimento[0]][coluna+movimento[1]] != "#":
        if mapa[linha+movimento[0]][coluna+movimento[1]] == "X":
            if pastilha:
                mapa = mover(mapa, linha, coluna, movimento)
                return mapa, pastilha, True, 0, False
            else:
                #gameover
                return mapa, pastilha, False, 0, True
        elif mapa[linha+movimento[0]][coluna+movimento[1]] == ".":
            mapa = mover(mapa, linha, coluna, movimento)
            return mapa, pastilha, True, 1, False
        elif  mapa[linha+movimento[0]][coluna+movimento[1]] == "*":
            mapa = mover(mapa, linha, coluna, movimento)
            pastilha = True
            return mapa, pastilha, True, 1, False
        else:
            mapa = mover(mapa, linha, coluna, movimento)
            return mapa, pastilha, True, 0, False
    return  mapa, pastilha, False, 0, False

def gameon(mapa, linha, coluna, zona, pastilha):
    movimentos = [(0,1),(-1,0), (0,-1),(1,0)]
    while True:
        
        if linha+movimentos[zona][0]<0:
            mapa, pastilha, moveu, quantidade, morreu = movimentacao(mapa, len(mapa), coluna, zona, movimentos[zona], pastilha)
        elif linha+movimentos[zona][0]>=len(mapa):
            mapa, pastilha, moveu, quantidade, morreu = movimentacao(mapa, -1, coluna, zona, movimentos[zona], pastilha)
        elif coluna+movimentos[zona][1]<0:
            mapa, pastilha, moveu, quantidade, morreu = movimentacao(mapa, linha, len(mapa[0]), zona, movimentos[zona], pastilha)
        elif coluna+movimentos[zona][1]>=len(mapa[0]):
            mapa, pastilha, moveu, quantidade, morreu = movimentacao(mapa, linha, -1, zona, movimentos[zona], pastilha)
        else:
            mapa, pastilha, moveu, quantidade, morreu = movimentacao(mapa, linha, coluna, zona, movimentos[zona], pastilha)
        
        if morreu:
            break
        if moveu:
            return mapa, (zona-1)%4, pastilha, True, quantidade
        zona = (zona+1)%4

    return mapa, zona, pastilha, False, 0

def direcao(mapa):
    for linha in range(len(mapa)):
        for coluna in range(len(mapa[linha])):
            if mapa[linha][coluna] == "C":
                return linha, coluna
    return None, None

def main():
    # Leitura da entrada
    N = int(input())
    T = int(input())

    mapa = []
    for _ in range(N):
        mapa.append(list(input()))

    # Simulação do jogo
    jogo = True
    zona = 3
    pastilha = False
    tempopastilha = T+1
    comidas = 0

    while jogo:
        linha, coluna = direcao(mapa)
        if pastilha == True:
            tempopastilha+= -1
            if tempopastilha == 0:
                pastilha = False
                tempopastilha = T+1

        if linha != None and coluna != None:
            mapa, zona, pastilha, jogo, quantidade = gameon(mapa, linha, coluna, zona, pastilha)
            comidas += quantidade

        if vazio(mapa):
            jogo = False

    # Impressão da saída
    print(comidas)

if __name__ == "__main__":
  main()
