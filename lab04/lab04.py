###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Pedra, Papel e Tesoura 2.0
# Nome: Jorge Felipe Lopes Pereira
# RA: 251771
###################################################

# Leitura dos valores de força de cada jogador
bonus_jogador_1 = int(input())
bonus_jogador_2 = int(input())
vitorias_jogador_1 = 0
vitorias_jogador_2 = 0
empate = 0

# Processamento dos dados

game = True
while game:

  entrada = input().split()
  if entrada[0] == '0':
    game = False
  else:
    jogada_jogador_1, forca_jogador_1, jogada_jogador_2, forca_jogador_2, fator_rodada = entrada
    forca_jogador_1 = int(forca_jogador_1)
    forca_jogador_2 = int(forca_jogador_2)
    fator_rodada = int(fator_rodada)

    #descontar bônus
    if bonus_jogador_1 < forca_jogador_1 - 1:
        forca_jogador_1 = bonus_jogador_1 + 1
        bonus_jogador_1 = 0
    else:
        bonus_jogador_1 = bonus_jogador_1 - (forca_jogador_1 - 1)

    if bonus_jogador_2 < forca_jogador_2 - 1:
        forca_jogador_2 = bonus_jogador_2 + 1
        bonus_jogador_2 = 0
    else:
        bonus_jogador_2 = bonus_jogador_2 - (forca_jogador_2 - 1)
    
    #jogadas
    if jogada_jogador_1 == jogada_jogador_2:
      #calcular vencedor
        if forca_jogador_1 > forca_jogador_2:
          vitorias_jogador_1 += 1
        elif forca_jogador_1 < forca_jogador_2:
          vitorias_jogador_2 += 1
        else:
          # jogo normal vence
          empate += 1

    else:
      if jogada_jogador_1 == "Tesoura" and jogada_jogador_2 == "Papel":
          #calcular força do mais fraco
          forca_jogador_2 = forca_jogador_2 * fator_rodada
          if forca_jogador_2 > forca_jogador_1:
            vitorias_jogador_2 += 1
          else:
             # jogo normal vence
            vitorias_jogador_1 += 1

      elif jogada_jogador_1 == "Tesoura" and jogada_jogador_2 == "Pedra":
          #calcular força do mais fraco
          forca_jogador_1 = forca_jogador_1 * fator_rodada
          if forca_jogador_1 > forca_jogador_2:
            vitorias_jogador_1 += 1
          else:
             # jogo normal vence
            vitorias_jogador_2 += 1

      elif jogada_jogador_1 == "Papel" and  jogada_jogador_2 == "Pedra":
          #calcular força do mais fraco
          forca_jogador_2 = forca_jogador_2 * fator_rodada
          if forca_jogador_2 > forca_jogador_1:
            vitorias_jogador_2 += 1
          else:
             # jogo normal vence
            vitorias_jogador_1 += 1

      elif jogada_jogador_1 == "Papel" and jogada_jogador_2 == "Tesoura":
          #calcular força do mais fraco
          forca_jogador_1 = forca_jogador_1 * fator_rodada
          if forca_jogador_1 > forca_jogador_2:
            vitorias_jogador_1 += 1
          else:
             # jogo normal vence
            vitorias_jogador_2 += 1

      elif jogada_jogador_1 == "Pedra" and jogada_jogador_2 == "Tesoura":
          #calcular força do mais fraco
          forca_jogador_2 = forca_jogador_2 * fator_rodada
          if forca_jogador_2 > forca_jogador_1:
            vitorias_jogador_2 += 1
          else:
             # jogo normal vence
            vitorias_jogador_1 += 1

      elif jogada_jogador_1 == "Pedra" and jogada_jogador_2 == "Papel":
          #calcular força do mais fraco
          forca_jogador_1 = forca_jogador_1 * fator_rodada
          if forca_jogador_1 > forca_jogador_2:
            vitorias_jogador_1 += 1
          else:
             # jogo normal vence
            vitorias_jogador_2 += 1

# Saída de dados
print('Vitórias do jogador 1:', vitorias_jogador_1)
print('Vitórias do jogador 2:', vitorias_jogador_2)
print('Empates:', empate)
