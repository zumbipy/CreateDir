import os
import argparse


class CreateDir(object):
    """Esta Classe criar um nome ou nomes definidos pelo usuário.
        Tendo como objectivo agilizar a criação de varias pastas com nomes parecidos ou ate diferentes
        com numeração no começo ou no final
    """

    def __init__(self, total_pasta, nome_pasta, prefixo=False, inicio=1, sim=False):
        # Variaveis resposavel para criação do nome das pastas.
        self.prefixo = prefixo
        self.sufixo = True if not prefixo else False  # prefixo verdade sufixo falso
        self.lista_nome_pastas = nome_pasta

        # Váriaveis para criação das do total de pasta.
        self.total_pasta = total_pasta
        self.inicio = inicio

        # confirmação de craição de pasta
        self.sim_ou_nao = sim

        # Métodos.
        self.nomeando_pastas()
        self.criar_nomes()

    def criar_nomes(self):
        """ Craindo nomes nas pastas."""
        self.prefixo_nome_sufixo()
        self.visualizar()

        # Criar pasta só se self.total_pasta for maior que 0.
        if self.lista_nome_pastas:
            self.criar_pastas()

    def criar_pastas(self):
        """ Criar as pastas no OS."""
        if self.sim_nao():
            for pasta in self.lista_nome_pastas:
                os.mkdir(pasta)

    def visualizar(self):
        """ Visualiza os nomes das pastas."""
        for nome in self.lista_nome_pastas:
            print(nome)

    def nomeando_pastas(self):
        len_nome_pasta = len(self.lista_nome_pastas)
        if len_nome_pasta == 1:
            nome = self.lista_nome_pastas[0]
            self.lista_nome_pastas = [nome] * self.total_pasta
        else:
            for numero in range((self.total_pasta - len_nome_pasta)):
                self.lista_nome_pastas.append("")

    def prefixo_nome_sufixo(self):
        """ Pega um elemento dentro da lista_nome_pasta e acrecenta prefixo ou sufixo. """
        contador = 0

        for numero in range(self.inicio, (self.total_pasta + self.inicio)):

            # Validação se True retorna numero se False retorna nada.
            prefixo = self.verdade_ou_falso(self.prefixo, numero)
            sufixo = self.verdade_ou_falso(self.sufixo, numero)

            # Pega o valor e o modificar.
            nome_pasta = self.lista_nome_pastas[contador]
            self.lista_nome_pastas[contador] = f"{prefixo}{nome_pasta}{sufixo}"

            contador += 1

    def verdade_ou_falso(self, verifica, numero):
        """ Validação simples """

        # Se verdade adicionar o numero se não adicionar str vazia.
        if verifica:
            return numero
        else:
            return ''

    def sim_nao(self):
        """ Verificar se tem certeza que vai criar as pastas no OS """
        if self.sim_ou_nao:
            return True
        while True:
            sim_nao = input("Criar pastas [s] - sim ou [n] - não: ").lower()
            if sim_nao == 's':
                return True
                break
            if sim_nao == 'n':
                return False
                break


comados = argparse.ArgumentParser(prog="cdir.py",
                                  usage='''cdir.py *[Numero De Pastas] -n 'Nome' -p -i [numero]

Criando varias pastas facilmete por linha de comando.
Obs: "Primeiro valor é Obrigadorio."""

Comandos Básicos:
    cdir.py 3 -n " - Aula"
        Aula - 1
        Aula - 2
        Aula - 3

    cdir.py 3 -n "Aula - " -p
        1 - Aula
        2 - Aula
        3 - Aula

     cdir.py 3 -n "Aula - " "Curso - " -i 100
        Aula - 100
        Curso - 101
        102
 ''',
                                  epilog="final linha")


comados.add_argument('total_pasta', type=int,
                     help="Valor Total de quantas pasta será criada.")
comados.add_argument('-n', type=str, nargs='+', default=[],
                     help="Nome ou Nomes para as pastas")
comados.add_argument('-p', action="store_true", default=False,
                     help="Coloca numero depois do Nome da pasta.")
comados.add_argument('-i', type=int, default=1,
                     help="Numero que iniciar o valor das pastas")
comados.add_argument('-s', action="store_true", default=False,
                     help="Criar as pastas sem fazer pergunta.")
var = comados.parse_args()


if __name__ == '__main__':
    print(var)
    CreateDir(var.total_pasta, var.n, prefixo=var.p,
              inicio=var.i, sim=var.s)
