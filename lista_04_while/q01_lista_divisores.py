import os
from utils.number_utils import obter_numero_int


def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def obter_divisores(n):
    divisores = []
    for i in range(1, n):
        if n % i == 0:
            divisores.append(i)
    for i in range(len(divisores)):
        if len(divisores) == 1:
            print(f" 1 e {n}. {n} é um número primo.")
        elif len(divisores) == 2:
            print(f" {divisores[0]} e {divisores[1]}.")
        elif i == (len(divisores) - 2):
            print(" ", end=f"{divisores[i]}")
        elif i == (len(divisores) - 1):
            print(f" e {divisores[i]}.")
        else:
            print(" ", end=f"{divisores[i]},")


def main():
    aux = 1
    limpar_tela()
    while aux != 0:
            print("Insira um número inteiro: ", end="")
            n = obter_numero_int()
            print(f"Os divisores de {n} são:", end="")
            obter_divisores(n)
            try:
                aux = int(input("Pressione enter para prosseguir com o programa, ou digite 0 para finalizar >> "))
            except ValueError:
                pass


main()