from datetime import date

nasc = int(input('Digite seu ano de nascimento'))
idade = (date.today().year)-nasc

if idade < 18:
    saldo = 18 - idade
    print('Voce deverá se alistar em {} ano(s). Aguarde.' .format(saldo))
elif idade == 18:
    print('Você completa 18 anos em {}. Hora de se alistar!' .format(date.today().year))
else:
    saldo = idade - 18
    print('Você já passou do prazo de alistamento! Seu alistamento ocorreu há {} ano(s), em {}.' .format(saldo, (date.today().year - (saldo))))
