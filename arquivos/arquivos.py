#abrir o txt no mesmo diretorio
meu_arquivo= open('arquivo.txt')
conteudo_dias = meu_arquivo.read()
##################
#quando esta em outra pasta do diretorio
arquivo  = open('praticas-boasPraticas\dados\dias.txt')
conteudo =arquivo.read()#abri o arquivo e lê ele 
print(conteudo)#imprime o conteudo do txt
##################
#endereço absoluto
arquivo  = open('C:/Users/Dell/aulas/praticas-boasPraticas/dados/dias.txt')#quando esta em outra pasta do diretorio
conteudo =arquivo.read()#abri o arquivo e lê ele 
#ler linha a linha
conteudo =arquivo.readlines()#lista de linhas -- coloca tudo em uma string 
conteudo =arquivo.readline()#ler apenas uma linha
print(conteudo)#imprime o conteudo do txt
##################
#interar -- readlines ou for ou while
arquivo  = open('praticas-boasPraticas\dados\dias.txt')
linha =arquivo.readline()
#le linha a linha ate acabar todo o arquivo
while linha:
  print(linha)
  linha = arquivo.readline()
################

import os

caminho = os.path.join('dados','dias.txt') #roda em win,linux qualquer sostema operacional
def ler_arquivo(caminho):
#endereços relativos - que não limita o caminho- comunica com o sistema operacional construindo caminho
  meu_arquivo=open(caminho)#open(caminho,r)
  conteudo = meu_arquivo.read()
  print(conteudo) 

  meu_arquivo.close()

arquivo = open(os.path.join('arquivos','codigo.txt'))
linhas = arquivo.readlines()
ordenadas = sorted(linhas)
arquivo.close()
#para abrir a escrita em um novo arquivo para escrever nele ordenado
novo_arquivo = open(os.path.join('arquivos','ordenado.txt'),'w')# a - para adicionar(apend) / r- para ler(read) /w- escrver (write) 
for l in ordenadas:
  novo_arquivo.write(l)
novo_arquivo.close()

def escrever_arquivo(caminho):
#escrever em um arquivo
  novo_arquivo = open('arquivos\codigo.txt','w')
  novo_arquivo.write('escrevendo no arquivo')
  novo_arquivo.close()







