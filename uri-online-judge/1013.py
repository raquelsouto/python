num1, num2, num3 = map(int, input().split())
maiorAB = (num1 + num2 + abs(num1 - num2))/2
maior_final = (maiorAB + num3 + abs(maiorAB - num3))/2
print('%d eh o maior' %(maior_final))
