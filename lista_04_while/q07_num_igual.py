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
    n2 = None
    while n1 != n2:
        try:
            print("Insira um número igual ao primeiro número lido:", end=" ")
            n2 = obter_numero_int()
        except:
            print("Valor inválido, tente novamente.")
            continue
    print("Fim do programa.")


main()