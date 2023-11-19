import os

#Obter o diretório da pasta que deseja ser alterada

cwd = str(input("Diga o nome da pasta na área de trabalho que deseja organizar"))
diretorio_desktop = "c:\\Users\\Desktop\\Desktop\\"
pasta_organizada = diretorio_desktop + cwd
pasta_organizada 

# criar uma lista de itens da pasta a organizar
c = []
c = os.path.isfile(pasta_organizada) 
c
# colocar todos os arquivos(importante nao extrair as pastas) em uma lista 
d = [ i for i in c if os.path.isfile(i) and '.py' not in i] #lista de itens que nao sao pastas
e = list(d.split('.')[-1])
e


#extrair os ultimos 3 strings dos artigos e por em uma lista afim de obter a extensao de cada arquivo

#remover as duplicatas

#criar pastas nomeadas de acordo com a extensao dos arquivos



#inserir cada arquivo em sua respectiva pasta