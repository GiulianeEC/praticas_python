#retorna se é par
def eh_par(n):
    if n % 2 == 0:
        return True
    else:
        return False

#entra como string 
numero = input('digite o numero: ')
#converte para inteiro
numero = int(numero)

if eh_par(numero):
    print (f'{numero} é par')
else:
    print (f'{numero} é impar')