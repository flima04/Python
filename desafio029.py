speed = float(input('Qual a velocidade do veículo, em km/h?'))

multa = (speed-80)*7

if speed <= 80:
    print('Dentro da Velocidade')

else:
    print('Acima da Velocidade! Você foi multado em R${}.' .format(multa))

print('--FIM DO PROGRAMA--')
