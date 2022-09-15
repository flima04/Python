#Tabuada com FOR

num = int(input('Digite um número'))

for n in range(1,11):
    print('{} x {:2} = {}' .format(num, n, (num*n)))

print('FIM')