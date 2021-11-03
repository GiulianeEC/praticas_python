
def voto_eleitoral(idade):
    if idade >= 16 and idade < 18 or idade >=70:
        return 'facultativo'
    elif idade < 16:
        return 'proibido'
    else:
        return 'obrigatorio'


idade = int(input('digite a idade: '))
print(voto_eleitoral(idade))
        