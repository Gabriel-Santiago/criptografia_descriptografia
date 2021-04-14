print('Informe um número de 4 algarismos')
number = input('Digite um número: ')

if len(number) == 4:

    print('Escolha umas das opções abaixo:')
    print('1 - Criptografar')
    print('2 - Descriptografar')
    escolha = input()

    if escolha == '1':

        numberOne = int(number)

        unity = (numberOne // 1 % 10) + 6
        ten = (numberOne // 10 % 10) + 6
        hundred = (numberOne // 100 % 10) + 6
        thousands = (numberOne // 1000 % 10) + 6

        newThousands = ten % 10
        newHundred = unity % 10
        newTen = thousands % 10
        newUnity = hundred % 10

        milhar = str(newThousands)
        centena = str(newHundred)
        dezena = str(newTen)
        unidade = str(newUnity)

        cryptography = milhar + centena + dezena + unidade
        print('\n', cryptography)

    elif escolha == '2':

        numberTwo = int(number)

        unity = (numberTwo // 1 % 10) - 6
        ten = (numberTwo // 10 % 10) - 6
        hundred = (numberTwo // 100 % 10) - 6
        thousands = (numberTwo // 1000 % 10) - 6

        if thousands < 0:
            thousands += 10

        if hundred < 0:
            hundred += 10

        if ten < 0:
            ten += 10

        if unity < 0:
            unity += 10

        newThousands = ten
        newHundred = unity
        newTen = thousands
        newUnity = hundred

        milhar = str(newThousands)
        centena = str(newHundred)
        dezena = str(newTen)
        unidade = str(newUnity)

        decryption = milhar + centena + dezena + unidade
        print('\n', decryption)

    else:
        print('\033[1;31m' + '\nValor não correspondente')

else:
    print('\033[1;31m' + '\nValor não correspondente')
    print('\033[1;33m' + 'Tem que ser um valor de 4 algarismos')
