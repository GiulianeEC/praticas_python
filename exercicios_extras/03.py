#Faça uma função que calcule o n-ésimo termo (aquele que fica na posição número n) da sequência de Fibonnaci.
n=int(input('numero:'))

#forma recursiva
'''def fibo(n):
  if n <= 1:
    return n
  else:
    return fibo(n-1) + fibo(n-2)'''

#forma nao recursiva
def fibo(n):
  f0 = 0
  f1 = 1
  for k in range(1,n+1):
    f2 = f0 + f1
    f0 = f1
    f1 = f2
  return f0

print (fibo(n))