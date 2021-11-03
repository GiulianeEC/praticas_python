def buscar(lista,elemento):
    indice = None #none significa vazio
    for i in range (len(lista)):
       if lista[i]==elemento: 
        indice = i
    return indice

numeros = [1,0,2,3,4,5,6]
print(buscar(numeros,4))
print(sorted(numeros))#FUNÇÃO QUE ORDENA A LISTA