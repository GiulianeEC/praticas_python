import os 

#projeto final

#cadastro
arquivo_cadastro = open('arquivo_cadastro.txt','w')

def cadastro (nome,cpf,numero_titulo,data_nascimento):
    nome = input("Nome do eleitor: ")
    arquivo_cadastro.write(nome)
    cpf = (int(input("Digite seu CPF: ")))
    arquivo_cadastro.write(cpf)
    numero_titulo = int(input("Número do título: "))
    arquivo_cadastro.write(numero_titulo)
    data_nascimento = int(input("Data de nascimento: "))
    arquivo_cadastro.write(data_nascimento)
    #representar que a pessoa votou na ultima eleição

'''[Validação] Crie uma forma de solicitar alguns dos dados da pessoa para verificar se é possível 
emitir sua certidão. Busque a pessoa na sua base de dados (CSV) e verifique se ela está com sua 
situação eleitoral regular (era obrigada a votar e votou ou não era obrigada a votar). 
Caso a pessoa não se encontre no cadastro exiba a mensagem *"Eleitor(a) NÃO Cadastado(a)"*.
Caso a pessoa não possa votar, informe-a de acordo. Caso a situação esteja regular, proceda com 
o passo seguinte.'''  
#validacao   
def validacao():
    pass
 
#Emissao da certidão 
'''[Emissão da Certidão] Você deve gerar um arquivo que simule a Certidão de Quitação Eleitoral. 
Você pode gerar uma simples "certidao.txt" sem problemas, o importante é usar os dados cadastrados 
em uma mensagem que faça sentido. No entanto, existe um arquivo modelo no repositório do curso que 
pode ser usado para gerar um documento com forma de certidão. Vale a pena tentar usar este modelo e 
substituir os campos marcados com $ como $CAMPO$ pelo valor cadastrado correspondente. '''        
def emissao_certidao():
    pass
    

if __name__ == '__main__':
    cadastro()
    validacao()
    emissao_certidao()
    

