import os

# obtem o endereço absoluto
pasta_atual = os.path.abspath('.')
print(pasta_atual)
# compõe endereços concatenando com "/" ou "\"
# com isso, o código funciona em qualquer sistema
caminho = os.path.join(pasta_atual, 'teste.txt')
print(caminho)