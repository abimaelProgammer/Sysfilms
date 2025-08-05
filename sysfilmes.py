# sysfilmes.py
# O código abaixo é um sistema de gerenciamento e avaliação de filmes denominado SysFilmes
# Permite cadastrar filmes, avaliar, listar por título, gênero ou número de estrelas
# Trabalho referente a disciplina de Fundamentos da Programação - CK0211
# Alunos:
# Carlos Abimael Oliveira do Nascimento, matrícula 587010
# João Gabriel dos Santos Araújo, matrícula 582584

import csv
import os
try:
    import unidecode
except ImportError:
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "unidecode"])
    import unidecode
try:
  from IPython.display import clear_output
except ImportError:
  # Clear OutPuts for Terminals
    def clear_output():
      # Check the operating system name
      if os.name == 'nt':  # For Windows
        _ = os.system('cls')
      else:  # For Linux, macOS, and other Unix-like systems
        _ = os.system('clear')


filmes = [] # Lista de filmes cadastrados
arqFilmes = 0
arqAvls = 0

# Mostrar Menu
def mostra_menu(total):
  """
  Função: Mostra o menu de opções. Caso o usuário digite uma opção válida, a função correspondente a ela.

  Parâmetros:
  total (int): Quantidade de filmes adicionados

  Retorna:
  result (int): Opção selecionada
  """
  clear_output()
  print(f"""*********** SysFilmes ***********
******* Existem: {total} filmes *******
*********************************
1. Cadastrar Filme
2. Avaliar Filme
3. Consultar Filme por Título
4. Listar Filmes por Gênero
5. Listar Filmes por Estrelas
6. Listar Todos os Filmes
7. Carregar Filmes de Arquivo
8. Carregar Avaliações de Arquivo
9. Sair do Sistema""")
  while True:
    try:
      result = int(input("Digite a opção desejada: "))
      if 1 <= result <= 9:
        break
      else:
        print("Opção não encontrada!")
    except:
      print("Digite um número!")
  clear_output()
  return result

# Buscar Título de Filme
def busca_titulo(titulo,filmes):
  """
  Função: Busca o filme com o título digitado pelo usuário na lista. Para uma busca mais eficiente, se usa a função unidecode que formata o título de forma padronizada

  Parâmetros:
  titulo (str): Título digitado pelo usuário
  filmes (list): A lista de filmes

  Retorna:
  filme (dict): Se o filme existir na lista, mostra as informações do filme
  """
  try:
    for filme in filmes:
      if unidecode.unidecode(filme['Titulo'].upper()) == unidecode.unidecode(titulo.upper()):
        return filme
    return None
  except Exception as e:
    print("ERRO! ->", e ,"\nTente Novamente:")
    return consulta_titulo(filmes)

# Pedir o Título de um Filme
def consulta_titulo(filmes):
  """
  Função: Recebe o título digitado pelo usuário

  Parâmetros:
  filmes (list): A lista de filmes

  Retorna:
  A função busca_titulo
  """
  try:
    return busca_titulo(input("Digite o título do filme desejado: "),filmes)

  except Exception as e:
    print("ERRO! ->", e ,"\nTente Novamente:")
    return consulta_titulo(filmes)

# Cadastrar um Filme na Lista
def cria_filme(filmes,titulo=None,ano=None,genero=None,main=False):
  """
  Função: Ao escolher a Opção 1, cadastra um filme novo na lista, se o filme não existir (verificação através do busca_titulo)

  Parâmetros:
  filmes (list): A lista de filmes

  Parâmetros Opcionais:
  titulo(str): titulo do filme (se já existir, não irá pedir ao usuário)
  ano(int): ano do filme (se já existir, não irá pedir ao usuário)
  genero(str): genero do filme (se já existir, não irá pedir ao usuário)


  Retorna:
  filmes.append(filme) ou None: Vai adicionar o filme cadastrado na lista 'filmes'  """

  try:
    if titulo == None:
      titulo = str(input("Título: "))
    if busca_titulo(titulo,filmes) == None:
      if ano == None:
        ano = int(input("Ano: "))
      if genero == None:
        genero = str(input("Gênero: "))
      filme = {"Titulo": str(titulo),
             "Ano": int(ano),
             "Genero": str(genero),
             "Estrelas": float(0),
             "Número de Avaliações": int(0)}
      filmes.append(filme)
      if main == False:
        filme = [titulo,int(ano),genero]
        atualiza_filmes(filme)
      return (f"Filme: {titulo} Cadastrado com sucesso")
    return None
  except Exception as e:
     print(f"Erro {e}")
     return cria_filme(filmes,titulo,ano,genero)

# Mostra as Informações de um filme
def mostra_filme(filme):
  """
  Função: A partir da função lista_todos, mostra as informações de cada filme da lista

  Parâmetros:
  filme (dict): Um filme da lista

  Retorna:
  As informações de um filme da lista
  """

  try:
    print(f"Titulo: {filme['Titulo']}\n   Ano: {filme['Ano']}\n   Gênero: {filme['Genero']}\n   Estrelas: {filme['Estrelas']:.2f}\n   Avaliações: {filme['Número de Avaliações']}\n")
  except:
    return "Filme não encontrado"

# Mostra todos os Filmes da Lista
def lista_todos(filmes):
  """
  Função: Ao escolher a opção 6, mostra todos os filmes cadastrados na lista de filmes

  Parâmetros:
  filmes (list): A lista de filmes

  Retorna:
  Se a lista de filmes não estiver vazia, chama a função mostra_filme para cada filme da lista
  """

  if len(filmes) != 0:
    for filme in filmes:
      mostra_filme(filme)
  else:
    return print('Nenhum filme disponível')

# Filtra os filmes da lista por gênero
def lista_genero(genero, filmes):
  """
  Função: Ao escolher a opção 4, mostra todos os filmes da lista com o gênero digitado pelo usuário

  Parâmetros:
  genero (str): O gênero selecionado pelo usuário
  filmes (list): A lista com todos os filmes

  Retorna:
  Se existirem filmes do gênero selecionado, mostra todos os filmes da lista "filmes" com o gênero selecionado atráves da função mostra_filme
  """
  try:
    count = 0
    for filme in filmes:
      if unidecode.unidecode(genero).upper() == unidecode.unidecode(filme['Genero']).upper():
        mostra_filme(filme)
        count += 1
    if count == 0:
      return "Nenhum filme encontrado com esse gênero"
  except:
    return "Gênero Inválido"

# Filtra os filmes da lista por número de estrelas
def lista_estrelas(num, filmes):
  """
  Função: Ao escolher a opção 5, mostra os filmes da lista a partir de um número de estrelas digitado pelo usuário

  Parâmetros:
  num (float): Número de estrelas digitado pelo usuário
  filmes (list): A lista com todos os filmes

  Retorna:
  Todos os filmes com o número de estrelas igual ou superior ao número digitado pelo usuário
  """
  try:
    if num == None:
      num = int(input("Digite o número de estrelas desejado: "))
    if num > 5 or num < 0:
      print("Número de estrelas inválido!")
      return lista_estrelas(None, filmes)
    num = float(num)
    count = 0
    for filme in filmes:
      if (filme['Estrelas'] >= num):
        mostra_filme(filme)
        count+=1
    if count == 0:
      print(f"Não há filmes com {num} Estrelas ou mais")
  except Exception as e:
    print("ERRO! ->", e),
    return lista_estrelas(None, filmes)

# Avalia um filme da lista
def avalia_filme(filmes,titulo=None,avl=None, main=False):
  """
  Função: Ao escolher a opção 2, avalia um filme existente na lista

  Parâmetros:
  filmes (list): A lista de filmes

  Parâmetros opcionais:
  titulo (str): O título do filme
  avl (float): A avaliação que será dada ao filme

  Retorna:
  Adiciona uma avaliação a um filme existente na lista
  """
  try:
    if titulo == None:
      titulo = input("Digite o título do filme desejado: ")
    filme = busca_titulo(titulo, filmes)
    if filme != None:
      if avl == None:
        avl = int(input(f"Quantas estrelas você atribui a esse filme? (1 a 5): "))
      if avl > 5 or avl <= 0:
         print("Avaliação inválida")
         return avalia_filme(filmes,titulo)
      filme['Estrelas'] = (filme['Estrelas'] * filme['Número de Avaliações'] + avl)/(filme['Número de Avaliações']+1) 
      filme['Número de Avaliações'] = filme['Número de Avaliações']+1
      if main == False:
        atualiza_avaliacoes(titulo,avl)
      return [f"Filme: {titulo} foi Avaliado com Sucesso"]
    else:
      return "Filme não encontrado"
  except Exception as e:
    print("ERRO -> ", e, "\nTente Novamente!")
    return avalia_filme(filmes,titulo,avl)

# Carrega um arquivo com filmes
def carrega_filmes(filmes, arq=None, main=False):
  """
  Função: Ao escolher a opção 7, adiciona os filmes de um arquivo para a lista

  Parâmetros:
  filmes (list): A lista de filmes

  Retorna:
  Adiciona os novos filmes à lista
  """
  try: 
    if arq == None:
      arq = input("Nome do arquivo: ")
    with open(f'{arq}', 'r', encoding='utf-8') as arq_filmes:
      lista_filmes = arq_filmes.readlines()
      lista_filmes.pop(0)
      for filme in lista_filmes:
        filme = filme.split(",")
        titulo = filme[0]
        ano = int(filme[1])
        genero = filme[2].strip("\n")
        cria_filme(filmes, titulo, ano, genero,main)
    return("Filmes carregados com sucesso!")
  except Exception as e:
    print(f"ERRO-> {e}")
    return(carrega_filmes(filmes))

# Carrega um arquivo com avaliações
def carrega_avaliacoes(filmes,arq=None, main=False):
  """
  Função: Ao escolher a opção 8, adiciona as avaliações de um arquivo aos filmes existentes na lista

  Parâmetros:
  filmes (list): A lista de filmes

  Retorna:
  Adiciona as avaliações aos filmes na lista
  """
  try:
    nAvl = 0
    if arq == None:
      arq = input("Nome do arquivo: ")
    with open(f'{arq}', 'r') as arq_avl:
      avl_lista = arq_avl.readlines()
      avl_lista.pop(0)
      for avl in avl_lista:
        avl = avl.split(",")
        titulo = avl[0]
        avaliacao = int(avl[1].strip("\n"))
        if avaliacao > 5 or avaliacao < 0:
          return "Arquivo Incompatível"
        nAvl += 1
        avalia_filme(filmes,titulo,avaliacao,main)
    return f"{nAvl} Avaliações foram carregadas"
  except Exception as e:
    print(f"ERRO-> {e}")
    return carrega_avaliacoes(filmes)

# Atualiza os filmes no arquivo
def atualiza_filmes(filme):
  """
  Função: Ao ser adicionado um arquivo de filmes, atualiza esse arquivo salvando todos os filmes que forem cadastrados pelo usuário

  Parâmetros:
  filme (list): A lista com as informações do filme

  Retorna:
  Atualiza o arquivo de filmes a cada novo filme que for cadastrado
  """
  try:
    with open('filmes.csv', 'a', newline='', encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(filme)
        return None
  except Exception as e:
    return f"ERRO -> {e}"

# Atualiza as avaliações no arquivo
def atualiza_avaliacoes(titulo,avl):
  """
  Função: Ao ser adicionado um arquivo de avaliações, atualiza esse arquivo salvando todas as avaliações que forem feitas pelo usuário

  Parâmetros:
  avaliacoes (list): Lista de avaliações

  Retorna:
  Atualiza o arquivo de avaliações a cada nova avaliação que for feita
  """
  try:
    with open('avaliacoes.csv','a', newline='', encoding="utf-8") as arquivo:
      escritor = csv.writer(arquivo)
      att = [titulo, avl]
      escritor.writerow(att)
      return "Avaliações Atualizadas"

  except Exception as e:
    return f"ERRO -> {e}"


# Programa Principal: Exibe o menu e executa as opções até o usuário escolher sair
op = None
carrega_filmes(filmes,"filmes.csv",True)
carrega_avaliacoes(filmes,"avaliacoes.csv",True)
while True:
  try:
    op = mostra_menu(len(filmes))
    if op == 1:
      print("""*********** SysFilmes ***********
******* Cadastrando Filme *******
*********************************""")
      result = cria_filme(filmes)
      if result == None:
        print("Filme já cadastrado")
        input("[**Tecle enter para voltar ao Menu Principal**]\n")
        continue
      print(result)
      input("[**Tecle enter para voltar ao Menu Principal**]\n")
      continue
      
    elif op == 2:
      print("""*********** SysFilmes ***********
******* Avaliação de Filme ******
*********************************""")
      result = (avalia_filme(filmes))
      print(result)
      input("[**Tecle enter para voltar ao Menu Principal**]\n")
      continue
    elif op == 3:
      print("""*********** SysFilmes ***********
*** Consulta Filmes por Título **
*********************************""")
      result = consulta_titulo(filmes)
      if result == None:
        print("Filme não encontrado!")
        input("[**Tecle enter para voltar ao Menu Principal**]\n")
        continue
      mostra_filme(result)
      input("[**Tecle enter para voltar ao Menu Principal**]\n")
      continue
    elif op == 4:
      print("""*********** SysFilmes ***********
*** Listando Filmes por Gênero **
*********************************""")
      genero = input("Digite o gênero desejado: ")
      result = lista_genero(genero,filmes)
      if result != None:
        print(result)
      input("[**Tecle enter para voltar ao Menu Principal**]\n")
      continue
    elif op == 5:
      print("""*********** SysFilmes ***********
** Listando Filmes por Estrelas *
*********************************""")
      estrelas = int(input("Digite o número de estrelas desejado: "))
      lista_estrelas(estrelas,filmes)
      input("[**Tecle enter para voltar ao Menu Principal**]\n")
      continue
    elif op == 6:
      print("""*********** SysFilmes ***********
******** Listando Filmes ********
*********************************""")
      lista_todos(filmes)
      input("""[**Tecle enter para voltar ao Menu Principal**]\n""")
      continue
    elif op == 7:
      print("""*********** SysFilmes ***********
** Carregando Filmes do Arquivo *
*********************************""")
      result = carrega_filmes(filmes)
      print(result)
      input("""[**Tecle enter para voltar ao Menu Principal**]\n""")
      if result == 'Filmes carregados com sucesso!':
        arqFilmes += 1
      continue
    elif op == 8:
      print("""*********** SysFilmes ***********
** Carregando avaliações do Arquivo *
*********************************""")
      if arqFilmes  != arqAvls+1:
        print("Carregue Primeiro o Arquivo de Filmes")
        input("""[**Tecle enter para voltar ao Menu Principal**]\n""")
        continue
      result = carrega_avaliacoes(filmes)
      print(result)
      input("""[**Tecle enter para voltar ao Menu Principal**]\n""")
      continue
    elif op == 9:
      print("""[**Bye, você saiu do SysFilmes!**]""")
      break
  except Exception as e:
    print(f"Erro -> {e}")
    continue
