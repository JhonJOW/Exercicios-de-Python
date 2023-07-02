v1 = float(input('Primeiro segmento: '))
v2 = float(input('Segundo segmento : '))
v3 = float(input('Terceiro segmento: '))
if v1 < v2 + v3 and v2 < v1 + v3 and v3 < v1 + v2:
    if v1 == v2 == v3:
        print('Os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO.')
    elif v1 != v2 != v3 != v1:
        print('Os segmentos acima PODEM FORMAR um triângulo ESCALENO.')
    else:
        print('Os segmentos acima PODEM FORMAR um triângulo ISÓSCELES.')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo.')