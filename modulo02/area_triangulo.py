a = float(input('Lado 1:' ))
b = float(input('Lado 2:' ))
c = float(input('Lado 3:' ))

#primeiro e pior
'''if abs(b-c) < a and a<b+c:
    if abs(a-c) < b and b<a+c:
        if abs (a-b) < c:
            p=(a+b+c)/2
            area = (p*(p-a)*(p-b)*(p-c))**(1/2)
            print('a area é: ', area)
        else:
            print('triangulo impossivel')
    else:
        print('triangulo impossivel')
else: 
    print('triangulo impossivel')'''
    
#segundo jeito    
'''if (abs(b-c) < a and a<b+c
    and (abs(a-c) < b and b<a+c) 
    and ( abs (a-b) < c)):
           
    p=(a+b+c)/2
    area = (p*(p-a)*(p-b)*(p-c))**(1/2)
    print('a area é: ', area)   
        
else: 
    print('triangulo impossivel') '''   
                    
#para calcular o perimetro
p= (a + b + c)/2
#area dada pela area de heron
(p*(p-a) * (p-b) * (p-c)) ** (1/2)

#usando função
def verificar_lado (a,b,c):
    if (b-c) < a and a<b+c:
        return True
    else:
        return False
    
if verificar_lado(a,b,c) and verificar_lado(b,a,c)  and verificar_lado(c,b,a):
    p=(a+b+c)/2
    area = (p*(p-a)*(p-b)*(p-c))**(1/2)
    print('a area é: ', area) 
else:
    print('triangulo impossivel')

