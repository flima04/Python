# usuário tenta adivinhar o numero que o pc escolheu, no final mostrar em quantas tentativas ele conseguiu

import random

num = random.randint(0,11)
tentativas = 1
palpite = int(input('Tente adivinhar o número que estou pensando de 0 a 10: '))

while palpite != num:
    palpite = int(input('Tente novamente! Vamos ver se consegue dessa vez. '))
    tentativas += 1

print('Você acertou! O número que estava pensando era {} e você conseguiu adivinhar em {} tentativas.' .format(num, tentativas))
