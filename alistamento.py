from datetime import date
ano = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - ano
print(f'Quem nasceu em {ano} tem {idade} anos em {atual}')
if idade == 18:
    print('Você tem que se ALISTAR!')
elif idade < 18:
    print('Você não tem que se alistar,AINDA BEM!')
elif idade > 18:
    saldo = idade - 18
    print(f'Você já deveria ter se alistado há {saldo} anos')
    anos = atual - saldo
    print(f'\033[31m Seu alistamento foi em {anos}')
