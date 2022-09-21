num = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA:'))
resposta = 10

print('Os 10 primeiros termos dessa PA são:')
while resposta != 0:
    for r in range (resposta, 0, -1):
        print(num, end=' -> ')
        num += razao
        resposta -= 1
        
print('ACABOU')