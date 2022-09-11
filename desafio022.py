# Ler um nome, mostra-lo maiusculo, minusculo, so o primeiro nome, quantos caracteres ele tem no total e quantos so o primeiro nome tem.

nomecompleto = str(input('Digite seu nome completo')).strip()

print('Seu nome maiusculo é:', nomecompleto.upper())

print('seu nome minusculo é:', nomecompleto.lower())

separado = nomecompleto.split()

print('Seu primeiro nome é:', separado[0])

print('Seu primeiro nome tem quantas letras?', nomecompleto.find(' '))

print('Seu primeiro nome tem quantas letras?', len(separado[0]))

print('Quantos caracteres tem seu nome completo?', len(nomecompleto) - nomecompleto.count(' '))
