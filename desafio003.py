n = input('Digite algo')

print('Qual o tipo primitivo?', type(n))
print('É numérico?', n.isnumeric())
print('É alfabético?', n.isalpha())
print('É alfanumérico?', n.isalnum())
print('Está em caixa baixa?', n.islower())
print('Está em caixa alta?', n.isupper())
print('Está capitalizado?', n.istitle())
