v1 = int(input())
v2 = int(input())

if v2 <= v1:
    while v2 <= v1:
        v2 = int(input())

soma = 0
for i in range(1, v2):
    soma += v1
    v1 += 1
    if soma > v2:
        break
print(i)

            