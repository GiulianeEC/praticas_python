'''Variáveis e tipos de dados
Saída de dados
Operações com dados
Conversão de tipos
Controle de fluxo
Entrada de Dados
Formatação de Strings'''
#controles de fluxo (if,else,elif)
#boolean
situação = True #False
if True:
    print ('é verdadeiro')
else:
    print ('é falso')
    
idade = 17
if(idade >=18) and (idade<70):
    print ('obrigado a  votar')
elif idade >=16 or idade>= 70:
    print ('facultativo')
else:
    print ('não é obrigado a votar')
    
#operações logicas -- Tabela verdade    
print ('verdade E verdade:',True and True)
print ('verdade E falso:',True and False)
print ('Falso E falso: ',False and True)
print ('verdade OU verdade:', True or True)
print ('verdade OU falso: ',True or False)
print ('Falso OU falso',False or False)


#operações com dados
#conversões de tipos de dados
type(idade)#retorna o tipo das variaveis
type(True)
idade = '4'
int(idade)
float(idade)
str(7)
print ('palavra' + ' '+ str(7))


#entrada de dados -- input
input('digite algo: ')
valor = input('vai entrar com valor de STRING: ')
int(valor)
numero = int(input('digite algo: '))

#formatação de strings
idade = 18
print ('com '+ str(idade)+'anos, voce é obrigado a votar')
print('com',idade,'anos, voce é obrogado a votar')
print (f'com {idade} anos, voce é obrigado a votar')#o f que separa a string

resposta = 42
k = 5

print(resposta + k)
print(resposta * k)
# repare a mudança de tipo
print(resposta / k)
# divisão inteira
print(resposta // k)
# resto da divisão inteira
print(resposta % k)
# potenciação
print(resposta ** k)











    
