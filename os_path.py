import os


os.getcwd()
aula = os.getcwd()

os.path.basename(os.getcwd()) #entrega o ultimo item do diretório, ou seja a pasta aberta
os.getcwd().split("\\") 
os.getcwd().split("\\")[-1]

os.path.split(aula) #separa em tuplas

os.path.dirname(os.getcwd()) #entrega o nome da base 

os.path.getmtime(aula) # o tempo da modificação da pasta a partir de 1/01/1970

from datetime import datetime
datetime.utcfromtimestamp(os.path.getmtime(aula)) # data de modificação do arquivo

os.path.isfile(aula) #pergunta se é um arquivo
os.path.isdir(aula) #pergunta se é uma pasta

