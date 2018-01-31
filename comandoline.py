import argparse
from CreateDir import CreateDir

comados = argparse.ArgumentParser(prog="CreateDir",
								  
								  description='Criando varias pastas facilmete por linha de comand')
comados.add_argument('total_pasta', metavar='Obrigatorio Digita uma valor para criar as pastas.', type=int)

comados.add_argument('-n', '--nome', type=str, nargs='+', dest="nome_pasta", default=())
comados.add_argument('-p', '--prefixo', action="store_false", dest="prefixo", default=True)
comados.add_argument('-s', '--sufixo', action="store_true", dest="sufixo", default=False)
comados.add_argument('-i', '--inicio', type=int, default=1, dest="inicio")

var = comados.parse_args()




if __name__ == '__main__':
	CreateDir(var.total_pasta, var.nome_pasta, prefixo=var.prefixo, sufixo=var.sufixo, inicio=var.inicio)