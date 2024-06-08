def fatorial(n, show=False):
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


def escreva(msg):
    tam = len(msg)
    print('~' * tam)
    print(msg)
    print('~' * tam)


#programa principal
escreva('SEJA BEM VINDO, PATRÃO EZEQUIEL!')
while True:
    fato = int(input('Fale um número para ver seu fatorial: '))
    print(fatorial(fato, show=True))
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERROR! Por favor, digite apenas S ou N.')
    if resp == 'N':
        break       
escreva('VOLTE SEMPRE!')
