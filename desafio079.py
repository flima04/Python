lista = []
while True:
    num = int(input('Digite um número: '))
    if num in lista:
        print('Este número já está cadastrado.')
    else:
        lista.append(num)
    opção = str(input('Deseja continuar? (S ou N): ')).strip().upper()[0]
    if opção in 'N':
        break
print(f'Os valores digitados em ordem crescente foram: {sorted(lista)}')