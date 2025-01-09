###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 2 - Em Busca de um Chuveiro
# Nome: Jorge Felipe Lopes Pereira
# RA:
###################################################

# Leitura da entrada

resistor = int(input())
voltage = int(input())
time = int(input())
cost = float(input())
limit = int(input())

# Cálculo do consumo e impressão da saída

power = (voltage**2)//resistor
kwh = (power*time)//1000
used = kwh*cost

print(used<=limit)
