import os


class CreateDir(object):
    def __init__(self, total_pasta, *nome_pasta, prefixo=True, sufixo=False, inicio=1):
        self.prefixo = prefixo
        self.sufixo = sufixo
        self.lista_nome_pastas = list(nome_pasta)

        self.total_pasta = total_pasta
        self.inicio = inicio

        self.nome_pasta_correcao()
        self.criar_nomes()

    def criar_nomes(self):
        self.prefixo_nome_sufixo()
        self.visualizar()

    def criar_pastas(self):
        for pasta in self.lista_nome_pastas:
            os.mkdir(pasta)

    def visualizar(self):
        for nome in self.lista_nome_pastas:
            print(nome)

    def nome_pasta_correcao(self):
        t_pasta = self.total_pasta - len(self.lista_nome_pastas)
        if len(self.lista_nome_pastas) == 1:
            nome = self.lista_nome_pastas[0]
            for i in range(t_pasta):
                self.lista_nome_pastas.append(nome)

        elif len(self.lista_nome_pastas) == 0:
            nome = ''
            for i in range(t_pasta):
                self.lista_nome_pastas.append(nome)

        elif not(self.prefixo) and self.total_pasta > len(self.lista_nome_pastas) and not(self.sufixo):
            nome = "Sem Nome"
            for i in range(t_pasta):
                self.lista_nome_pastas.append(nome)
        else:
            for i in range(t_pasta):
                self.lista_nome_pastas.append("")

    def prefixo_nome_sufixo(self):
        contador = 0
        for numero in range(self.inicio, self.total_pasta + 1):

            prefixo = self.verdade_ou_falso(self.prefixo, numero)
            sufixo = self.verdade_ou_falso(self.sufixo, numero)

            nome_pasta = self.lista_nome_pastas[contador]
            novo_nome = f"{prefixo}{nome_pasta}{sufixo}"
            self.lista_nome_pastas[contador] = novo_nome

            contador += 1

    def verdade_ou_falso(self, verifica, numero):
        if verifica:
            return numero
        else:
            return ''


lista = ["rogerio", "karina", "rodrigo", "marcos"]

print("teste com um nome so")
print("-" * 50)
so_nome = CreateDir(10, "so_nome", prefixo=False)
prefixo_so_nome = CreateDir(10, " - prefixo_so_nome")
so_nome_sufixo = CreateDir(10, "so_nome_sufixo - ", prefixo=False, sufixo=True)
so_numero = CreateDir(10)
print("-" * 50)
print("teste com um dic_nomes")
print("-" * 50)


so_nome = CreateDir(10, "rogerio", "karina", "rodrigo", "marcos", prefixo=False)


print(so_nome.lista_nome_pastas)
prefixo_so_nome = CreateDir(10, "rogerio", "karina", "rodrigo", "marcos")
so_nome_sufixo = CreateDir(10, "rogerio", "karina", "rodrigo", "marcos", prefixo=False, sufixo=True)
so_numero = CreateDir(10)
print("-" * 50)
so_nome = CreateDir(0, "rogerio", "karina", "rodrigo", "marcos", prefixo=False)
so_nome = CreateDir(1, "so_nome", )
