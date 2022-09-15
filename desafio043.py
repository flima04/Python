peso = float(input('Digite o seu peso em Kg'))
altura =float(input('Digite a sua altura em metros'))

imc = peso/(altura**2)

if imc < 18.5:
    print('Seu IMC é {:.2f} e você está abaixo do peso.' .format(imc))
elif imc >= 18.5 and imc <= 25:
    print('Seu IMC é {:.2f} e você está no peso ideal.' .format(imc))
elif imc > 25 and imc <=30:
    print('Seu IMC é {:.2f} e você está em sobrepeso.' .format(imc))
elif imc > 30 and imc <= 40:
    print('Seu IMC é {:.2f} e você está em obesidade.' .format(imc))
else:
    print('Seu IMC é {:.2f} e você está em obesidade mórbida.' .format(imc))
