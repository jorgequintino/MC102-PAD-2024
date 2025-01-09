###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 08 - Calculadora genômica
# Nome: Jorge Felipe Lopes Pereira
# RA:
###################################################


def reverter(genoma, i, j, ciclico):
    if ciclico:
        if j < i:
            temp = (genoma[i:] + genoma[:j+1])
            temp1= temp[::-1]
            p = len(genoma) - i
            genoma = temp1[p:] + genoma[j+1:i] + temp1[:p]
        else:
            i = i & len(genoma)
            j = j & len(genoma)
            genoma = genoma[:i] + genoma[i:j+1:][::-1] + genoma[j+1:]
    else:
        genoma = genoma[:i] + genoma[i:j+1:][::-1] + genoma[j+1:]
    return genoma

def transpor(genoma, i, j, k, ciclico):
    if ciclico:
        i = i & len(genoma)
        j = j & len(genoma)
        k = k & len(genoma)
        genoma = genoma[:i] + genoma[j+1:k+1] + genoma[i:j+1] + genoma[k+1:]
    else:
        genoma = genoma[:i] + genoma[j+1:k+1] + genoma[i:j+1] + genoma[k+1:]
    return genoma

def inserir(genoma, codigo, i, ciclico):
    if ciclico:
        if i>= len(genoma):
            i = i & len(genoma)
            genoma =  genoma[:i] + codigo + genoma[i:]
        else:
            genoma =  genoma[:i] + codigo + genoma[i:]
    else:
        genoma =  genoma[:i] + codigo + genoma[i:]
    return genoma

def remover(genoma, i, j, ciclico):
    if ciclico:
        if i>= len(genoma):
            i = i & (len(genoma)-1)
            genoma = genoma[:i] + genoma[j+1:]
        else:
            genoma = genoma[:i] + genoma[j+1:]
    else:
        genoma = genoma[:i] + genoma[j+1:]
    return genoma

def fissao(genoma, i):
    return genoma[i:] + genoma[:i]

def fusao():
    return True

def mostrar(genoma, ciclico):
    if ciclico:
        print(genoma + " c1")
    else:
        print(genoma + " c0")

def buscar(genoma, codigo, ciclico):
    if ciclico:
        repeticao = genoma.count(codigo)
        tamanho = len(genoma)-len(codigo)
        for i in range(tamanho):
            genoma_alt = genoma[(tamanho+i):] + genoma[:i]
            if genoma_alt.count(codigo)>0:
                repeticao = repeticao + genoma_alt.count(codigo)
                break

        if repeticao == 0:
            genoma = genoma[::-1]
            repeticao = genoma.count(codigo)
            tamanho = len(genoma)-len(codigo)
            for i in range(tamanho):
                genoma_alt = genoma[(tamanho+i):] + genoma[:i]
                if genoma_alt.count(codigo)>0:
                    repeticao = repeticao + genoma_alt.count(codigo)
                    break
        print(repeticao)

    else:
        print(genoma.count(codigo))

def main():
    genoma = input().split()
    comando = input().split()
    ciclico = False

    if len(genoma) == 2:
        if genoma[1] == "c1":
            ciclico = True

    while comando[0] != "sair":
        if comando[0] == "reverter":
            genoma[0] = reverter(genoma[0], int(comando[1]), int(comando[2]), ciclico)

        elif comando[0] == "transpor":
            genoma[0] = transpor(genoma[0], int(comando[1]), int(comando[2]), int(comando[3]), ciclico)

        elif comando[0] == "inserir":
            genoma[0] = inserir(genoma[0], comando[1], int(comando[2]), ciclico)

        elif comando[0] == "remover":
            genoma[0] = remover(genoma[0], int(comando[1]), int(comando[2]), ciclico)

        elif comando[0] == "fissao":
            ciclico = False
            genoma[0] = fissao(genoma[0], int(comando[1]))

        elif comando[0] == "fusao":
            ciclico = fusao()
            
        elif comando[0] == "mostrar":
            mostrar(genoma[0], ciclico)
            
        elif comando[0] == "buscar":
            buscar(genoma[0], comando[1], ciclico)

        comando = input().split()

if __name__ == "__main__":
    main()
