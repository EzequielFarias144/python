casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salario? R$'))
anos = int(input('Em quantos anos vai pagar?'))
prestação = casa / (anos * 12)
minimo = salario * 30/100
print(f'Para pagar essa casa de R${casa:.2f} em {anos} anos, a prestação será de R${prestação:.2f}')
if prestação <= minimo:
    print('Emprestimo pode ser CONCEDIDO!')
else:
    print('O empréstimo foi NEGADO!')
