print('_' * 30)
print('      CADASTRE UMA PESSOA')
print('_' * 30)
maior18 = homens = mulheres = 0
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    print('_' * 30)
    opcao = ' '
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    if idade > 18:
        maior18 += 1
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        print('_' * 30)
    if opcao == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maior18} ')
print(f'Ao todo temos {homens} homens cadastrados.')
print(f'E temos {mulheres} mulheres com menos de 20 anos.')