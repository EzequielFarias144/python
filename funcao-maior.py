from time import sleep

def maior(* num):
    cont = maior = 0
    print('-=' * 30)
    print('Analizando os valores passados... ')
    for valor in num:
        print(f'{valor},', end=' ', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo. ')
    print(f'O maior valor informado foi {maior}. ')


#programa principal
maior(1, 2, 55, 20, 1)
maior(0)
maior(8, 9, 6)
