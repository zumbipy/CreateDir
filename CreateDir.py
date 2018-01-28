import os


class CreateDir(object):

    def __init__(self, numero_pasta, *nome_pasta, prefixo=False, sufixo=False, inicio=1):
        self.prefixo = prefixo
        self.sufixo = sufixo
        self.inicio = inicio
        self.numero_pasta = numero_pasta
        self.nome_pasta = nome_pasta
        self.lista_nome_pastas = []

    def criar_nomes(self):
        if not self.lista_nome_pastas:
            nome = self.nome_pasta
            if self.prefixo and self.sufixo:
                for pastas in range(self.inicio, self.numero_pasta + 1):
                    if pastas <= len(nome):
                        self.lista_nome_pastas.append(f'{pastas}{nome[pastas-1]}{pastas}')
                    else:
                        self.lista_nome_pastas.append(f'{pastas}')

            elif self.prefixo:
                for pastas in range(self.inicio, self.numero_pasta + 1):
                    if pastas <= len(nome):
                       self.lista_nome_pastas.append(f'{pastas}{nome[pastas-1]}')
                    else:
                        self.lista_nome_pastas.append(f'{pastas}')

            elif self.sufixo:
                for pastas in range(self.inicio, self.numero_pasta + 1):
                    if pastas <= len(nome):
                       self.lista_nome_pastas.append(f'{nome[pastas-1]}{pastas}')
                    else:
                        self.lista_nome_pastas.append(f'{pastas}')
            elif len(self.nome_pasta) is 1:
                for pastas in range(self.inicio, self.numero_pasta + 1):
                    self.lista_nome_pastas.append(f'{self.nome_pasta[0]}')
            else:
                for pastas in range(self.inicio, self.numero_pasta + 1):
                    self.lista_nome_pastas.append(f'{pastas}')

    def limpar(self):
        self.lista_nome_pastas = []

    def criar_pastas(self):
        for pastas in self.lista_nome_pastas:
            os.mkdir(pastas)

    def visualizar(self):
        for nomes in self.lista_nome_pastas:
            print(nomes)
"""
    def verificando_lista(self, nome_pasta):
        if len(nome_pasta) == 1:
            nome = nome_pasta[0]
            nome_pasta = [nome for nome in range(self.numero_pasta)]
        else:
            return nome_pasta
"""
