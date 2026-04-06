import os
from utils.number_utils import obter_numero_int

def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def calcular_peso():
    print("Insira a quantidade de containers:", end=" ")
    containers = obter_numero_int()
    print("""
    Insira o peso dos containers
    """)
    peso = 0 
    for i in range(containers):
        print(f"Insira o peso do container {i + 1}:", end=" ")
        peso_container = obter_numero_int()
        peso += peso_container
    print("""
    Insira os dados dos passageiros
    """)
    while True:
        print("Insira o número do bilhete do passageiro:", end=" ")
        bilhete = obter_numero_int()
        if bilhete == 0:
            break
        print("Insira a quantidade de bagagens do passageiro:", end=" ")
        peso_bagagem = 0
        bagagens = obter_numero_int()
        for i in range(bagagens):
            peso_bagagem += 10
        peso += 70 + peso_bagagem
    return peso


def calcular_combustivel(peso):
    capacidade_restante = 500000 - peso
    combustivel = capacidade_restante / 1.5
    return combustivel


def main():
    limpar_tela()
    peso = calcular_peso()
    combustivel = calcular_combustivel(peso)
    if combustivel > 10000:
        print("O avião vai decolar!")
    else:
        print("O avião não vai decolar... :(")


main()