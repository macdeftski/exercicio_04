import os
from utils.number_utils import obter_numero_float, obter_numero_int

def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def main():
    limpar_tela()
    aprovados = 0
    reprovados = 0
    total_alunos = 0
    while True:
        print("""
        Insira o número da matrícula do aluno
        """)
        print(">", end=" ")
        matricula = obter_numero_int()
        if matricula == 0:
            break
        print("""
        Insira as notas do aluno
        """)
        print("Nota 1:", end=" ")
        nota1 = obter_numero_float()
        print("Nota 2:", end=" ")
        nota2 = obter_numero_float()
        print("Nota 3:", end=" ")
        nota3 = obter_numero_float()
        media = ((2 * nota1) + (3 * nota2) + (5 * nota3)) / 10
        if media >= 7:
            aprovados += 1
            total_alunos += 1
        else:
            reprovados += 1
            total_alunos += 1
        print(f"""
        Total de alunos = {total_alunos}
        Total de alunos aprovados = {aprovados}
        Total de alunos reprovados = {reprovados}
        """)


main()