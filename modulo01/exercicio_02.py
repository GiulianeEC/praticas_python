'''1- faça um programa que recebe uma lista de numeros reais e exibe o seu maior elemento'''
'''2- faça um programa que recebe uma lista de numeros reais e exibe sua media'''
'''3- dada uma lista de numeros inteiros, faça um programa que responda a soma de todos os numeros pares na lista e o produto de todos os numeros impares'''

lista = [0,2,3,5,4,1,6,8,9,11,20,55,7]
maior =0
soma =0
soma_par=0
produto_impar =1
i=0

for item in lista:
 
  if item > maior:
    maior=item
  soma = item + soma
  media = soma/len(lista)
  if item%2==0:
    par=item
    #print(par)
    soma_par = par+ soma_par
  else:
    impar=item
    #print(impar)
    produto_impar = item * produto_impar  
    
print('tamanho da lista:',len(lista))
print('maior elemento: ',maior)  
print('soma:' ,soma)  
print('media: ',media)
print('soma dos valores par : ',soma_par)
print('produto dos valores impar : ',produto_impar)

'''4- faça um programa que recebe um numero e exiba o fatorial desse numero'''
numero= int(input('escreva o numero: '))
fat=1
i=2
while i<=numero:
  fat=fat*i
  i=i+1
print('o fatoria do numero é : ',fat)

'''5- dada uma lista de numeros inteiros e um numero inteiro desejado, responder qual o indice deste numero na lista'''
cont=0
numero_desejado= int(input('escreva o numero: '))
for item in range(len(lista)):
  indice=lista.index(item)
  if item == numero_desejado:
    print('o numero foi encontrado na posição: ',indice)
else:
  print('nao foi encontrado o numero na lista')

'''6-Faça um programa que verifique se uma string possui caracteres duplicados  '''
'''7- Faça um programa que receba uma string que seja uma combinação dos seguintes caracteres: 
'-', 'a', 't', 'c', 'g'. Eles podem aparecer em qualquer ordem e múltiplas vezes, por exemplo: 
'---agcatg-c-c-a-ttt--' A saída do programa deve ser:
7a) A string de entrada sem os '-' do início. No caso do exemplo: 'agcatg-c-c-a-ttt--'
7b) A string de entrada sem os '-' do final. No caso do exemplo: '---agcatg-c-c-a-ttt'
7c) A string de entrada sem os '-' início e do final. No caso do exemplo: 'agcatg-c-c-a-ttt'''
  

