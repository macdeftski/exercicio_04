import os
from utils.number_utils import obter_numero_int, obter_numero_float

def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def main():
    limpar_tela()

    pontos_a = 0
    pontos_b = 0

    while True:
        print("Insira o número da prova:", end=" ")
        prova = obter_numero_int()
        print("Insira o número de nadadores:", end=" ")
        nadadores = obter_numero_int()
        if prova == 0 and nadadores == 0:
            break
        for i in range(nadadores):
            nome = input("Insira o nome do nadador: ")
            print("Insira a colocação do nadador:", end=" ")
            colocacao = obter_numero_int()
            print("Insira o tempo do nadador:", end=" ")
            tempo = obter_numero_float()
            clube = input("Insira o clube do nadador: ")

            if colocacao == 1:
                pontos = 9
            elif colocacao == 2:
                pontos = 6
            elif colocacao == 3:
                pontos = 4
            elif colocacao == 4:
                pontos = 3
            else:
                pontos = 0

            if clube == "a" or clube == "A":
                pontos_a += pontos
            else:
                pontos_b += pontos

    print("Clube A:", pontos_a)
    print("Clube B:", pontos_b)

    if pontos_a > pontos_b:
        print("Vencedor: Clube A")
    elif pontos_b > pontos_a:
        print("Vencedor: Clube B")
    else:
        print("Empate")


main()