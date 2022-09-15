num = int(input('Digite um número: '))

if num > 3 and num % 2 != 0 and num % 5 != 0 or num % 3 != 0:
    print('O numero {} é primo.' .format(num))
elif num == 2 or 3:
    print('O numero {} é primo.' .format(num))
else:
    print('O numero {} NÃO é primo.' .format(num))
