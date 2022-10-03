lista = []
pares = []
impares = []
while True:
    num = int(input('Digite um numero: '))
    lista.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    opção = str(input('Deseja continuar (S ou N)? ')).strip().upper()[0]
    if opção in 'N':
        break
print(f'Os numeros digitados foram: {lista}')
print(f'Os numeros pares são: {pares}')
print(f'Os numeros impares são: {impares}')
