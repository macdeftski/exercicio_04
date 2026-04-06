import os
from utils.number_utils import obter_numero_int

def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def obter_n():
    print("Insira um número inteiro:", end=" ")
    n1 = obter_numero_int()
    return n1


def main():
    limpar_tela()
    n1 = obter_n()
    print("Insira dois números consecutivos em que a soma de ambos resulte no primeiro número recebido:")
    n2 = obter_numero_int()
    n3 = obter_numero_int()
    while n1 != n2 + n3:
        n2 = obter_numero_int()
        if n2 + n3 == n1:
            break
        n3 = obter_numero_int()
    print("Fim do programa.")


main()