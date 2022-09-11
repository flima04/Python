frase = str(input('Digite uma frase.')).strip()

fraselower = frase.lower()

fraseprimeiro = fraselower.find('a')+1

fraseultimo = fraselower.rfind('a')+1

print('Sua frase possui {} vogais "A".' .format(fraselower.count('a')))

print('A posição da primeira vogal "A" é:', fraseprimeiro)

print('A posição da última vogal "A" é:', fraseultimo)
