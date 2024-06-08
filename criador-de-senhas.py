import random

print('Bem vindo ao meu gerador de senhas!')

carac = 'abcdefgahijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12345567890!@#$%&*()/,.;:?°çÇâÂãÃ'

quantsenhas = int(input('Quantas senhas você quer? '))

caracteres = int(input('Quantos caracteres? '))

print('\nAqui estao suas senhas: ')

for pwd in range(quantsenhas):
    senha = ''
    for c in range(caracteres):
        senha += random.choice(carac)
    print(senha)
