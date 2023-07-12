from time import sleep
continuar = True
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo  valor: '))
while continuar == True:
    print('    [ 1 ] Somar\n    [ 2 ] Multiplicar\n    [ 3 ] Maior\n    [ 4 ] Novos números\n    [ 5 ] Sair')
    opcao = int(input('>>>>> Qual é a sua opção? '))
    if opcao == 1:
        print('A soma entre {} + {} é {}'.format(num1, num2, num1 + num2))
    elif opcao == 2:
        print('A multiplicação entre {} x {} é {}'.format(num1, num2, num1 * num2))
    elif opcao == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print('Entre {} e {} o maior valor é {}'.format(num1, num2, maior))
    elif opcao == 4:
        print('Informe os valores novamente:')
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo  valor: '))
    elif opcao == 5:
        continuar = False
    else:
        print('Opção ínvalida!')
    print(11 * '=-=')
    sleep(1)
print('Saindo... Até mais!')
