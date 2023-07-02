print('=' * 30)
print('     10 TERMOS DE UMA PA')
print('=' * 30)
numero = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = numero + (10 - 1) * razao
for j in range(numero, decimo, razao):
    print('{} '.format(j), end='➜ ')
print('FIM!')
