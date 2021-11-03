#programa que recebe uma lista de numeros e exibe o maior

numeros = input('digite alguns numeros:\n ')#sempre recebe em string
lista = numeros.split() #quebra a string nos espaços e retorna uma lista
#print(lista)

num = []
for elemento in lista:
    n=float(elemento)
    num.append(n)
    
'''print(lista)    
print(num)'''

maior = -9999999999

for n in num:
    if n > maior:
        maior = n

print('o maior é: ', maior)
print(max(num))   #caminho pronto      


#fazendo em forma de função o que o MAX faz
def maximo(lista):
    maior = -9999999
    for n in num:
        if n > maior:
            maior = n
        
#retornar a media        
def media(lista):
    m=0
    for n in lista:
        #acumula a soma da lista
        m = m + n
    #retorna a media    
    return  print('a media: ' ,m/len(lista))

#fatorial - sem recursão
def fatorial(n):
    produto = 1 
    while n > 0:
        produto = produto *n
    return produto





