import os
from utils.number_utils import obter_numero_int

def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def obter_xn():
    print("Insira o dividendo (X): ", end="")
    x = obter_numero_int()
    print("Insira um divisor N maior que 2: ", end="")
    n = obter_numero_int()
    return x, n


def dividir(x, n):
    divisoes = []
    while n > 2:
        x = x / n
        n -= 1
        divisoes.append(x)
    return x, n, divisoes


def main():
    limpar_tela()
    x, n = obter_xn()
    x, n, divisoes = dividir(x, n)
    print("O(s) resultado(s) da(s) divisões entre X e N com decremento de -1 em N até que chegue a 2 são", end=" ")
    for i in range(len(divisoes)):
        if len(divisoes) == 1:
            print(f"{divisoes[0]}.")
        elif len(divisoes) == 2:
            print(f" {divisoes[0]} e {divisoes[1]}.")
        elif i == (len(divisoes) - 2):
            print(" ", end=f"{divisoes[i]}")
        elif i == (len(divisoes) - 1):
            print(f" e {divisoes[i]}.")
        else:
            print(" ", end=f"{divisoes[i]},")


main()