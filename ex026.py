s = float(input('Qual o salário do funcionário? R$'))
if s >= 1250.00:
    aumento = (s * 10/100) + s
else:
    aumento = (s * 0.15) + s
print(f'\033[4;31;43m O novo salario desse funcionario será R${aumento:.2f}\033[m')