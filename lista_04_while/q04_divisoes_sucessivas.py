import os
from utils.number_utils import obter_numero_int


def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def dividir(n):
    while n >= 1:
        n = n / 2
    return n


def main():
    limpar_tela()
    print("Insira um número inteiro >> ", end="")
    n = obter_numero_int()
    n = dividir(n)
    print(f"O resultado da última divisão é {n}")


main()