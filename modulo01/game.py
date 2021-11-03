#jogo Pedra Papel e tesoura
'''
i.pedra vence tesoura
ii.tesoura vence papel
iii.papel vence pedra 
iv. quando ambos são iguais, temos um empate

'''
print('*** PEDRA || PAPEL || TESOURA **')
print('preparem-se jogadores!!' + '\n')

pedra = 0
papel = 1
tesoura = 2
jogar = 's'

while (jogar == 's'):
    jogador_1 = int(input("primeiro jogador, digite 0 p/pedra, 1 p/papel ou 2/tesoura: "))
    jogador_2 = int(input("segundo jogador, digite 0 p/pedra, 1 p/papel ou 2/tesoura: "))
    
    if(0 <= jogador_1 <= 2) and (0<jogador_2<=2):
        if(jogador_1 == jogador_2):
            print('EMPATE! Ninguem ganhou :(')
        elif (jogador_1 - jogador_2 == -2) or (jogador_1 - jogador_2 == 1):
            print('jogador 1 ganhou.')
        else:
            print ('jogador 2 ganhou.')
    else:
        print ('opção invalida')
    jogar = input('deseja jogar novamente? (s - sim e n - nao)')        

print('Fim')

    

