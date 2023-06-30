from datetime import date
hoje = date.today().year
nasc = int(input('Ano de Nascimento: '))
idde = hoje - nasc
print('O atleta tem {} anos.'.format(idde))
if idde > 25:
    print('Classificação: MASTER')
elif idde > 19:
    print('Classificação: SÊNIOR')
elif idde > 14:
    print('Classificação: JÚNIOR')
elif idde > 9:
    print('Classificação: INFANTIL')
elif idde > 0:
    print('Classificação: MIRIM')
else:
    print('Data \033[31mINVÁLIDA!\033[m')
