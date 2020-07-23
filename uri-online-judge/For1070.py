num = int(input()) 

cont = 0
for i in range(1, 10001):
    if i % num == 2:
        print(num)
        cont += 1
print(cont)



