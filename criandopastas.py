import sys
import os


def lista_nome_dir(nome_das_pastas=0, inicio=0, fim=0):
    lista_nome_pastas = []
    for pastas in range(inicio, fim + 1):
        numero = str(pastas)
        lista_nome_pastas.append(nome_das_pastas + numero)
    return lista_nome_pastas


def criar_pasta(lista_nome_pastas):
    for pastas in lista_nome_pastas:
        print("Pasta {} crianda com sucesso.".format(pastas))
        os.mkdir(pastas)


def vizualizar(lista_nome_pastas):
    for nomes in lista_nome_pastas:
        print(nomes)


def main():
    criar_pasta(lista_nome_dir(sys.argv[1], int(sys.argv[2]), int(sys.argv[3])))


if __name__ == '__main__':
    main()
