n1 = float(input('primeira nota do aluno:'))
n2 = float(input('segunda nota do aluno:'))
n3 = float(input('terceira nota do aluno:'))
n4 = float(input('quarta nota do aluno:'))
m = (n1+n2+n3+n4) / 4
print(f'a média final entre {n1} e {n2} e {n3} e {n4} é igual a {m:.1f}')
if m >= 6.0:
    print('Você passou nessa máteria!PARÁBENS!')
else:
    print('Você não passou nessa materia. QUE PENA, ESTUDE MAIS!')