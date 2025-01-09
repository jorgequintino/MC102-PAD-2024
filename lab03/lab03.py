###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - Cupons de Desconto
# Nome: Jorge Felipe Lopes Pereira
# RA: 251771
###################################################

# leitura de dados

x1 = int(input())
z1 = int(input())
x2 = int(input())
z2 = int(input())
x3 = int(input())
z3 = int(input())
sale = int(input())

# cálculo dos descontos
cupom1 = x1
cupom2 = (x2/100)*sale
cupom3 = (x3/100)*sale

# Impressão da saída


# checar se cupom 1 e 2 são válidos
# checar o teto de desconto 2
# dentre os cupons validos ver o maior desconto

desconto = 0

if sale >= z1:
    if sale >= z3:
        #desconto 1, 2, 3
        if cupom2 > z2:
            cupom2 = z2
        else:
            if cupom2 == cupom1:
                if cupom2 == cupom3:
                    desconto = cupom2
                    print("Maior desconto: Cupons 1, 2, 3")
                elif cupom2 > cupom3:
                    desconto = cupom2
                    print("Maior desconto: Cupons 1, 2")
                else:
                    desconto = cupom3
                    print("Maior desconto: Cupom 3")

            elif cupom2 > cupom1:
                if cupom2 == cupom3:
                    desconto = cupom2
                    print("Maior desconto: Cupons 2, 3")
                elif cupom2 > cupom3:
                    desconto = cupom2
                    print("Maior desconto: Cupom 2")
                else:
                    desconto = cupom3
                    print("Maior desconto: Cupom 3")
                
            else:
                if cupom1 == cupom3:
                    desconto = cupom2
                    print("Maior desconto: Cupons 1, 3")
                elif cupom1 > cupom3:
                    desconto = cupom2
                    print("Maior desconto: Cupom 1")
                else:
                    desconto = cupom3
                    print("Maior desconto: Cupom 3")

    else:
        #desconto 1, 2
        if cupom2 > z2:
            cupom2 = z2
            if cupom2 > cupom1:
                desconto = cupom2
                print("Maior desconto: Cupom 2")
            if cupom2 == cupom1:
                desconto = cupom2
                print("Maior desconto: Cupons 1, 2")
            else:
                desconto = cupom1
                print("Maior desconto: Cupom 1")
        else:
            if cupom2 > cupom1:
                desconto = cupom2
                print("Maior desconto: Cupom 2")
            elif cupom2 == cupom1:
                desconto = cupom2
                print("Maior desconto: Cupons 1, 2")
            else:
                desconto = cupom1
                print(cupom2)
                print("Maior desconto: Cupom 1")
else:
    if sale >= z3:
        #desconto 3 e 2
        if cupom2 > z2:
            cupom2 = z2
            if cupom3 > cupom2:
                desconto = cupom3
                print("Maior desconto: Cupom 3")
            elif cupom3 == cupom2:
                desconto = cupom2
                print("Maior desconto: Cupons 2, 3")
            else:
                desconto = cupom2
                print("Maior desconto: Cupom 2")
        else:
            if cupom3 > cupom2:
                desconto = cupom3
                print("Maior desconto: Cupom 3")
            elif cupom3 == cupom2:
                desconto = cupom2
                print("Maior desconto: Cupons 2, 3")
            else:
                desconto = cupom2
                print("Maior desconto: Cupom 2")
    else:
        #desconto 2
        if cupom2 >= z2:
            desconto = z2
            print("Maior desconto: Cupom 2")
        else:
            desconto = cupom2
            print("Maior desconto: Cupom 2")

# ...
print("Valor do desconto: R$ {:.2f}".format(desconto).replace(".", ","))
