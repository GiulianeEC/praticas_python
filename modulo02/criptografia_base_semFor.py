#criptografia com cifra de césar
'''a -> d 
b -> e 
c -> f 
x -> a 
y -> b
z -> c
ou pela tabela de ASCII'''

def cifra_cesar(chave,letra):
  print(ord(letra))
  return chr(ord(letra)+chave)

entrada='a'
resposta = cifra_cesar(3,entrada)
print(f'a crifra de {entrada} é {resposta}')


