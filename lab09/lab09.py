###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 9 - Anonimizador de Texto
# nome: Jorge Felipe Lopes Pereira
# RA: 251771
###################################################

def nomes(pessoa, textoanonimizado, anonimizados, chave, i):
    count = 0
    pontofinal = False
    virgula = False
    for k in range(len(pessoa[chave])-(i+1)):
        if pessoa[chave][i+1+k].isalpha() and not pontofinal and not virgula:
            if pessoa[chave][i+1+k][0] > "@" and pessoa[chave][i+1+k][0] < "[":
                count += 1
            else:
                break
        elif not pontofinal and not virgula and pessoa[chave][i+1+k][len(pessoa[chave][i+1+k])-1] == ".":
            pontofinal = True
            temp = pessoa[chave][i+1+k][:len(pessoa[chave][i+1+k])-1]
            if temp.isalpha():
                if temp > "@" and temp < "[":
                    count += 1
                else:
                    break
        elif not virgula and not pontofinal and pessoa[chave][i+1+k][len(pessoa[chave][i+1+k])-1] == ",":
            virgula = True
            temp = pessoa[chave][i+1+k][:len(pessoa[chave][i+1+k])-1]
            if temp.isalpha():
                if temp > "@" and temp < "[":
                    count += 1
                else:
                    break
        else:
            break

    if count>0:
        texto = pessoa[chave][i]
        for l in range(k):
            if pessoa[chave][i+1].isalpha():
                texto += pessoa[chave][i+1]
                del(pessoa[chave][i+1])
            else:
                texto += pessoa[chave][i+1][:len(pessoa[chave][i+1])-1]
                del(pessoa[chave][i+1])

        if texto in textoanonimizado:
            pessoa[chave][i] = textoanonimizado[texto]
            if pontofinal:
                pessoa[chave][i] += "."
                return pessoa, textoanonimizado, anonimizados
            elif virgula:
                pessoa[chave][i] += ","
                return pessoa, textoanonimizado, anonimizados
            else:
                return pessoa, textoanonimizado, anonimizados
        else:
            anonimizados +=1
            textoanonimizado[texto] = "nome:" + str(anonimizados)
            pessoa[chave][i] = textoanonimizado[texto]
            if pontofinal:
                pessoa[chave][i] += "."
                return pessoa, textoanonimizado, anonimizados
            elif virgula:
                pessoa[chave][i] += ","
                return pessoa, textoanonimizado, anonimizados
            else:
                return pessoa, textoanonimizado, anonimizados
    else:
        return pessoa, textoanonimizado, anonimizados

def email(pessoa, textoanonimizado, anonimizados, chave, i):
    texto = pessoa[chave][i]
    if texto in textoanonimizado:
        pessoa[chave][i] = textoanonimizado[texto]
        return pessoa, textoanonimizado, anonimizados
    else:
        anonimizados +=1
        textoanonimizado[texto] = "email:" + str(anonimizados)
        pessoa[chave][i] = textoanonimizado[texto]
        return pessoa, textoanonimizado, anonimizados

def cartao(pessoa, textoanonimizado, anonimizados, chave, i):
    if len(pessoa[chave][i]) == 16:
        texto = pessoa[chave][i]
        if texto in textoanonimizado:
            pessoa[chave][i] = textoanonimizado[texto]
            return pessoa, textoanonimizado, anonimizados

        else:
            anonimizados += 1
            textoanonimizado[texto] = "cartao:" + str(anonimizados)
            pessoa[chave][i] = textoanonimizado[texto]
            return pessoa, textoanonimizado, anonimizados

    elif len(pessoa[chave][i]) == 4:
        count = 0
        for m in range(3):
            if pessoa[chave][i+1+m].isnumeric():
                count += 1
        if count == 3:
            texto = pessoa[chave][i]
            for m in range(3):
                texto += pessoa[chave][i+1]
                del(pessoa[chave][i+1])
            
            if texto in textoanonimizado:
                pessoa[chave][i] = textoanonimizado[texto]
                return pessoa, textoanonimizado, anonimizados

            else:
                anonimizados += 1
                textoanonimizado[texto] = "cartao:" + str(anonimizados)
                pessoa[chave][i] = textoanonimizado[texto]
                return pessoa, textoanonimizado, anonimizados
        else:
            return pessoa, textoanonimizado, anonimizados
    else:
        return pessoa, textoanonimizado, anonimizados
            
def cpf(pessoa, textoanonimizado, anonimizados, chave, i):
    if pessoa[chave][i][3] == ".":
        temp = pessoa[chave][i][:3] + pessoa[chave][i][4:7] + pessoa[chave][i][8:11] + pessoa[chave][i][12:]
        if temp.isnumeric():
            texto = temp
            if texto in textoanonimizado:
                pessoa[chave][i] = textoanonimizado[texto]
                return pessoa, textoanonimizado, anonimizados
            else:
                anonimizados += 1
                textoanonimizado[texto] = "cpf:" + str(anonimizados)
                pessoa[chave][i] = textoanonimizado[texto]
                return pessoa, textoanonimizado, anonimizados
        else:
            return pessoa, textoanonimizado, anonimizados
    elif pessoa[chave][i][9] == "-":
        temp = pessoa[chave][i][:9] + pessoa[chave][i][10:]
        if temp.isnumeric():
            texto = temp
            if texto in textoanonimizado:
                pessoa[chave][i] = textoanonimizado[texto]
                return pessoa, textoanonimizado, anonimizados
            else:
                anonimizados += 1
                textoanonimizado[texto] = "cpf:" + str(anonimizados)
                pessoa[chave][i] = textoanonimizado[texto]
                return pessoa, textoanonimizado, anonimizados
        else:
            return pessoa, textoanonimizado, anonimizados
    else:
        return pessoa, textoanonimizado, anonimizados
    
def data(pessoa, textoanonimizado, anonimizados, chave, i):
    texto = pessoa[chave][i]
    if texto in textoanonimizado:
        pessoa[chave][i] = textoanonimizado[texto]
        return pessoa, textoanonimizado, anonimizados
    else:
        anonimizados += 1
        textoanonimizado[texto] = "data:" + str(anonimizados)
        pessoa[chave][i] = textoanonimizado[texto]
        return pessoa, textoanonimizado, anonimizados

def pontuacao(pessoa, chave, i):
    pontofinal = False
    virgula = False
    if pessoa[chave][i][len(pessoa[chave][i])-1] ==".":
        pessoa[chave][i] = pessoa[chave][i][:len(pessoa[chave][i])-1]
        pontofinal = True
        return pontofinal, virgula
    if pessoa[chave][i][len(pessoa[chave][i])-1] ==",":
        pessoa[chave][i] = pessoa[chave][i][:len(pessoa[chave][i])-1]
        virgula = True
        return pontofinal, virgula
    return pontofinal, virgula

def pontuacaofinal(pessoa, chave, i, pontofinal, virgula):
    if pontofinal:
        pessoa[chave][i] = pessoa[chave][i] + "."
        return pessoa
    elif virgula:
        pessoa[chave][i] = pessoa[chave][i] + ","
        return pessoa
    return pessoa

def anonimizacao(textoanonimizado, pessoa, chave, i, anonimizados):
    pontofinal, virgula = pontuacao(pessoa, chave, i)

    if pessoa[chave][i].isalpha() and not pontofinal and not virgula:
        #nome
        if pessoa[chave][i][0] > "@" and pessoa[chave][i][0] < "[":
            #nome começa com maiúsculo
            pessoa, textoanonimizado, anonimizados = nomes(pessoa, textoanonimizado, anonimizados, chave, i)

    elif pessoa[chave][i].count("@") == 1:
        #email
        pessoa, textoanonimizado, anonimizados = email(pessoa, textoanonimizado, anonimizados, chave, i)

    elif pessoa[chave][i].isnumeric():
        #cartao
        pessoa, textoanonimizado, anonimizados = cartao(pessoa, textoanonimizado, anonimizados, chave, i)

    elif len(pessoa[chave][i]) >= 12:
        #cpf
        pessoa, textoanonimizado, anonimizados = cpf(pessoa, textoanonimizado, anonimizados, chave, i)

    elif len(pessoa[chave][i])>2 and pessoa[chave][i][2] == "/":
        #data
        pessoa, textoanonimizado, anonimizados = data(pessoa, textoanonimizado, anonimizados, chave, i)

    pessoa = pontuacaofinal(pessoa, chave, i, pontofinal, virgula)
    return pessoa, textoanonimizado, anonimizados

def imprimir(cliente, atendente):
    for linha in range(len(cliente)):
        #imprimir linha cliente
        for palavra in range(len(cliente[linha])):
            if palavra < len(cliente[linha])-1:
                print(cliente[linha][palavra], end=" ")
            else:
                print(cliente[linha][palavra])

        for palavra in range(len(atendente[linha])):
            #imprimir linha atendente
            if palavra < len(atendente[linha])-1:
                print(atendente[linha][palavra], end=" ")
            else:
                print(atendente[linha][palavra])

def main():
    # Leitura do texto
    cliente = dict({})
    atendente = dict({})
    textoanonimizado = dict({})
    clientecontador = 0
    atendentecontador = 0

    linha = input().split()
    while linha[0] != "-":

        if linha[0] == "Cliente:":
            cliente[clientecontador] = linha
            clientecontador += 1        
            #salvar no dicionário cliente

        elif linha[0] == "Atendente:":
            atendente[atendentecontador] = linha
            atendentecontador += 1
            # salvar linha no dicionário  atendente
            
        linha = input().split()

    # Anonimização do texto
    anonimizados = 0
    for chave in range(len(cliente)):

        for i in range(len(cliente[chave])):
            # casos cliente para anonimizar
            if i < len(cliente[chave]):
                cliente, textoanonimizado, anonimizados = anonimizacao(textoanonimizado, cliente, chave, i, anonimizados)

            else:
                break  
        
        for i in range(len(atendente[chave])):
            # casos atendente para anonimizar
            if i < len(atendente[chave]):
                atendente, textoanonimizado, anonimizados = anonimizacao(textoanonimizado, atendente, chave, i, anonimizados)

            else:
                break  

    imprimir(cliente, atendente)

if __name__ == "__main__":
    main()
