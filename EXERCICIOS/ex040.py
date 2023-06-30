mat = float(input('Nota de Matemática: '))
por = float(input('Nota de Português : '))
cie = float(input('Nota de Ciências  : '))
med = (mat+por+cie) / 3
print('A média do aluno é {:.1f}'.format(med))
if 10.0 < med:
    print('Média \033[31mINVÁLIDA\033[m')
elif med < 5.0:
    print('Aluno foi \033[31mREPROVADO\033[m')
elif 5.0 <= med < 6.9:
    print('Aluno está de \033[33mRECUPERAÇÃO\033[m')
else:
    print('Aluno foi \033[32mAPROVADO\033[m')
