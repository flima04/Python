print('Posso calcular o volume de tinta necessário para pintar uma parede. Vamos tentar?')

a = float(input('Qual a altura da parede em metros?'))
l = float(input('Agora digite a largura da parede.'))

area = a*l
vol = area/2

print('A sua parede tem uma área de {} metros quadrados. O volume de tinta necessário para pintar esta parede é de {} litros.' .format(area, vol))
