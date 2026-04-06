import os
from utils.number_utils import obter_2_numeros


def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def calcular_mdc(n1, n2):
    aux = 0
    if n1 > n2:
        while n1 % n2 != 0:
            aux = n2
            n2 = n1 % n2
            n1 = aux
        mdc = n2

    elif n2 > n1:
        while n2 % n1 != 0:
            aux = n1
            n1 = n2 % n1
            n2 = aux
        mdc = n1
    else:
        mdc = n1
    return mdc


def calcular_mmc(n1, n2, mdc):
    mmc = (n1 * n2) // mdc
    return mmc


def main():
    limpar_tela()
    n1, n2 = obter_2_numeros()
    mdc = calcular_mdc(n1, n2)
    mmc = calcular_mmc(n1, n2, mdc)
    print(f"O MMC de {n1} e {n2} é {mmc}.")


main()