soma = 0
cont = 0
for c in range(1, 7):
    n1 = int(input(f'Digite o {c} valor: '))
    if n1 % 2 == 0:
        soma += n1
        cont += 1
print(f'Voce informou {cont} números PARES e a soma foi {soma}')