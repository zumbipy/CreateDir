import os


class CreateDir(object):

    def __init__(self, numero_pasta, *nome_pasta, prefixo=False, sufixo=False, inicio=1):
        self.inicio = inicio
        self.numero_pasta = numero_pasta + 1
        self.prefixo = prefixo
        self.sufixo = sufixo
        self.nome_pasta = nome_pasta
        self.lista_nome_pastas = []

    def criar_nomes(self):
        if self.prefixo:
            nome = self.nome_pasta
            if len(self.nome_pasta) == 1:
                for n in range(self.inicio, self.numero_pasta):
                    self.lista_nome_pastas.append(f"{n}{nome[0]}")
            else:
                for n in range(self.inicio, self.numero_pasta):
                    if n <= len(self.nome_pasta):
                        self.lista_nome_pastas.append(f"{n}{nome[n - 1]}")
                    else:
                        self.lista_nome_pastas.append(f"{n}")
        elif self.sufixo:
            nome = self.nome_pasta
            if len(self.nome_pasta) == 1:
                for n in range(self.inicio, self.numero_pasta):
                    self.lista_nome_pastas.append(f"{nome[0]}{n}")
            else:
                for n in range(self.inicio, self.numero_pasta):
                    if n <= len(self.nome_pasta):
                        self.lista_nome_pastas.append(f"{nome[n - 1]}{n}")
                    else:
                        self.lista_nome_pastas.append(f"{n}")

        elif (self.numero_pasta - 1) == 0:
            for n in self.nome_pasta:
                self.lista_nome_pastas.append(f"{n}")

        elif self.nome_pasta:
            nome = self.nome_pasta
            for n in range(self.inicio, self.numero_pasta):
                self.lista_nome_pastas.append(f"{nome[0]}")
        else:
            for n in range(self.inicio, self.numero_pasta):
                self.lista_nome_pastas.append(f"{n}")

    def criar_pastas(self):
        for pastas in self.lista_nome_pastas:
            os.mkdir(pastas)

    def visualizar(self):
        for nomes in self.lista_nome_pastas:
            print(nomes)
