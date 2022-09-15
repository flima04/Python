preco = float(input('Digite o valor do produto'))
forma = str(input('Digite a forma de pagamento. Escolha entre: Dinheiro, Cheque, Cartão à vista, 2 ou mais parcelas(Digite apenas o número de parcelas)')).title()

if forma == 'Dinheiro' or forma == 'Cheque':
    print('Você tem direito a 10 porcento de desconto. O valor a pagar é R${:.2f}.' .format(preco-(preco*0.1)))
elif forma == 'Cartão':
    print('Você tem direito a 5 porcento de desconto. O valor a pagar é R${:.2f}.' .format(preco-(preco*0.05)))
elif forma == '2':
    print('O valor a pagar é R${:.2f}.' .format(preco))
else:
    print('Para compras a partir de 3 vezes o preço é acrescido de 20 porcento. O valor a pagar é R${:.2f}.' .format(preco+(preco*0.2)))
