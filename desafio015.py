d = float(input('Quantos dias o carro foi alugado?'))

km = float(input('Quantos km foram rodados?'))

v = (d*60)+(km*0.15)

print('O valor a ser pago pelo aluguel é de R${:.2f}' .format(v))
 