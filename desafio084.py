lista = []
pessoa = []

while True:
    pessoa.append(str(input('Qual o nome? ')))
    pessoa.append(float(input('Qual o peso (em kg)? ')))
    lista.append(pessoa[:])
    print(lista)
    print(pessoa)
    pessoa.clear()
    opção = str(input('Deseja continuar (S ou N)? ')).strip().upper()[0]
    if opção in 'N':
        break
