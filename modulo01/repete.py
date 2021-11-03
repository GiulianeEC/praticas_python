#repetições (iterações) condicionais
#enquanto

numero = 7
while numero > 0:
    print (numero)
    numero = numero - 1
    
repetir = True
while repetir == True:
    idade = input('digite a idade : ')
    idade = int(idade)

    if (idade>= 18 and idade < 70):
        print(f'com {idade} anos, seu voto é obrigatorio!' )
    elif (idade >= 16):
        print(f'com {idade} anos, o voto é facultativo')
    else:
        print(f'com {idade} anos, voce nao pode votar!')

    pergunta = input('deseja verificar a idade? (s/n) ')    
    if pergunta == 's':
        repetir = True
    else:
        repetir = False
        
#lista de dados
#lista de dados com numeros
idade = [12,47,78,8,18]
letras_e_numeros = [15,'biscoito',True,'teste', 67.9]
print(idade[0])
print(idade) #imprime lista completa
print(letras_e_numeros[1])    #imprime posição 1 da lista

#trocar elemento
idade[3]= 25
print(idade)

#adiciona elementos
idade.append(77)
print(idade)
#da para adicionar de outro jeito mas ai é criado uma nova lista
print(idade + [88,12])


#lista dentro de outra lista
dois_colchetes = [[7,9,5]]
print(dois_colchetes[0][1])# lista posição zero elemento posição 1

#iterações definidas FOR
idades= [12,47,78,8,18]
for idade in idades:
    print(idade)#imprime um item por vez
    print(idade +2 )#soma mais 2 em cada item
    print(idade) #vai imprimir a lista um por um com a soma 
    if (idade>= 18 and idade < 70):
        print(f'com {idade} anos, seu voto é obrigatorio!' )
    elif (idade >= 16):
        print(f'com {idade} anos, o voto é facultativo')
    else:
        print(f'com {idade} anos, voce nao pode votar!')
    
#intervalos 
for i in range(3,8,2):# soma dois a dois começando em 3 e finalizando em 8
    print(i)

for i in range(3,8):# imprime de 3 e a 8
    print(i)
#para incrementar de forma decimal (de 0.2 em 0.2 por exemplo) ai é melhor fazer com while pq sao float

idades = [12,47,78,8,18]
nomes = ['joão', 'maria', 'severina', 'pedro','rebeca']
for i in range(5):
    print(f"{nomes[i]} tem {idades[i]} anos")

# len(nomes) #tamanho do comprimento da lista
idades = [12,47,78,8,18,70,2]
nomes = ['joão', 'maria', 'severina', 'pedro','rebeca','jonas','rafa']
for i in range(len(idades)):
    print(f"{nomes[i]} tem {idades[i]} anos")



    



