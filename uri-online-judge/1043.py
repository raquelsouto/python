valores = input().split()

valor1 = float(valores[0])
valor2 = float(valores[1])
valor3 = float(valores[2]) 

if (valor2 + valor3) > valor1 and (valor1 + valor3) > valor2 and (valor1 + valor2) > valor3:
    perimetro_triangulo = valor1 + valor2 + valor3
    print('Perimetro = %.1f' %perimetro_triangulo)

else:
    area = ((valor1 + valor2) * valor3) / 2
    print('Area = %.1f' %area)
