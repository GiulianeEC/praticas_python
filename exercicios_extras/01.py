#Escreva uma função que verifica se duas listas são iguais.
lista_01 = [0,1,2,3,4]
lista_02 = [0,10,3,4,50]
#lista_02 = [4,3,2,1,0]

def verifica (lista_01, lista_02):
    #lista itens diferentes
    #lista_diferentes = list(set(lista_02) - set(lista_01))
    lista_diferentes = [x for x in lista_02 if x not in lista_01]
    #lista itens iguais
    lista_iguais = [x for x in lista_02 if x in lista_01]
    
            
    print(lista_diferentes)
    print(lista_iguais)

verifica (lista_01, lista_02)    

'''def elementos_identicos(lista_01):
    return True if len(lista_01) == lista_01.count(lista_01[0]) else False


print(elementos_identicos(lista_02))'''

#verifica(lista_01, lista_02)