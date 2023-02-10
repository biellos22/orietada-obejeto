'''cálculo de média de 4 notas => 7 aprovado
<7 >= 4 = Exame final <4 reprovado'''

n1 = float(input('Digite sua 1° nota: '))
n2 = float(input('Digite sua 2° nota: '))
n3 = float(input('Digite sua 3° nota: '))
n4 = float(input('Digite sua 4° nota: '))

resultado = (n1 + n2 + n3 + n4) / 4

if resultado >= 7:
    print('Aprovado')
elif resultado >= 4 and resultado < 7:
    print('Exame final')
else:
    print('Reprovado')