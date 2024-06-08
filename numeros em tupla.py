from random import randint
#numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10),) > esse modo é ruim e antigo.
numeros = tuple(randint(1, 10) for c in range(1, 6)) #esse modo é mais pratico e economiza tempo.
print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')
