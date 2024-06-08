#valor = list(int(input(f'Digite um valor para a posição {c-1}: ')) for c in range(1, 6))
#print(f'Voce digitou os valores {valor}')
#print(f'O maior valor digitado foi {max(valor)} nas posições {c}')
#print(f'O menor valor digitado foi {min(valor)}')

#listanum = []
#mai = 0
#men = 0
#for c in range(0, 5):
#    listanum.append(int(input(f'Digite um valor para a posicao {c}: ')))
#    if c == 0:
#        mai = men = listanum[c]
#    else:
#        if listanum[c] > mai:
#            mai = listanum[c]
#        if listanum[c] < men:
#            men = listanum[c]
#print('=-' * 30)
#print(f'Voce digitou os valores {listanum}')
#print(f'O maior valor digitado foi {mai} nas posições ', end='')
#for i, v in enumerate(listanum):
#    if v == mai:
#        print(f'{i}... ', end='')
#print()
#print(f'O menor valor digitado foi {men} nas posições ', end='')
#for i, v in enumerate(listanum):
#    if v == men:
#        print(f'{i}... ', end='')
#print()


lista = []
posicao_maior = []
posicao_menor = []
for p in range(0, 5):
    val = int(input(f'Digite um valor na posição {p}: '))
    lista.append(val)
for posicao, valores in enumerate(lista):
    if valores == max(lista):
        posicao_maior.append(posicao)
    if valores == min(lista):
        posicao_menor.append(posicao)
print(f'Você digitou os valores {lista}')
print(f'O maior valor da lista é {max(lista)}, nas posições {posicao_maior}')
print(f'O menor valor da lista é {min(lista)}, nas posições {posicao_menor}')
