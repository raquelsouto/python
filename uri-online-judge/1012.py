base1, base2, altura = map(float, input().split())
pi = 3.14159
area_triangulo = (base1 * altura)/2
area_circulo = pi * altura**2
area_trapezio = ((base1 + base2)*altura)/2
area_quadrado = base2**2
area_retangulo = base1 * base2
print('TRIANGULO: %.3f' %area_triangulo)
print('CIRCULO: %.3f' %area_circulo)
print('TRAPEZIO: %.3f' %area_trapezio)
print('QUADRADO: %.3f' %area_quadrado)
print('RETANGULO: %.3f' %area_retangulo)
