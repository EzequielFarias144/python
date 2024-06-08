'''par = []
impar = []
for c in range(0, 7):
    valor = int(input(f'Digite o {c+1}° valor: '))
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
print('=-' * 30)
print(f'Os valores pares digitados foram: {par}')
print(f'Os valores impares digitado foram: {impar}')''' #fiz certo, desse jeito é mais facil mas o exercicio pediu de outro jeito


num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}° valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('=-' * 30)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores impares digitado foram: {num[1]}')
