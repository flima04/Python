salario = float(input('Informe seu salario'))
imovel = float(input('Informe o valor do imovel'))
anos = int(input('Informe em quantos anos você deseja pagar o financiamento'))

meses = anos*12
prestacao = imovel/meses
salario30 = salario*0.3

if prestacao <= salario30:
    print('Financiamento aprovado! Sua prestação será R${} e deverá ser paga em {} meses.' .format(prestacao, meses))
else:
    print('Financiamento negado! A parcela excede 30 porcento do salario do comprador.')