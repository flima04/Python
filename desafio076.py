produtos = ('Lapis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-' * 50)
print(f'{"LISTAGEM DE PREÇOS":^50}')
print('-' * 50)
for n in range(0, len(produtos), 2):
    print(f'{produtos[n]:.<40}', end='')
    n2 = n+1
    print(f'R$ {produtos[n2]:>6.2f}')
print('-' * 50)
