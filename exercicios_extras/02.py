#2-Escreva uma função que recebe um número inteiro (n) 
#como argumento e responde a soma de todos os números inteiros de 1 até este n.

numero = int(input('digite um numero inteiro: '))

def soma(numero):
    i=1
    s=0
    while i <= numero:
        s = i + s
        i=i+1
    print(s)
      
          
soma(numero)     