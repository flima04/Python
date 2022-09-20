frase = str(input('Digite uma frase')).strip().upper()
frasesplit = frase.split()
frasejoin = ''.join(frasesplit)
frasereverse = frasejoin[::-1]

if frasereverse == frasejoin:
    print('A frase "{}" ao contrário fica "{}", então ela É UM PALÍNDROMO' .format(frasejoin, frasereverse))
else:
    print('A frase "{}" ao contrário fica "{}", então ela NÃO É UM PALÍNDROMO' .format(frasejoin, frasereverse))
    
print('--Fim do Programa--')