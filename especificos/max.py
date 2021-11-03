# lista de exemplo
lista = [7,3,9,1,2,3,6]
# iniciamos o valor de maior, com um valor pequeno, que sabemos que não estará na lista
maior = -999999999999
if len(lista) > 0:
  indmaior = 0
  for i in range(len(numeros)):
    if numeros[i] > maior:
    # atualizamos o maior número visto até o momento
      maior = numeros[i]
    # guardamos seu índice também
    indmaior = i
      # Ao final, você terá o maior elemento na variável `maior` e o seu índice na lista na variável `indmaior`
  print(f"O maior elemento da lista é {maio} no índice {indmaior}")
else:
    print("lista vazia!")