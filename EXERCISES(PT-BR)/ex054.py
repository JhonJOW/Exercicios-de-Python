from datetime import date
x = date.today().year
menor = 0
maior = 0
for j in range(0,7):
    idade = int(input('Em que ano a {}ª pessoa nasceu? '))
    if x - idade < 18:
        menor += 1
    else:
        maior += 1
print('Ao todo tivemos {} pessoa(s) maior(s)\nde idade e {} menor(s) de idade.'.format(maior, menor))
