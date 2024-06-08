from random import randint
computador = randint(0, 10)
print('Sou seu computador...')
print('''Acabei de pensar em um número entre 0 e 10.
Sera que voce consegue adivinhar qual foi?''')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez')
print(f'voce acertou com {palpite} tentativas. Parabéns')
