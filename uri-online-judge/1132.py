num1 = int(input())
num2 = int(input())

if num1 > num2:
    temp = num1
    num1 = num2
    num2 = temp

soma = 0
for i in range(num1, num2+1):
    if i % 13 != 0:
        soma += i

print(soma)

