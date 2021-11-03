#verificar se tem caracteres duplicados em string

def tem_duplicado(palavra):
  vistos=[]
  for c in palavra:
    if c in vistos:
      return True
    vistos.append(c)  
  return False    


if tem_duplicado('abacaxi'):
  print('tem duplicados')
else:
    print("nao tem duplicados")