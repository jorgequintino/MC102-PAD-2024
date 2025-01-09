###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 10 - Quadrados à Obra
# Nome: Jorge Felipe Lopes Pereira
# RA:
###################################################

def ehvazio(terreno, tamanho, i, j, linha, coluna):
    # Se cabe um quadrado no perimetro.
    for largura in range(tamanho+1):
        for comprimento in range(tamanho+1):
            if terreno[i+largura][j+comprimento] != " " or i+largura==linha or j+comprimento==coluna:
                return False
    return True

def empecilho(terreno, i, j):
    return terreno[i][j] != " "

def areacasa(terreno, i, j, linha, coluna):
    # Para o primeiro caso [Quadrado 1u.a.]
    tamanho = 1

    # Para quadrados de maiores áreas.
    while ehvazio(terreno, tamanho, i, j, linha, coluna):
        tamanho+=1

    return tamanho

def demarcarcasa(terreno, tamanho, largurainicio, largurafim, comprimentoinicio, comprimentofim):
    for largura in range(tamanho):
        terreno[comprimentoinicio][largurainicio + largura] = "*"
        terreno[comprimentofim][largurainicio + largura] = "*"
    for comprimento in range(tamanho):
        terreno[comprimentoinicio+comprimento][largurainicio] = "*"
        terreno[comprimentoinicio + comprimento][largurafim] = "*"
    return terreno


def imprimirterreno(terreno, M, N):
    for linha in range(M):
        for coluna in range(N):
            if coluna == N-1:
                print(terreno[linha][coluna])
            else:
                print(terreno[linha][coluna], end="")

def main():
    # Leitura do número de setores verticais e horizontais.
    M, N = map(int, input().split())

    terreno = []

    # Leitura do mapa do terreno do cliente.
    for i in range(M):
        linha_i = list(input())
        terreno += [linha_i]

    # Percorre o terreno.
    largurainicio = 0
    largurafim = 0
    comprimentoinicio = 0
    comprimentofim = 0
    maiorarea = 0

    # Onde possui a maior area.
    for i in range(M-1):
        for j in range(N-1):
            if i > 0 and j >0:
                # Dentro apenas do perimetro.
                if not empecilho(terreno, i, j):
                    area = areacasa(terreno, i, j, M-1, N-1)
                    if area > maiorarea:
                        maiorarea = area
                        largurainicio = j
                        largurafim = j+maiorarea-1
                        comprimentoinicio = i
                        comprimentofim = i+maiorarea-1
    
    # Demarcar a nova casa.
    terreno = demarcarcasa(terreno, maiorarea, largurainicio, largurafim, comprimentoinicio, comprimentofim)

    # Printar novo terreno
    imprimirterreno(terreno, M, N)
                            

if __name__ == "__main__":
  main()
