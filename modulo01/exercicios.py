'''1. Escreva um programa que recebe um número inteiro do usuário 
e responde se esse número é par ou não. Um número é dito par se ele é divisível por 2.'''

numero = int(input('digite um valor inteiro: '))
if(numero % 2 == 0):
    print ('numero par!')
else:
    print ('numero impar')


'''2. Reescreva o programa que avalia a obrigatoriedade do voto de outra forma,
mas mantendo as 3 respostas corretas (obrigatório, facultativo, proibido).'''

idade = int(input('digite sua idade: '))
if (idade >= 18) and (idade<70):
    print ('obrigatorio')
elif(idade<=16) or (idade >= 70):
    print ('facultativo')
else:
    print ('proibido')    

#loop thinks     
n = int(input())
i=0
for i in range(0,n):
    print (i*i)    