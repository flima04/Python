termos = []

num = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

x = num
termos.append(x)

for r in range(0,9):
    x = x*razao
    termos.append(x)

print('Os 10 primeiros termos dessa PA são: {}' .format(termos))