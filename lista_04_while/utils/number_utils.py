# Utilitários para obter e calcular números

def obter_numero_int():
    n = int(input())
    return n


def obter_2_numeros():
    n1 = int(input("Insira o primeiro número: "))
    n2 = int(input("Insira o segundo número: "))
    return n1, n2

def obter_numero_float():
    n = float(input())
    return n


def somar(n1, n2):
    soma = n1 + n2
    return soma


def subtrair(n1, n2):
    subtracao = n1 - n2
    return subtracao


def multiplicar(n1, n2):
    multiplicacao = n1 * n2
    return multiplicacao


def dividir(n1, n2):
    divisao = n1 / n2
    return divisao