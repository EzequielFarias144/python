print('_' * 30)
print('        LOJA DO EZEQUIEL')
print('_' * 30)
total = totmil = menor = cont = 0
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    total += preco
    cont += 1
    if preco > 1000:
         totmil += 1
    if cont == 1:
        menor = preco
    else:
        if preco < menor:
            preco = menor
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if opcao == 'N':
        break
print('fim do programa')
print(f'o total da compra foi R$ {total:.2f}')
print(f'temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi de R${menor:.2f}')
