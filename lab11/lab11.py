###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 11 - Níveis de Radiação
# Nome: Jorge Felipe Lopes Pereira
# RA: 251771
###################################################

def criarterreno(linhas, colunas, coordlinha, coordcoluna, radiacao):
  terreno = list()
  for i in range(linhas):
    terreno.append([])
    for j in range(colunas):
      if i==coordlinha and j==coordcoluna:
        terreno[i].append(radiacao)
      else:
        terreno[i].append(0)
  return terreno

def adicionarterrenos(terreno1, terreno2):
  for i in range(len(terreno1)):
    for j in range(len(terreno1[i])):
      terreno1[i][j] += terreno2[i][j]
  return terreno1

def radioativos(terreno):
  pontos = []
  for linha in range(len(terreno)):
    for coluna in range(len(terreno[linha])):
      if terreno[linha][coluna] > 0:
        pontos.append((linha, coluna))
  return pontos

def ehdiagonal(matriz, radiatividade, coordlinha, coordcoluna, linha, coluna):
  horizontal = coordlinha - linha
  if horizontal<0:
    horizontal = linha-coordlinha
  vertical = coordcoluna-coluna
  if vertical<0:
    vertical = coluna-coordcoluna
  if horizontal==vertical and coordlinha!=linha and coordcoluna!=coluna:
    return True 
  return False 

def radiardiagonal(terrenoradioativo, coordlinha, coordcoluna, radioatividade):
  for linha in range(len(terrenoradioativo)):
    for coluna in range(len(terrenoradioativo[linha])):
      if ehdiagonal(terrenoradioativo, radioatividade, coordlinha, coordcoluna, linha, coluna):
        if (coordcoluna-coluna)>0:
          terrenoradioativo[linha][coluna] = radiaroponto(coordcoluna, coluna, radioatividade)
        else:
          terrenoradioativo[linha][coluna] = radiaroponto(coluna, coordcoluna, radioatividade)
  return terrenoradioativo

def temdiagonal(terreno, linha, coordlinha, coordcoluna):
  contador = 0
  primeira = 0
  segunda = 0
  for coluna in range(len(terreno[0])):
    if terreno[linha][coluna]>0:
      if linha == coordlinha and coluna==coordcoluna:
        return -1, coordcoluna, coordcoluna, terreno[coordlinha][coordcoluna]
      else:
        contador+=1
        if contador==1:
          primeira = coluna
        elif contador==2:
          segunda=coluna
  return contador, primeira, segunda, terreno[linha][primeira]

def radiaroponto(primeira, segunda, valor):
  diminuiu = (primeira-segunda)
  if valor - diminuiu<0:
    variacao = 0
  else:
    variacao = valor - diminuiu
  return variacao

def radiar(terrenoponto, coordlinha, coordcoluna):
  for linha in range(len(terrenoponto)):
    diagonais, primeira, segunda, valor= temdiagonal(terrenoponto, linha, coordlinha, coordcoluna)
    for coluna in range(len(terrenoponto[linha])):
      if diagonais==2:
        if coluna < primeira:
          terrenoponto[linha][coluna] = radiaroponto(primeira, coluna, valor)
        elif coluna>primeira and coluna<segunda:
          terrenoponto[linha][coluna] = valor
        elif coluna>segunda:
          terrenoponto[linha][coluna] = radiaroponto(coluna, segunda, valor)
      elif diagonais==1:
        if primeira<coordcoluna:
          if coluna<primeira:
            terrenoponto[linha][coluna] = radiaroponto(primeira, coluna, valor)
          elif coluna>primeira:
            terrenoponto[linha][coluna] = valor
        elif primeira>coordcoluna:
          if coluna<primeira:
            terrenoponto[linha][coluna] = valor
          elif coluna>primeira:
            terrenoponto[linha][coluna] = radiaroponto(coluna, primeira, valor)
      elif diagonais==-1:
        if coluna<primeira:
          terrenoponto[linha][coluna] = radiaroponto(primeira, coluna, valor)
        elif coluna>primeira:
          terrenoponto[linha][coluna] = radiaroponto(coluna, primeira, valor)
      else:
        if terrenoponto[linha-1][coluna]>0 and linha-1>0:
          if terrenoponto[linha-1][coluna]-1>0:
            terrenoponto[linha][coluna] = (terrenoponto[linha-1][coluna]-1)
  return terrenoponto

def processo(linhas, colunas, terreno, pontosradioativos):
  terrenofinal = criarterreno(linhas, colunas, 0, 0, 0)
  for pontos in range(len(pontosradioativos)):
    coordlinha = pontosradioativos[pontos][0]
    coordcoluna = pontosradioativos[pontos][1]
    terrenoponto = criarterreno(linhas, colunas, coordlinha, coordcoluna, terreno[coordlinha][coordcoluna])
    terrenoponto = radiardiagonal(terrenoponto, coordlinha, coordcoluna, terreno[coordlinha][coordcoluna])
    terrenoponto = radiar(terrenoponto, coordlinha, coordcoluna)
    terrenofinal = adicionarterrenos(terrenofinal, terrenoponto)
  return terrenofinal

def imprimirterreno(terreno):
  for linha in range(len(terreno)):
    for coluna in range(len(terreno[linha])):
      if terreno[linha][coluna]>9:
        terreno[linha][coluna] = "+"
      else:
        terreno[linha][coluna] = str(terreno[linha][coluna])
  for linha in terreno:
    print(''.join(linha))

def main():
  # Leitura de dados
  linhas = int(input())
  terreno = []
  for i in range(linhas):
    colunas = list(input())
    for objetos in range(len(colunas)):
      colunas[objetos] = int(colunas[objetos])
    terreno += [colunas]

  # Processamento
  terreno = processo(linhas, len(terreno[0]), terreno, radioativos(terreno))

  # Impressão da saída
  imprimirterreno(terreno)

if __name__ == "__main__":
  main()
