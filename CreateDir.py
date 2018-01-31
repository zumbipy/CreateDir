import os


class CreateDir(object):
    """ Esta Classe criar um nome com padrões definidos pelo o usuario.
    Tendo como objetivo agilizar a criação de varias pastas com nomes parecidos ou ate diferente 
    com numeração no começo ou no final.

    Paramentro Obrigatorio:
        total_pasta: Valor *Obrigatorio ,Servi para sabemos quantas pastas seram criadas
                    se valor for 0 as pastas não deram numeros.

    Parametros Opcionais:
        nome_pasta: Nome da pasta ou Listas de nomes de pasta
        prefixo: Por padãro esta em True, Para Desativa False para desativa
        sufico: Por padrão False, Para ativa colore True
        inicio: Por padrão 0 quaso a pasta começe com outra numerção e so coloca o número
        """

    def __init__(self, total_pasta, nome_pasta, prefixo=True, sufixo=False, inicio=1):
        # Variaveis resposavel para criação do nome das pastas.
        self.prefixo = prefixo
        self.sufixo = sufixo
        self.lista_nome_pastas = list(nome_pasta)

        # Váriaveis para criação das do total de pasta.
        self.total_pasta = total_pasta
        self.inicio = inicio

        # Métodos.
        self.correcao_nomes_pastas()
        self.criar_nomes()

    def criar_nomes(self):
        """ Criar o nome das pastas"""
        self.prefixo_nome_sufixo()
        self.visualizar()
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

    def correcao_nomes_pastas(self):
        """ Pega a lista de nome de pasta e deixa do mesmo tamanho do total de pastas a se criado"""

        # Aqui crio uma variavel que recebe a diferença de valor entre total_pasta com lista_nome_pastas.
        t_pasta = self.total_pasta - len(self.lista_nome_pastas)

        # Se lista_nome_pastas tive so um elemento o mesmo sera nome de todas as pastas.
        if len(self.lista_nome_pastas) == 1:
            nome = self.lista_nome_pastas[0]
            for i in range(t_pasta):
                self.lista_nome_pastas.append(nome)

        # Se lista_nome_pastas for 0 então as pasta "" <-- str() vazia.
        elif len(self.lista_nome_pastas) == 0:
            nome = ''
            for i in range(t_pasta):
                self.lista_nome_pastas.append(nome)

        # Existe a possibilidade da pasta não te nome se uma str '' o OS não aceita dando erro então
        # Para resolver este problema o Codigo Repete o nome "Sem Nome" no lugar da str
        elif not(self.prefixo) and self.total_pasta > len(self.lista_nome_pastas) and not(self.sufixo):
            nome = "Sem Nome"
            for i in range(t_pasta):
                self.lista_nome_pastas.append(nome)
        # Ultimo caso e quando pasta não tem nome é ele sera o numero.
        else:
            for i in range(t_pasta):
                self.lista_nome_pastas.append("")

    def prefixo_nome_sufixo(self):
        """ Adicionado prefixo ou sufixo no nome atual lista_nome_pastas. """
        contador = 0
        for numero in range(self.inicio, self.total_pasta + 1):

            prefixo = self.verdade_ou_falso(self.prefixo, numero)
            sufixo = self.verdade_ou_falso(self.sufixo, numero)

            nome_pasta = self.lista_nome_pastas[contador]
            novo_nome = f"{prefixo}{nome_pasta}{sufixo}"
            self.lista_nome_pastas[contador] = novo_nome

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
        while True:
            sim_nao = input("Criar pastas [s] - sim ou [n] - não: ").lower()
            if sim_nao == 's':
                return True
                break
            if sim_nao =='n':
                return False
                break

        