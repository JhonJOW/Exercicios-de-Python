frase = str(input('Escreva uma frase: ')).upper().strip()
print('Sua frase tem {} A'.format(frase.count('A')))
print('O primeiro "a" aparece na posição {}'.format(frase.find('A')+1))
print('O ultimo "a" aparece na posição {}'.format(frase.rfind('A')+1))
