#CSV - valores separados por virgula
colunas =['nome','linguagem','idade']

nome = input('digite seu nome: ')
ling=('linguagem em que é + proficiente: ')
idade =int(input('digite sua idade: '))

meu_cvs=open('modulo02/teste.csv','a')
meu_csv = open('teste.csv','w')
meu_csv.write(','.join(colunas)+'\n')#virgula como separador, o join une tudo que ta na lista como uma unica string e a virgula é o separador
meu_csv.write(','.join([nome,ling,str(idade)])+'\n')#precisa passar pro join uma lista so com string
meu_csv.close()

#HTML
pagina=open('dados/certidao.html')
conteudo = pagina.read()
atualizada = conteudo.replace('$NOME', 'Giuliane')
pagina.close()

nova_pagina = open('dados/certidao.html','w')
nova_pagina.write(atualizada)
nova_pagina.close()