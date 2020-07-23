lista = list(map(int, input().split()))
v1 = lista[0]

for pos in range(1, len(lista)):
    if lista[pos] > 0:
        v2 = lista[pos]
        break

soma = 0
for i in range(0, v2):
    valor = v1 + i
    soma += valor
print(soma)