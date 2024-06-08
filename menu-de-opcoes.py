from time import sleep
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo numero: '))
opção = 0
while opp != 5:
    print('''[ 1 ] somar
[ 2 ] multipllica
[ 3 ] maior
[ 4 ] novos numeros 
[ 5 ] sair do programa''')
    opp = int(input('>>>>> Qual é a sua opção? '))
    if opp == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} + {n2} é {soma}')
    elif opp == 2:
        multi = n1 * n2
        print(f'A multiplicacao entre {n1} x {n2} é {multi}')
    elif opp == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior valor é {maior}')
    elif opp == 4:
        print('Informe os números novamentes:')
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo numero: '))
    elif opp == 5:
        print('Finalizando...')
        sleep(2)
    else:
        print('OPÇÃO INVALIDA! TENTE NOVAMENTE!')
    print('=-=' * 10)
    sleep(1)
print('Fim do programa! Volte sempre!')
