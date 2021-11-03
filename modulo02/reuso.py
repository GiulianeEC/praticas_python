#save - salvar em arquivo
def save(mensagem):
    #salva mensagem no arquivo
    arquivo = open('mensgem.txt','w')
    arquivo.write(mensagem)
    arquivo.close()
    
def status_voto (idade):
    if (idade>= 18 and idade < 70):
        return 'obrigatorio'
    elif (idade >= 16):
        return 'facultativo'
    else:
        return 'proibido'
    

idade = int(input('digite a idade : '))
resposta = status_voto(idade)
#print(f"com {idade} anos, seu voto é {resposta}")
save(f"com {idade} anos, seu voto é {resposta}")#cria um arquivo de texto é escreve essa mensagem lá