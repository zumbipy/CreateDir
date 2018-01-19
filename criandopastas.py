import sys
import os


def listarDeNomesDePastas(nome_das_pastas=0, inicio=0, fim=0):
    lista_nome_pastas = []
    for pastas in range(inicio, fim + 1):
        numero = str(pastas)
        lista_nome_pastas.append(nome_das_pastas + numero)
    return lista_nome_pastas


def criarPastas(lista_nome_pastas):
    for pastas in lista_nome_pastas:
        print("Pasta {} crianda com sucesso.".format(pastas))
        os.mkdir(pastas)


def main():

    criarPastas(listarDeNomesDePastas(sys.argv[1], int(sys.argv[2]), int(sys.argv[3])))


if __name__ == '__main__':
    main()
