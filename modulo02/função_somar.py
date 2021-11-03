#funções que ajuda a organizar o programa

def exibe_soma(x,y):
    resultado = x + y
    print (resultado)

def somar(x,y): 
    resultado = x + y
    return resultado
    
exibe_soma(2,3)
a= somar(2,4)
print (a)

# x e y são parâmetros ou argumentos da função
def somar(x, y):
  resultado = x + y
  # o valor em resultado é retornado 
  # para ser usado fora da função
  return resultado
  
a = 7
b = 8
# a e b são passados como argumentos na chamada à
# função. a faz o papel de x; já b, o de y
c = somar(a, b)
# c recebeu o valor retornado pela função somar
print(c)
# temos liberdade de trabalhar com o valor retornado
# e fazer o que quisermos no programa
print(somar(a, c))
print(somar(c, b))