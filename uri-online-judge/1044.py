multiplos = input().split()
number1 = int(multiplos[0])
number2 = int(multiplos[1])

if (number1 % number2) == 0 or (number2 % number1) == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')