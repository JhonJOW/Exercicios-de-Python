print('-=-' * 12)
print('\033[1;31mAnalizador de trângulos:\033[m')
print('-=-' * 12)
a1 = float(input('\033[36mPrimeira aresta: '))
a2 = float(input('Segunda aresta: '))
a3 = float(input('Terceira aresta: \033[m'))
if a1 < a2 + a3 and a2 < a1 + a3 and a3 < a1 + a2:
    print('Os segmentos acima PODEM SIM formar um triângulo.')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo.')
