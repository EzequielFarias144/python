while True:
    n = int(input('Quer ver a tabuada de qual número? '))
    print('_' * 30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('_' * 30)
print('PROGRAMA TABUADA ENCERRADO! VOLTE SEMPRE!')
