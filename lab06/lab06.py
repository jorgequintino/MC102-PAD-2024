###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 06 - Espectativa de Vendas Mensais
# Nome: Jorge Felipe Lopes Pereira 
# RA:
###################################################

# Leitura da quantidade de meses e os valores de vendas mensais
N = int(input())

valores = list()

for i in range(N):
    # Leitura do valor das vendas do mês i.
    v_i = float(input())
    valores.append(v_i)
    #print(valores[i])
    if i>=2:
        #calcular m (usar i-1, até o mês anterior)
        primeiro = 0
        soma_x_i = 0
        soma_v_i = 0
        soma_x_i2 = 0

        for j in range(i):
            primeiro += (j+1)*valores[j]            
            soma_x_i += j+1
            soma_v_i += valores[j]
            soma_x_i2 += (j+1)**2
          
        numerador = ((i*primeiro) - (soma_x_i*soma_v_i))
        denominador = ((i*soma_x_i2) - (soma_x_i)**2)
        m = numerador/denominador

        #calcular b (usar i-1, até o mês anterior)
        b = (soma_v_i - m*soma_x_i)/i

        #calcular valor projetado do mês
        valorprojetado = round((m * (i+1)) + b, 1)

        if valorprojetado < valores[i]:
            conclusao = "SUPERIOR"
        elif valorprojetado == valores[i]:
            conclusao = "ESPERADO"
        else:
            conclusao = "INFERIOR"

        #printar a relação

        print(round(valores[i], 1), valorprojetado, conclusao)
