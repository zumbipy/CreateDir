import os


class CreateDir(object):

    def __init__(self, numero_pasta, prefixo=None, sufixo=None, inicio=1, nome_pasta=""):
        self.prefixo = prefixo
        self.sufixo = sufixo
        self.inicio = inicio
        self.numero_pasta = numero_pasta
        self.nome_pasta = nome_pasta
        self.lista_nome_pastas = []

    def criar_nomes(self):
        if not self.lista_nome_pastas:
            for pastas in range(self.inicio, self.numero_pasta + 1):
                self.lista_nome_pastas.append(f'{self.nome_pasta}{pastas}')

    def limpar(self):
        self.lista_nome_pastas = []

    def criar_pastas(self):
        for pastas in self.lista_nome_pastas:
            os.mkdir(pastas)

    def visualizar(self):
        for nomes in self.lista_nome_pastas:
            print(nomes)
