import random

num = random.randint(0, 5)

guess = int(input('Tente adivinhar o número que estou pensando... Digite um número de 0 a 5.'))

if guess == num:
    print('Você acertou! O número que estava pensando era {}' .format(num))

else:
    print('Você errou! O número que estava pensando era {}.' .format(num))

print('--FIM DO PROGRAMA--')