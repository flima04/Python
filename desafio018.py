import math

ang = float(input('Digite um ângulo e mostrarei seu seno, cosseno e tangente'))

sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))

print('O seno de {} é igual a {:.3f}' .format(ang, sen))
print('O cosseno de {} é igual a {:.3f}' .format(ang, cos))
print('A tangente de {} é igual a {:.3f}' .format(ang, tan))
