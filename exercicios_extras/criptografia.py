#a-d
#b-e
#c- f
#x - a
#i - l 
#dedfdal

alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l',
            'm','n','o','p','q','r','s','t','u','v','w','x','y','z']

n=len(alfabeto) #retorba o tamanho da lista alfabeto

chave = 3
mensagem = 'AbaCaXi'
mensagem = mensagem.lower() #minusculo para maiusculo 'mensagem.upper()
cifrada=''''''
for letra in mensagem:
    #print(letra)
    #ord() caracter para numero
    #chr() numero para caracter
    #indice = alfabeto.index(letra)
    indice = ord(letra)
    #acahar no alfabeto a letra que esteja chave posições a frente
    #nova_letra = alfabeto[(indice + chave)%26]
    nova_letra = chr((indice + chave)%n)
    #substituir na mensagem a letra pela nov_letra
    cifrada = cifrada + nova_letra
    #exibir mensagem cifrada
    print(mensagem) 
    print(cifrada)
    