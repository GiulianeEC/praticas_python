#word = 'osso'
#invertida = inverter(palavra)
#https://www.youtube.com/watch?v=asNugHKaeRI

palavra = input('digite a palavra: ')
def palindromo(frase):
    '''frase = frase.lower()
    if ' ' in frase:
        indesejados = ',.;:?-'
        palavra = [c for in frase if c not in indesejados]
    else:
        palavra = frase'''
    
    indesejados = ',.;:?-'
    palavra=frase
    inicio = 0
    fim =len(palavra)-1
    for i in range(len(palavra)//2):
        if palavra[inicio] != palavra[fim]:
            return False
        
        inicio = fim + 1
        fim = fim - 1
        while palavra[inicio] in indesejados:
            inicio = inicio + 1
            while palavra[fim] != indesejados:
                fim = fim -1
    return True
    
