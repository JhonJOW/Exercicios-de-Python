sexo = str(input('Informe seu sexo [M/F]: ')).upper().strip() [0]
while sexo not in 'MF':
    sexo = str(input('\033[31mDados inválidos.\033[m Informe seu sexo [M/F]: ')).upper().strip() [0]
print('Seu sexo foi registrado como {}'.format(sexo))
