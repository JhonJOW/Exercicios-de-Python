from datetime import date
hoje = date.today().year
nasc = int(input('Ano de nascimento: '))
idde = hoje - nasc
altm = nasc + 18
print('Quem nasceu em {} tem {} anos hoje.'.format(nasc, idde))
if nasc > hoje:
    print('Data \033[31mINVÁLIDA!\033[m')
elif idde < 18:
    print('Seu alistamento será em {}.'.format(altm))
elif idde == 18:
    print('Você deve se alistar IMEDIATAMENTE!')
else:
    print('Você já deveria ter se alistado há {} ano(s).'.format(hoje - altm))
    print('Seu alistamento foi em {}.'.format(altm))