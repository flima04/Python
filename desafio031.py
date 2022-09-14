dist = float(input('Qual a distância do seu destino em Km?'))

if dist<=200:
    print('O valor da sua passagem é R${:.2F}' .format(dist*0.5))

else:
    print('O valor da sua passagem é R${:.2F}' .format(dist*0.45))

print('--FIM DO PROGRAMA--')
