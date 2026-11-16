from pilha import Pilha

def decimal_para_binario(numero):
    pilha = Pilha()

    while numero > 0:
        resto = numero % 2
        pilha.empilhar(resto)
        numero = numero // 2

    binario = ''

    while not pilha.vazia():
        binario += str(pilha.desempilhar())

    return binario

numero = 10
resultado = decimal_para_binario(numero)

print(resultado)
