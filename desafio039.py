nasc = int(input('Digite seu ano de nascimento'))
idade = 2022-nasc

if idade < 18:
    print('Voce ainda vai se alistar. Aguarde.')
elif idade == 18:
    print('Hora de se alistar!')
else:
    print('Você já passou do prazo de alistamento!')
