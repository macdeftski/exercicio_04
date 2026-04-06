import os
from utils.number_utils import obter_numero_int

def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def obter_n():
    print("Insira um número inteiro para descobrir quantos dígitos há no número:", end=" ")
    n = obter_numero_int()
    return n


def digitos(n):
    qnt = len(str(abs((n))))
    return qnt


def main():
    limpar_tela()
    n = obter_n()
    qnt = digitos(n)
    print(f"O número {n} possui {qnt} dígitos.")


main()