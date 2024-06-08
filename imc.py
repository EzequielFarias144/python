peso = float(input('Quanto você pesa? '))
altura = float(input('Qual a sua altura? '))
imc = peso / (altura**2)
if imc < 18.5:
    print('você está abaixo do peso, CUIDE DA SUA SAÚDE!')
elif imc >= 18.5 and imc < 25:
    print('Seu peso está bom, PARABÉNS!')
elif imc >= 25 and imc < 30:
    print('Voce esta com sobrepeso, tome mais atenção com sua saude!')
elif imc >= 30 and imc < 40:
    print('Voce esta com OBESIDADE!')
elif imc >= 40:
    print('\033[0;31m Voce esta com obesidade morbida! Tome cuidado, voce pode MORRER!\033[m')
print(f'o seu imc é {imc:.2f}')