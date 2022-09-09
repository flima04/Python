import math

catetooposto = float(input('Digite o comprimento do cateto oposto'))
catetoadj = float(input('Digite o comprimento do cateto adjacente'))

hipo = math.hypot(catetooposto, catetoadj)

print('o comprimento da hipotenúsa é {:.2f}' .format(hipo))
