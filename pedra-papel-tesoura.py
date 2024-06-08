from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
escolha = int(input('Qual é a sua jogada? '))
print('-=' * 11)
print(f"jogador jogou {itens[escolha]}")
print(f'Computador jogou {itens[computador]}')
print('-=' * 11)
if computador == 0:
    if escolha == 0:
        print('EMPATE')
    elif escolha == 1:
        print('JOGADOR VENCE')
    elif escolha == 2:
        print('COMPUTADOR VENCE, VOCê PERDEU')
    else:
        print('JOGADA INVÁLIDA!')
if computador == 1:
    if escolha == 0:
        print('COMPUTADOR VENCE, VOCê PERDEU')
    elif escolha == 1:
        print('EMPATE')
    elif escolha == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
if computador == 2:
    if escolha == 0:
        print('JOGADOR VENCE')
    elif escolha == 1:
        print('COMPUTADOR VENCE, VOCê PERDEU')
    elif escolha == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')
