n = int(input())
for i in range(n):
    entrada = input()
    leds = 0
    for letra in entrada:
        if letra == '1':
            leds += 2
        elif letra in ['2', '3', '5']:
            leds += 5
        elif letra == '4':
            leds += 4
        elif letra in ['6', '9', '0']:
            leds += 6
        elif letra == '7':
            leds += 3
        elif letra == '8':
            leds +=7
    print('%d leds' %leds)