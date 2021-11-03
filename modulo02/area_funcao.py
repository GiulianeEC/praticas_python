'''
Tópicos abordados

* Definição de funções
* Uso de funções
* Resolução de exercícios

'''

def perimetro (a,b,c):
    return a+b+c 

def validar (a,b,c):
    if abs(b - c) < a and a > (b +c):
        return True
    return False         
        
def area_triangulo(a,b,c):
    p = perimetro(a,b,c)/2 
    return p       

def traingulo_valido(a,b,c):
    if validar (a,b,c) and validar (b,c,a) and validar (c,a,b):
        #semi-periodo
        p = perimetro(a,b,c)/2
        #formula de heron
        area = (p*(p-a)*(p-b)*(p-c))**(1/2)
        return area
    #triangulo impossivel
    return 0

    
a = float(input('Lado 1: '))
b= float(input('Lado 2: '))
c= float(input('Lado 3: '))
    
area = area_triangulo(a,b,c)
print(f'Area do trinagulo é: {area}')

