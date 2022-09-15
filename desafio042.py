seg1 = float(input('Digite o tamanho do primeiro segmento'))
seg2 = float(input('Digite o tamanho do segundo segmento'))
seg3 = float(input('Digite o tamanho do terceiro segmento'))

if seg1<seg2+seg3 and seg2<seg1+seg3 and seg3<seg1+seg2:
    if seg1 == seg2 == seg3:
        print('O triangulo a ser formado é o EQUILÁTERO')

    elif seg1 == seg2 or seg1 == seg3 or seg2 == seg3:
        print('O triangulo a ser formado é o ISÓSCELES')

    elif seg1 != seg2 != seg3:
        print('O triangulo a ser formado é o ESCALENO')
else:
    print('Não é possível formar um triangulo com esses segmentos.')
