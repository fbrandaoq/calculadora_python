while True: 
    # usuário informa os números
    x = str(input('Informe o primeiro número:')).replace(',','.')
    y = str(input('Informe o segundo número:')).replace(',','.')

    #converte para números decimais
    x = float(x)
    y = float(y)

    print('Operações disponivéis:\n')
    print('"+" para somar.')
    print('"-" para subtrair.')
    print('"*" para multiplicar.')
    print('"/" para dividir.')
    print('"%" para encontrar o resto da divisão.')
    

    op = input('Operação desejada:')

    match op:
        case '+':
            print(f'A soma é: {x + y}.')
        case '-':
            print(f'A subtração é: {x - y}.')
        case '*':
            print(f'A multiplicação é: {x * y}.')
        case '/':
            print(f'A divisão é: {x / y}.')
        case '%':
            print(f'O resto da divisão é: {x % y}.')
        case _:
            print('Operação invalida')
            continue # continue é interrompe o loop, volta para o próximo loop



